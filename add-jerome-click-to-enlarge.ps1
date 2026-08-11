$ErrorActionPreference = "Stop"

$repo = "C:\Dev\01_ACTIVE_PROJECTS\GhostlineTechWebsite"
Set-Location $repo

$utf8NoBom = New-Object System.Text.UTF8Encoding($false)

$css = @'

    /* =================================================
       JEROME LOCATION LIGHTBOX
       ================================================= */
    .location-shot {
        cursor: zoom-in;
    }

    .location-shot img {
        transition: transform .22s ease, filter .22s ease;
    }

    .location-shot:hover img,
    .location-shot:focus img {
        transform: scale(1.035);
        filter: brightness(1.06);
    }

    .location-shot:focus {
        outline: 3px solid var(--az-cyan);
        outline-offset: 3px;
    }

    .jerome-lightbox {
        position: fixed;
        inset: 0;
        z-index: 99999;
        display: none;
        align-items: center;
        justify-content: center;
        padding: 28px;
        background: rgba(3, 5, 9, .94);
        backdrop-filter: blur(5px);
    }

    .jerome-lightbox.open {
        display: flex;
    }

    .jerome-lightbox-dialog {
        position: relative;
        display: flex;
        flex-direction: column;
        width: min(1500px, 96vw);
        max-height: 94vh;
        overflow: hidden;
        border: 1px solid rgba(255, 255, 255, .16);
        border-radius: 16px;
        background: #080a0f;
        box-shadow: 0 30px 90px rgba(0, 0, 0, .75);
    }

    .jerome-lightbox-image-wrap {
        display: flex;
        align-items: center;
        justify-content: center;
        min-height: 0;
        padding: 14px;
        background: #030405;
    }

    .jerome-lightbox img {
        display: block;
        max-width: 100%;
        max-height: calc(94vh - 95px);
        object-fit: contain;
        border-radius: 8px;
    }

    .jerome-lightbox-caption {
        margin: 0;
        padding: 13px 70px 15px 18px;
        color: #f3eadc;
        font-size: .92rem;
        line-height: 1.45;
        background: #0d1016;
    }

    .jerome-lightbox-close {
        position: absolute;
        top: 12px;
        right: 12px;
        z-index: 2;
        width: 44px;
        height: 44px;
        border: 1px solid rgba(255, 255, 255, .25);
        border-radius: 50%;
        background: rgba(8, 10, 15, .92);
        color: #fff;
        font-size: 28px;
        line-height: 38px;
        cursor: pointer;
    }

    .jerome-lightbox-close:hover,
    .jerome-lightbox-close:focus {
        background: var(--az-oxblood);
        outline: none;
    }

    body.jerome-lightbox-open {
        overflow: hidden;
    }

    @media (max-width: 767.98px) {
        .jerome-lightbox {
            padding: 10px;
        }

        .jerome-lightbox-dialog {
            width: 98vw;
            max-height: 96vh;
        }

        .jerome-lightbox img {
            max-height: calc(96vh - 90px);
        }
    }
    /* END JEROME LOCATION LIGHTBOX */
'@

$markup = @'

<div id="jeromeLocationLightbox"
     class="jerome-lightbox"
     aria-hidden="true">
    <div class="jerome-lightbox-dialog"
         role="dialog"
         aria-modal="true"
         aria-labelledby="jeromeLightboxCaption">
        <button type="button"
                class="jerome-lightbox-close"
                aria-label="Close enlarged image">&times;</button>

        <div class="jerome-lightbox-image-wrap">
            <img id="jeromeLightboxImage" src="" alt="">
        </div>

        <p id="jeromeLightboxCaption"
           class="jerome-lightbox-caption"></p>
    </div>
</div>
'@

$js = @'

