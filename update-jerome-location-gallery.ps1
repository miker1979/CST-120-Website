$ErrorActionPreference = "Stop"

$repo = "C:\Dev\01_ACTIVE_PROJECTS\GhostlineTechWebsite"
Set-Location $repo

Write-Host ""
Write-Host "=== Jerome website photo update ===" -ForegroundColor Cyan
Write-Host "Repository: $repo"

# ------------------------------------------------------------
# 1. Normalize the image folder name for web-safe URLs
# ------------------------------------------------------------
$oldFolder = Join-Path $repo "images\Jerome Locations"
$newFolder = Join-Path $repo "images\jerome-locations"

if ((Test-Path $oldFolder) -and -not (Test-Path $newFolder)) {
    Rename-Item -Path $oldFolder -NewName "jerome-locations"
    Write-Host "Renamed images\Jerome Locations -> images\jerome-locations" -ForegroundColor Green
}

if (-not (Test-Path $newFolder)) {
    throw "Could not find images\jerome-locations (or the original images\Jerome Locations folder)."
}

$game = Join-Path $newFolder "Game"
$real = Join-Path $newFolder "Real"

if (-not (Test-Path $game)) { throw "Game folder not found: $game" }
if (-not (Test-Path $real)) { throw "Real folder not found: $real" }

# ------------------------------------------------------------
# 2. Keep the newest renders under the final web filenames
# ------------------------------------------------------------

# Gold King: use the newer equipment-yard render.
$newGoldGame = Join-Path $game "gold-king-haynes.png"
$finalGoldGame = Join-Path $game "gold-king-haynes-game.png"
if (Test-Path $newGoldGame) {
    if (Test-Path $finalGoldGame) { Remove-Item $finalGoldGame -Force }
    Rename-Item $newGoldGame "gold-king-haynes-game.png"
    Write-Host "Updated Gold King game render." -ForegroundColor Green
}

# High School: use the newer centered historic-entrance render.
$newSchoolGame = Join-Path $game "moonlit_entrance_investigation.png"
$finalSchoolGame = Join-Path $game "old-jerome-high-school-game.png"
if (Test-Path $newSchoolGame) {
    if (Test-Path $finalSchoolGame) { Remove-Item $finalSchoolGame -Force }
    Rename-Item $newSchoolGame "old-jerome-high-school-game.png"
    Write-Host "Updated Old Jerome High School game render." -ForegroundColor Green
}

# Cemetery canon change: Pioneer Graveyard replaces Hogback.
$oldPioneerGame = Join-Path $game "jerome-pioneer-graveyard.png"
$finalPioneerGame = Join-Path $game "jerome-pioneer-graveyard-game.png"
if (Test-Path $oldPioneerGame) {
    if (Test-Path $finalPioneerGame) { Remove-Item $finalPioneerGame -Force }
    Rename-Item $oldPioneerGame "jerome-pioneer-graveyard-game.png"
    Write-Host "Renamed Pioneer Graveyard game render." -ForegroundColor Green
}

# Use the newer ground-level Gold King photo for the website Real image when present.
$goldGroundPhoto = Join-Path $newFolder "kings mine ghost town 2.jpg"
$goldReal = Join-Path $real "gold-king-haynes.jpg"
if (Test-Path $goldGroundPhoto) {
    Copy-Item $goldGroundPhoto $goldReal -Force
    Write-Host "Updated Gold King real-world reference photo." -ForegroundColor Green
}

# ------------------------------------------------------------
# 3. Verify all 12 real/game pairs
# ------------------------------------------------------------
$pairs = @(
    @("jerome-grand-hotel.jpg", "jerome-grand-hotel-game.png"),
    @("gold-king-haynes.jpg", "gold-king-haynes-game.png"),
    @("douglas-mansion.jpg", "douglas-mansion-game.png"),
    @("connor-hotel.jpg", "connor-hotel-game.png"),
    @("jennies-place.png", "jennies-place-game.png"),
    @("haunted-hamburger.png", "haunted-hamburger-game.png"),
    @("old-jerome-high-school.png", "old-jerome-high-school-game.png"),
    @("little-daisy-hotel.jpg", "little-daisy-hotel-game.png"),
    @("new-state-motor-company.png", "new-state-motor-company-game.png"),
    @("liberty-theatre.jpg", "liberty-theatre-game.png"),
    @("jerome-pioneer-graveyard.jpg", "jerome-pioneer-graveyard-game.png"),
    @("episcopal-christ-church.jpeg", "episcopal-christ-church-game.png")
)

