/* =========================================================
   TRANSITLOGIC DASHBOARD CONTROLS
   Quick presets, clickable KPI cards, and progressive display
   for exact-postal radius controls. Kept separate from app.js
   so the carrier search workflow can evolve independently.
   ========================================================= */
(function () {
    "use strict";

    function byId(id) { return document.getElementById(id); }
    function refresh() { window.TransitLogicApp?.refresh?.(); }
    function setValue(id, value) {
        const element = byId(id);
        if (!element) return false;
        element.value = value;
        return true;
    }
    function toast(message) {
        const node = byId("boardToast");
        if (!node) return;
        node.textContent = message;
        node.classList.add("is-visible");
        window.clearTimeout(toast.timer);
        toast.timer = window.setTimeout(() => node.classList.remove("is-visible"), 2600);
    }
    function openAdvanced(focusId) {
        const panel = byId("advancedFilters");
        const button = byId("moreFiltersBtn");
        if (panel?.hidden) button?.click();
        window.setTimeout(() => byId(focusId)?.focus(), 80);
    }
    function applyAndRefresh(values, message) {
        Object.entries(values).forEach(([id, value]) => setValue(id, value));
        refresh();
        if (message) toast(message);
    }
    function profilePostal(profile) {
        if (!profile || typeof profile !== "object") return "";
        const candidates = [
            profile.homeTerminalPostal, profile.homeTerminalZip, profile.terminalZip,
            profile.postalCode, profile.zip, profile.address?.postalCode,
            profile.address?.zip, profile.terminalAddress?.postalCode,
            profile.terminalAddress?.zip, profile.companyAddress?.postalCode,
            profile.companyAddress?.zip
        ];
        return candidates.find(value => String(value || "").trim()) || "";
    }
    function applyHomeTerminal() {
        const profile = window.TransitLogicStorage?.getActiveProfile?.();
        const postal = profilePostal(profile);
        if (!postal) {
            toast("Add a home-terminal ZIP or postal code to the active carrier profile first.");
            return;
        }
        const zip = window.TransitLogicZip;
        const country = zip?.detectCountry?.(postal) || (/\d/.test(postal) ? "US" : "CA");
        setValue("originCountrySelect", country);
        byId("originCountrySelect")?.dispatchEvent(new Event("change", { bubbles: true }));
        const input = byId("originZipInput");
        if (input) {
            input.value = zip?.formatPostal?.(postal, country) || postal;
            input.dispatchEvent(new Event("input", { bubbles: true }));
            input.dispatchEvent(new Event("change", { bubbles: true }));
        }
        openAdvanced("originZipInput");
        toast("Home terminal applied to the pickup search.");
    }
    function applyPreset(name) {
        document.querySelectorAll("[data-search-preset]").forEach(button => {
            button.classList.toggle("is-active", button.dataset.searchPreset === name);
        });
        switch (name) {
            case "home": applyHomeTerminal(); break;
            case "saved": byId("showSavedSearches")?.click(); break;
            case "deadhead":
                applyAndRefresh({ maxDeadheadSelect: "50", sortSelect: "deadhead-low", profitFilter: "all" }, "Showing low-deadhead opportunities first.");
                break;
            case "profit":
                applyAndRefresh({ profitFilter: "high", sortSelect: "profit-high", maxDeadheadSelect: "all" }, "Showing the highest-profit loads first.");
                break;
            case "recent":
                applyAndRefresh({ searchTimeWindow: "1", sortSelect: "newest" }, "Showing loads posted in the last 24 hours.");
                break;
        }
    }
    function handleKpi(action) {
        switch (action) {
            case "all":
                applyAndRefresh({ profitFilter: "all", maxDeadheadSelect: "all", searchTimeWindow: "all" }, "Showing all loads in the current lane search.");
                break;
            case "deadhead":
                applyAndRefresh({ sortSelect: "deadhead-low" }, "Sorted by lowest deadhead.");
                break;
            case "fuel": openAdvanced("dieselInput"); break;
            case "profit":
                applyAndRefresh({ profitFilter: "high", sortSelect: "profit-high" }, "Filtered to high-profit loads.");
                break;
            case "risk":
                applyAndRefresh({ profitFilter: "loss", sortSelect: "profit-high" }, "Filtered to loads with negative true margin.");
                break;
        }
    }
    function syncRadius(inputId, fieldId, selectId) {
        const input = byId(inputId);
        const field = byId(fieldId);
        const select = byId(selectId);
        if (!input || !field || !select) return;
        const update = () => {
            const hasPostal = Boolean(input.value.trim());
            field.hidden = !hasPostal;
            select.disabled = !hasPostal;
            if (!hasPostal) select.value = "0";
        };
        input.addEventListener("input", update);
        input.addEventListener("change", update);
        update();
    }
    function init() {
        if (!byId("loadBoard")) return;
        document.querySelectorAll("[data-search-preset]").forEach(button => {
            button.addEventListener("click", () => applyPreset(button.dataset.searchPreset));
        });
        document.querySelectorAll("[data-kpi-action]").forEach(button => {
            button.addEventListener("click", () => handleKpi(button.dataset.kpiAction));
        });
        syncRadius("originZipInput", "originRadiusField", "originRadiusSelect");
        syncRadius("destinationZipInput", "destinationRadiusField", "destinationRadiusSelect");
        const date = byId("pickupDateSearch");
        if (date) date.min = new Date().toISOString().slice(0, 10);
    }
    document.addEventListener("DOMContentLoaded", init);
})();