<script>
(function () {
    const lightbox = document.getElementById("jeromeLocationLightbox");
    if (!lightbox) return;

    const lightboxImage = document.getElementById("jeromeLightboxImage");
    const lightboxCaption = document.getElementById("jeromeLightboxCaption");
    const closeButton = lightbox.querySelector(".jerome-lightbox-close");
    const shots = document.querySelectorAll(".location-shot");

    let lastTrigger = null;

    function openLightbox(figure) {
        const image = figure.querySelector("img");
        const badge = figure.querySelector("figcaption");
        const card = figure.closest(".location-card");
        const locationTitle = card ? card.querySelector("h3") : null;

        if (!image) return;

        lastTrigger = figure;
        lightboxImage.src = image.currentSrc || image.src;
        lightboxImage.alt = image.alt || "Enlarged Jerome location image";

        const labelParts = [];
        if (locationTitle && locationTitle.textContent.trim()) {
            labelParts.push(locationTitle.textContent.trim());
        }
        if (badge && badge.textContent.trim()) {
            labelParts.push(badge.textContent.trim());
        }

        lightboxCaption.textContent = labelParts.join(" — ");
        lightbox.classList.add("open");
        lightbox.setAttribute("aria-hidden", "false");
        document.body.classList.add("jerome-lightbox-open");
        closeButton.focus();
    }

    function closeLightbox() {
        lightbox.classList.remove("open");
        lightbox.setAttribute("aria-hidden", "true");
        document.body.classList.remove("jerome-lightbox-open");
        lightboxImage.src = "";

        if (lastTrigger) {
            lastTrigger.focus();
        }
    }

    shots.forEach(function (figure) {
        figure.setAttribute("tabindex", "0");
        figure.setAttribute("role", "button");

        const image = figure.querySelector("img");
        if (image && image.alt) {
            figure.setAttribute("aria-label", "Enlarge " + image.alt);
        } else {
            figure.setAttribute("aria-label", "Enlarge location image");
        }

        figure.addEventListener("click", function () {
            openLightbox(figure);
        });

        figure.addEventListener("keydown", function (event) {
            if (event.key === "Enter" || event.key === " ") {
                event.preventDefault();
                openLightbox(figure);
            }
        });
    });

    closeButton.addEventListener("click", closeLightbox);

    lightbox.addEventListener("click", function (event) {
        if (event.target === lightbox) {
            closeLightbox();
        }
    });

    document.addEventListener("keydown", function (event) {
        if (event.key === "Escape" && lightbox.classList.contains("open")) {
            closeLightbox();
        }
    });
})();
</script>
'@

$files = @(
    ".\arizona-paranormal.html",
    ".\arizona-paranormal-v2.html"
)

foreach ($file in $files) {
    if (-not (Test-Path $file)) {
        throw "Could not find $file"
    }

    $path = (Resolve-Path $file).Path
    $html = [System.IO.File]::ReadAllText($path, [System.Text.Encoding]::UTF8)

    # Remove prior version if this script is run again.
    $html = [regex]::Replace(
        $html,
        '(?s)\s*/\* =================================================\s*JEROME LOCATION LIGHTBOX\s*================================================= \*/.*?/\* END JEROME LOCATION LIGHTBOX \*/',
        ''
    )

    $html = [regex]::Replace(
        $html,
        '(?s)\s*<div id="jeromeLocationLightbox".*?</div>\s*</div>\s*',
        ''
    )

    $html = [regex]::Replace(
        $html,
        '(?s)\s*<script>\s*\(function \(\) \{\s*const lightbox = document\.getElementById\("jeromeLocationLightbox"\);.*?</script>',
        ''
    )

    if ($html -notmatch '</style>') {
        throw "No </style> tag found in $file"
    }

    if ($html -notmatch '</body>') {
        throw "No </body> tag found in $file"
    }

    $html = $html.Replace("</style>", "$css`r`n</style>")
    $html = $html.Replace("</body>", "$markup`r`n$js`r`n</body>")

    [System.IO.File]::WriteAllText($path, $html, $utf8NoBom)

    Write-Host "Added click-to-enlarge lightbox to $file" -ForegroundColor Green
}

Write-Host ""
Write-Host "Done. Refresh Live Server with Ctrl+F5, then click any Real Location or Game Render image." -ForegroundColor Cyan
