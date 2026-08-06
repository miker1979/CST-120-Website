# TransitLogic Update Summary

## Profitability Engine

- Deadhead miles are now included in total operating miles.
- Fuel expense uses loaded miles plus deadhead miles.
- Operating expense uses loaded miles plus deadhead miles.
- True trip profit is revenue minus total fuel and operating expense.
- The board shows loaded-mile RPM, all-mile RPM, and true trip profit.
- Load details show profit per loaded mile, profit per all mile, break-even rate, and minimum target rate.

## Load Workflow

- Accepting a posted load removes it from the available board and moves it into Broker Operations.
- Broker Operations releases cleared freight into Driver Account after compliance, packet, and signed rate confirmation requirements are complete.
- Driver Account supports Dispatched → In Transit → Delivered status changes.
- Completed loads move into delivered history.

## Data and Reliability

- Load IDs start after the five reserved demonstration IDs and inspect all stored IDs before generating the next number.
- Stored and demonstration loads are merged by ID instead of duplicated.
- Demonstration dates are generated relative to the current date.
- Maryland, Delaware, Washington, D.C., and Alaska are mapped to regions; Hawaii and U.S. territories are outside the supported U.S. freight scope.
- Unrecognized locations use Other instead of silently defaulting to Central.
- User-provided values are escaped before table rendering.

## Interface

- View opens a structured profitability panel instead of a browser alert.
- Driver Account and Pricing are available from primary navigation.
- Pricing plan buttons now lead to relevant product pages.
- Margin and pickup-region filters have visible labels.
- ETA language identifies the result as an estimate based on a 50 MPH planning assumption.
- Post Load preview shows loaded miles, deadhead, total operating miles, loaded RPM, and all-mile RPM.

## Project Cleanup

- Removed the duplicate nested application copy.
- Removed repository internals and temporary Git files from the distribution ZIP.
- Added an optional Google Maps configuration file; manual mileage mode works without a key.

## Broker Operations & Carrier Compliance Update

- Load acceptance now moves freight into Broker Operations instead of directly into Driver Account.
- Added carrier authority, MC/FF, USDOT, COI, Auto Liability, and Cargo Insurance review fields.
- Added reusable carrier profiles.
- Added Broker–Carrier Agreement, W-9, carrier setup, and payment-term tracking.
- Added Rate Confirmation drafting, sent/signed status, and a printable rate-confirmation page.
- Added gated dispatch release with driver, facility, reference, and tracking information.
- Added BOL, POD, delivery, and invoice-ready workflow.
- Driver Account now receives freight only after broker dispatch release.

## Role-Based Registration Update

- Added a Business Account Registration page for freight brokers, shippers, and receivers.
- Freight broker registration captures legal company identity, MC and USDOT numbers, authority review status, BMC-84/BMC-85 bond or trust details, primary administrator, billing address, EIN, W-9 filename, and bond evidence filename.
- Shipper registration captures company and billing identity, logistics contact, EIN/W-9, credit status, bank and trade references, and a default origin facility with dock hours and scheduling preferences.
- Receiver registration provides a lightweight destination profile with exact facility address, gate instructions, receiving hours, dock contact, appointment requirements, scheduling software, lumper fee policy, and unloading constraints.
- Added role-specific validation, completion indicators, local account IDs, edit/delete controls, directory filtering, and browser-local persistence.
- Added Registration navigation to the active application pages.
- Prototype registrations remain pending until an authorized compliance or credit process verifies the supplied information.

## Modern Marketplace Dashboard

- Rebuilt the main load board as a modern carrier marketplace with a dark TransitLogic navigation bar and a compact freight-search workspace.
- Added origin, destination, equipment, margin, and sort controls.
- Added a collapsible true-profit settings panel for diesel, MPG, operating cost, profit target, and pickup-region assumptions.
- Added KPI cards for load count, average deadhead, diesel benchmark, high-profit opportunities, and loss risks.
- Added Quick Links, saved loads, saved searches, Lane Watch, and equipment-market conditions.
- Added browser-local saved searches and favorite-load bookmarks.
- Reworked load rows to show route, equipment, loaded/deadhead/all miles, loaded RPM, all-mile RPM, and true trip profit in a cleaner layout.
- Preserved the existing compliance handoff to Broker Operations when a carrier accepts a load.

## Region-based marketplace search

- Replaced free-text pickup and delivery search boxes with matching region dropdowns.
- Both dropdowns include All regions, Northeast, Southeast, Midwest, Central, Northwest, Southwest, and Other / Unknown.
- Updated filtering, saved searches, and the swap button to use region values.
- Removed the redundant Pickup Region field from More Filters.

## ZIP3 Freight Market Intelligence Update