$missing = @()
foreach ($pair in $pairs) {
    if (-not (Test-Path (Join-Path $real $pair[0]))) { $missing += "Real\$($pair[0])" }
    if (-not (Test-Path (Join-Path $game $pair[1]))) { $missing += "Game\$($pair[1])" }
}

if ($missing.Count -gt 0) {
    Write-Host ""
    Write-Host "Missing required files:" -ForegroundColor Red
    $missing | ForEach-Object { Write-Host "  $_" -ForegroundColor Red }
    throw "Fix the missing files above before continuing."
}

Write-Host "All 12 real/game image pairs are present." -ForegroundColor Green

# ------------------------------------------------------------
# 4. Update Arizona Paranormal v2 page
# ------------------------------------------------------------
$htmlPath = Join-Path $repo "arizona-paranormal-v2.html"
if (-not (Test-Path $htmlPath)) {
    throw "arizona-paranormal-v2.html was not found in the repository root."
}

$html = [System.IO.File]::ReadAllText($htmlPath, [System.Text.Encoding]::UTF8)

$galleryCss = @'
    /* JEROME LOCATION COMPARISON GALLERY */
    .location-card{
      height:100%;
      overflow:hidden;
      padding:0;
    }
    .location-card-body{
      padding:1.35rem 1.45rem 1.55rem;
    }
    .location-compare{
      display:grid;
      grid-template-columns:1fr 1fr;
      gap:.65rem;
      padding:.7rem;
      border-bottom:1px solid var(--az-border);
      background:#0a0c12;
    }
    .location-shot{
      position:relative;
      overflow:hidden;
      margin:0;
      aspect-ratio:16/10;
      border:1px solid rgba(255,255,255,.13);
      border-radius:10px;
      background:#050608;
    }
    .location-shot img{
      display:block;
      width:100%;
      height:100%;
      object-fit:cover;
    }
    .location-shot figcaption{
      position:absolute;
      top:.45rem;
      left:.45rem;
      margin:0;
      padding:.28rem .48rem;
      border-radius:999px;
      background:rgba(7,9,13,.84);
      color:#f3eadc;
      font-size:.62rem;
      font-weight:900;
      letter-spacing:.04rem;
      text-transform:uppercase;
      box-shadow:0 2px 10px rgba(0,0,0,.32);
    }
    .location-shot.game figcaption{
      background:rgba(125,31,48,.9);
    }
    .location-card h3{
      margin-top:.2rem;
    }
    body.arizona-page.dark-mode .location-compare{
      border-bottom-color:#3b4657;
    }
    @media(max-width:575.98px){
      .location-compare{grid-template-columns:1fr;}
    }
    /* END JEROME LOCATION COMPARISON GALLERY */
'@

# Replace previous gallery CSS if script is run more than once; otherwise insert it.
$cssPattern = '(?s)\s*/\* JEROME LOCATION COMPARISON GALLERY \*/.*?/\* END JEROME LOCATION COMPARISON GALLERY \*/'
if ([regex]::IsMatch($html, $cssPattern)) {
    $html = [regex]::Replace($html, $cssPattern, "`r`n$galleryCss")
} else {
    $html = $html.Replace("</style>", "$galleryCss`r`n  </style>")
}

$locationSection = @'
<section id="locations" class="az-section-alt">
  <div class="container">
    <div class="text-center mb-5">
      <p class="section-label">Locked Main Locations</p>
      <h2 class="section-title">Real Jerome locations become <span class="az-accent">playable environments.</span></h2>
      <p class="lead az-lead">Each location now pairs a real-world reference photo with the current in-game visual direction. The game renders preserve recognizable architecture while shifting each site into the moonlit first-person investigation style.</p>
    </div>

    <div class="row">

      <div class="col-lg-6 mb-4">
        <article class="location-card h-100">
          <div class="location-compare">
            <figure class="location-shot"><img src="images/jerome-locations/Real/jerome-grand-hotel.jpg" alt="Real-world photograph of the Jerome Grand Hotel"><figcaption>Real Location</figcaption></figure>
            <figure class="location-shot game"><img src="images/jerome-locations/Game/jerome-grand-hotel-game.png" alt="Game render of the Jerome Grand Hotel investigation"><figcaption>Game Render</figcaption></figure>
          </div>
          <div class="location-card-body"><div class="d-flex justify-content-between align-items-start"><span class="location-number">01</span><span class="location-status">Primary investigation hub</span></div><h3>Jerome Grand Hotel / United Verde Hospital</h3><p>Historic hospital and hotel layers anchor the modern investigation and the earliest major supernatural escalation.</p></div>
        </article>
      </div>

      <div class="col-lg-6 mb-4">
        <article class="location-card h-100">
          <div class="location-compare">
            <figure class="location-shot"><img src="images/jerome-locations/Real/gold-king-haynes.jpg" alt="Real-world photograph of Gold King Mine and Ghost Town"><figcaption>Real Location</figcaption></figure>
            <figure class="location-shot game"><img src="images/jerome-locations/Game/gold-king-haynes-game.png" alt="Game render of the Gold King Mine and Haynes investigation"><figcaption>Game Render</figcaption></figure>
          </div>
          <div class="location-card-body"><div class="d-flex justify-content-between align-items-start"><span class="location-number">02</span><span class="location-status">Finale location</span></div><h3>Gold King Mine &amp; Ghost Town / Haynes</h3><p>The story ultimately returns to the historical Haynes site for the binding attempt and the final outcome.</p></div>
        </article>
      </div>

      <div class="col-lg-6 mb-4">
        <article class="location-card h-100">
          <div class="location-compare">
            <figure class="location-shot"><img src="images/jerome-locations/Real/douglas-mansion.jpg" alt="Real-world photograph of Douglas Mansion"><figcaption>Real Location</figcaption></figure>
            <figure class="location-shot game"><img src="images/jerome-locations/Game/douglas-mansion-game.png" alt="Game render of Douglas Mansion"><figcaption>Game Render</figcaption></figure>
          </div>
          <div class="location-card-body"><div class="d-flex justify-content-between align-items-start"><span class="location-number">03</span><span class="location-status">Main investigation</span></div><h3>Douglas Mansion</h3><p>A major historical location used for evidence, story progression, and the town's mining-era context.</p></div>
        </article>
      </div>

      <div class="col-lg-6 mb-4">
        <article class="location-card h-100">
          <div class="location-compare">
            <figure class="location-shot"><img src="images/jerome-locations/Real/connor-hotel.jpg" alt="Real-world photograph of the Connor Hotel"><figcaption>Real Location</figcaption></figure>
            <figure class="location-shot game"><img src="images/jerome-locations/Game/connor-hotel-game.png" alt="Game render of the Connor Hotel"><figcaption>Game Render</figcaption></figure>
          </div>
          <div class="location-card-body"><div class="d-flex justify-content-between align-items-start"><span class="location-number">04</span><span class="location-status">Main investigation</span></div><h3>Connor Hotel</h3><p>A locked story location at Main Street and Jerome Avenue, tied into the investigation route through central Jerome.</p></div>
        </article>
      </div>

      <div class="col-lg-6 mb-4">
        <article class="location-card h-100">
          <div class="location-compare">
            <figure class="location-shot"><img src="images/jerome-locations/Real/jennies-place.png" alt="Real-world photograph of Jennie's Place and Nellie Bly"><figcaption>Real Location</figcaption></figure>
            <figure class="location-shot game"><img src="images/jerome-locations/Game/jennies-place-game.png" alt="Game render of Jennie's Place"><figcaption>Game Render</figcaption></figure>
          </div>
          <div class="location-card-body"><div class="d-flex justify-content-between align-items-start"><span class="location-number">05</span><span class="location-status">Main investigation</span></div><h3>Jennie's Place / Nellie Bly</h3><p>A canonical investigation space used to uncover evidence and move the story forward through Jerome's historic commercial district.</p></div>
        </article>
      </div>

      <div class="col-lg-6 mb-4">
        <article class="location-card h-100">
          <div class="location-compare">
            <figure class="location-shot"><img src="images/jerome-locations/Real/haunted-hamburger.png" alt="Real-world photograph of the Haunted Hamburger"><figcaption>Real Location</figcaption></figure>
            <figure class="location-shot game"><img src="images/jerome-locations/Game/haunted-hamburger-game.png" alt="Game render of the Haunted Hamburger"><figcaption>Game Render</figcaption></figure>
          </div>
          <div class="location-card-body"><div class="d-flex justify-content-between align-items-start"><span class="location-number">06</span><span class="location-status">Main investigation</span></div><h3>Haunted Hamburger</h3><p>A modern Jerome landmark folded into the supernatural investigation and the town's living history.</p></div>
        </article>
      </div>

      <div class="col-lg-6 mb-4">
        <article class="location-card h-100">
          <div class="location-compare">
            <figure class="location-shot"><img src="images/jerome-locations/Real/old-jerome-high-school.png" alt="Real-world exterior reference of Old Jerome High School"><figcaption>Real Location</figcaption></figure>
            <figure class="location-shot game"><img src="images/jerome-locations/Game/old-jerome-high-school-game.png" alt="Game render of the Old Jerome High School entrance"><figcaption>Game Render</figcaption></figure>
          </div>
          <div class="location-card-body"><div class="d-flex justify-content-between align-items-start"><span class="location-number">07</span><span class="location-status">Main investigation</span></div><h3>Old Jerome High School</h3><p>A canonical exploration site where environmental storytelling and paranormal pressure can intensify.</p></div>
        </article>
      </div>

      <div class="col-lg-6 mb-4">
        <article class="location-card h-100">
          <div class="location-compare">
            <figure class="location-shot"><img src="images/jerome-locations/Real/little-daisy-hotel.jpg" alt="Real-world photograph of the Little Daisy Hotel"><figcaption>Real Location</figcaption></figure>
            <figure class="location-shot game"><img src="images/jerome-locations/Game/little-daisy-hotel-game.png" alt="Game render of the Little Daisy Hotel"><figcaption>Game Render</figcaption></figure>
          </div>
          <div class="location-card-body"><div class="d-flex justify-content-between align-items-start"><span class="location-number">08</span><span class="location-status">Main investigation</span></div><h3>Little Daisy Hotel</h3><p>A historic location connected to Jerome's mining history and the wider evidence network.</p></div>
        </article>
      </div>

      <div class="col-lg-6 mb-4">
        <article class="location-card h-100">
          <div class="location-compare">
            <figure class="location-shot"><img src="images/jerome-locations/Real/new-state-motor-company.png" alt="Real-world photograph of the New State Motor Company Building"><figcaption>Real Location</figcaption></figure>
            <figure class="location-shot game"><img src="images/jerome-locations/Game/new-state-motor-company-game.png" alt="Game render of the New State Motor Company Building"><figcaption>Game Render</figcaption></figure>
          </div>
          <div class="location-card-body"><div class="d-flex justify-content-between align-items-start"><span class="location-number">09</span><span class="location-status">Main investigation</span></div><h3>New State Motor Company Building</h3><p>A canonical town location supporting investigation, environmental storytelling, and encounter variation.</p></div>
        </article>
      </div>

      <div class="col-lg-6 mb-4">
        <article class="location-card h-100">
          <div class="location-compare">
            <figure class="location-shot"><img src="images/jerome-locations/Real/liberty-theatre.jpg" alt="Real-world photograph of Liberty Theatre"><figcaption>Real Location</figcaption></figure>
            <figure class="location-shot game"><img src="images/jerome-locations/Game/liberty-theatre-game.png" alt="Game render of Liberty Theatre"><figcaption>Game Render</figcaption></figure>
          </div>
          <div class="location-card-body"><div class="d-flex justify-content-between align-items-start"><span class="location-number">10</span><span class="location-status">Main investigation</span></div><h3>Liberty Theatre</h3><p>A Main Street landmark used as one of the game's locked story locations.</p></div>
        </article>
      </div>

      <div class="col-lg-6 mb-4">
        <article class="location-card h-100">
          <div class="location-compare">
            <figure class="location-shot"><img src="images/jerome-locations/Real/jerome-pioneer-graveyard.jpg" alt="Real-world photograph of Jerome Pioneer Graveyard"><figcaption>Real Location</figcaption></figure>
            <figure class="location-shot game"><img src="images/jerome-locations/Game/jerome-pioneer-graveyard-game.png" alt="Game render of Jerome Pioneer Graveyard"><figcaption>Game Render</figcaption></figure>
          </div>
          <div class="location-card-body"><div class="d-flex justify-content-between align-items-start"><span class="location-number">11</span><span class="location-status">Main investigation</span></div><h3>Jerome Pioneer Graveyard</h3><p>A historic hillside burial ground tied to death records, memory, spiritual residue, and Jerome's unresolved past.</p></div>
        </article>
      </div>

      <div class="col-lg-6 mb-4">
        <article class="location-card h-100">
          <div class="location-compare">
            <figure class="location-shot"><img src="images/jerome-locations/Real/episcopal-christ-church.jpeg" alt="Real-world photograph of the Jerome Episcopal Christ Church"><figcaption>Real Location</figcaption></figure>
            <figure class="location-shot game"><img src="images/jerome-locations/Game/episcopal-christ-church-game.png" alt="Game render of the Jerome Episcopal Christ Church"><figcaption>Game Render</figcaption></figure>
          </div>
          <div class="location-card-body"><div class="d-flex justify-content-between align-items-start"><span class="location-number">12</span><span class="location-status">Main investigation</span></div><h3>Jerome Episcopal Christ Church</h3><p>A church location supporting the spiritual, ritual, and historical side of the investigation.</p></div>
        </article>
      </div>

    </div>
  </div>