- Added a reusable ZIP market reference file with representative ZIP5 codes, ZIP3 markets, regions, market names, and geographic centroids.
- Assigned exact pickup and delivery ZIP codes to all demonstration freight.
- Expanded the demonstration board with a dense recurring ZIP5 lane dataset across major freight markets.
- Changed the top marketplace selectors to region-grouped ZIP3 market dropdowns while preserving full-region choices.
- Added exact ZIP5/ZIP3 search, pickup and delivery radius options, posting-age filters, and maximum-deadhead filtering.
- Added a ZIP3 freight heat panel with separate outbound and inbound views.
- Added green high-freight, yellow medium-freight, red low-freight, and black no-recent-freight conditions.
- Added equipment and time-window controls for freight heat.
- Added ZIP3 lane scoring based on volume, true profitability, posting recency, and return-freight availability.
- Made ZIP market and lane cards clickable so drivers can immediately filter available loads.
- Updated load cards and load details to display exact ZIP codes, ZIP3 markets, and market names.
- Added required pickup and delivery ZIP fields to Post Load, including Google Places postal-code capture when Maps is configured.
- Saved searches now preserve ZIP markets, exact ZIP filters, radiuses, posting windows, deadhead limits, equipment, and margin settings.
- Radius calculations currently use market centroids and are clearly identified as prototype planning estimates.

## Directional ZIP5 Lane Intelligence & Bird's-Eye Map

- Expanded the demonstration market to 169 generated ZIP-coded loads across recurring directional freight corridors.
- Added representative full ZIP5 coverage for every prototype ZIP3 market.
- ZIP3 market cards now show the top exact pickup or delivery ZIP5 codes observed in the selected window.
- Added freshness-weighted regional freight density cards for a bird's-eye outbound or inbound market view.
- Added a self-contained freight network map with Region, ZIP3, and ZIP5 detail levels.
- Map line thickness represents load volume; line color can represent freight activity, profitability, or overall lane health.
- Added exact directional ZIP5 lane scoring with activity, profitability, recency, direct reverse freight, and destination return-market availability.
- Added confidence levels so sparse ZIP5 lanes are not presented with false precision.
- Exact ZIP5 scores blend with their parent ZIP3 trend until enough exact observations exist.
- Added a ranked Hot & Cold ZIP5 lane table with rate, RPM, deadhead, trip profit, return-market score, and one-click load filtering.
- Added watched zero-activity corridors so black No Freight conditions are visible in the prototype.

## Full U.S. and Canadian Postal Directory Update

- Replaced the representative ZIP-market directory with a nationwide location index.
- Added 33,537 U.S. ZIP records for the lower 48 states, Alaska, and Washington, D.C.
- Excluded Hawaii, Puerto Rico, Guam, the U.S. Virgin Islands, American Samoa, and the Northern Mariana Islands from the supported U.S. freight scope.
- Added 889 U.S. ZIP3 freight markets with the agreed TransitLogic regional assignments.
- California uses a configurable working boundary: 900–935 Southwest and 936–961 Northwest.
- Added all 1,665 Canadian FSAs and the official first-letter freight-region labels supplied for TransitLogic.
- Added 899,779 unique full Canadian postal codes in lazy-loaded first-letter data shards.
- Added country-aware origin, destination, exact-code, saved-search, load-posting, and lane-filter logic.
- Added Canadian domestic and U.S.–Canada cross-border demonstration lanes.
- Added visible SimpleMaps and GeoNames attribution.
- Exact Canadian postal records load only when needed so the initial dashboard remains responsive.

## Major Freight Market Search Update

- Replaced the driver-facing ZIP3/FSA dropdowns with 127 curated major U.S. and Canadian freight markets.
- Grouped major city and metro choices by TransitLogic U.S. region or Canadian first-letter postal region.
- Kept the complete U.S. ZIP and Canadian postal directories as the hidden validation, radius, lane, and heat-intelligence layer.
- Moved optional exact ZIP/postal and radius refinement directly beneath the pickup and delivery market selectors.
- Added metro-aware filtering that combines known ZIP3/FSA coverage with geographic market-radius matching.
- Reworked freight heat cards, market density, Lane Watch, and top-lane cards to use recognizable city/metro names.
- Preserved exact ZIP/postal directional lane tables and map detail for drivers who need precise location intelligence.
- Updated saved searches and lane-card actions to translate older ZIP3/FSA selections into the closest major market or exact postal filter.

## 2026-08-05 — Business Registration Cards and Postal Labels