</section>
'@

$sectionPattern = '(?s)<section id="locations" class="az-section-alt">.*?</section>'
if (-not [regex]::IsMatch($html, $sectionPattern)) {
    throw "Could not locate the current #locations section in arizona-paranormal-v2.html."
}
$html = [regex]::Replace($html, $sectionPattern, [System.Text.RegularExpressions.MatchEvaluator]{ param($m) $locationSection }, 1)

# Update hero / social preview to the new game render.
$html = $html.Replace("images/jerome-hotel-gameplay.png", "images/jerome-locations/Game/jerome-grand-hotel-game.png")
$html = $html.Replace("https://ghostlinetech.com/images/jerome-hotel-gameplay.png", "https://ghostlinetech.com/images/jerome-locations/Game/jerome-grand-hotel-game.png")

# Save UTF-8 without BOM.
$utf8NoBom = New-Object System.Text.UTF8Encoding($false)
[System.IO.File]::WriteAllText($htmlPath, $html, $utf8NoBom)

# Keep the public canonical URL current without changing existing site links.
Copy-Item $htmlPath (Join-Path $repo "arizona-paranormal.html") -Force

Write-Host ""
Write-Host "Website page updated successfully." -ForegroundColor Green
Write-Host "Updated:"
Write-Host "  arizona-paranormal-v2.html"
Write-Host "  arizona-paranormal.html"
Write-Host ""
Write-Host "Next: preview arizona-paranormal.html in Live Server, then commit/push." -ForegroundColor Cyan