- Added prominent role-selection cards for Freight Broker, Shipper, and Receiver registration.
- Broker registration covers legal identity, MC/USDOT authority, BMC-84/BMC-85 bond or trust details, account administrator, billing, EIN, and W-9 file-name tracking.
- Shipper registration covers business identity, billing, EIN, credit and trade references, logistics contact, and default origin-facility scheduling details.
- Receiver registration uses a lightweight facility profile with address, gate instructions, receiving hours, dock contact, appointment rules, scheduling software, lumper fees, and unloading constraints.
- Added a prototype sensitive-data warning and retained the explicit no-verification disclaimer.
- Restored representative ZIP3/FSA codes before major-market names in pickup and delivery menus and market intelligence cards.

## Geographic freight lane map correction

- Replaced the empty coordinate grid with actual U.S., Canada, and Mexico geographic outlines.
- Added separate Alaska and northern-Canada insets so continental markets are no longer compressed.
- Changed the default map detail to ZIP3/FSA and the default lane count to 10.
- Added collision-aware market-code labels and removed permanent exact-postal labels from the map.
- Exact postal codes remain available through the detail selector and lane summary.

## Selectable freight-map areas

- Changed the default freight overlay to the contiguous Lower 48 only.
- Added a Map Area selector for Lower 48, Canada, Alaska, and North America.
- Canada and Alaska are no longer drawn on the default map.
- Canada and Alaska use dedicated views; cross-border and Alaska-to-Lower-48 lanes use North America view.
- Pickup/delivery country and Alaska-market selections automatically choose the appropriate map area.

## 2026-08-05 — Facility Checklists and Nearby Driver Services

- Replaced the receiver's single unloading-constraints box with standardized registration checklists covering appointment/unloading, PPE and driver rules, trailer restrictions, dock procedures, freight handling, driver amenities, and washout requirements.
- Added a required three-state Driver Restroom Access field: Available, Not available, or Unknown, plus restroom-location/access details.
- Retained an Additional Instructions field for gate directions and exceptions that do not fit a standardized selection.
- Added generated Facility / Customer Info panels to load details, Broker Operations, Driver Account, and registration account cards.
- Added high-visibility warnings for appointment requirements, TWIC, lumper fees, no overnight parking, washout requirements, and unavailable restrooms.
- Added a browser-bundled driver-services index with 3,096 truck stop/fuel listings and 343 truck-wash listings; 54 wash entries are marked as confirmed washout-related records in the source data.
- Added nearest-service lookup using postal centroids. Washout-required facilities prioritize a confirmed washout listing when one is available.
- Added source and verification notices because straight-line distance is not truck-route mileage and directory services, hours, and access can change.

## 2026-08-05 — Carrier Marketplace Layout Order

- Moved the Carrier Marketplace load board, results toolbar, sidebar tools, and Available Loads table above the freight-intelligence and directional map section.
- Search filters and KPI summaries remain first, followed by the operational load board, then regional heat, map, and lane intelligence.
- No load filtering, booking, map, or facility-information behavior was changed.

## 2026-08-05 — Central State, Draft Recovery, and Route Profitability

- Added `js/storage.js`, a centralized TransitLogic state manager for customer profiles, active-customer selection, posted loads, per-customer last-used load settings, calculator preferences, and post-load drafts.
- Preserved the existing `customerProfiles`, `activeCustomerProfile`, `postedLoads`, and `transitLogic_loadDraft` keys as compatibility mirrors while the prototype migrates to the unified `transitLogic_state` record.
- Connected Customer Hub, Customer Profile, and Post a Load through the shared state manager.
- Added 650-millisecond debounced draft auto-save with Continue Draft and Discard Draft recovery controls.
- Added customer-specific last-used equipment, commodity, weight, deadhead, RPM, fuel, MPG, and operating-cost settings to the Saved Default selector after a successful posting.
- Added automatic postal-centroid route-mile estimation when Google Directions is not configured. Estimates are clearly labeled and use an editable/configurable road-distance factor.
- Added `js/calculator.js` and an Automatic Route Profitability panel with gross revenue, fuel, other operating costs, total expense, net profit, margin, all-mile RPM, and break-even loaded RPM.
- Saved route source, profitability results, and cost assumptions with newly posted load records.
- Moved the Post a Load integration code into `js/post-load.js` for a cleaner modular page structure.

## August 5, 2026 — Simplified Carrier Search Workflow

- Reduced the primary carrier search to pickup market, delivery market, equipment, pickup date, and Search Loads.
- Moved country, exact postal code, radius, margin, posting window, deadhead, and operating assumptions into More Filters.
- Added quick presets for home terminal, saved lanes, low deadhead, highest profit, and recently posted freight.
- Made dashboard KPI cards interactive so drivers can filter or sort directly from the metrics.
- Added pickup-date filtering and saved-search persistence for pickup dates.
- Added progressive radius controls that appear only after an exact ZIP or postal code is entered.
- Added `js/dashboard-controls.js` to separate workflow controls from the main load-board engine.
