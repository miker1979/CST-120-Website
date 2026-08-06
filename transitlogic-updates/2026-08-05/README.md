# TransitLogic Carrier Workflow Update — August 5, 2026

This update documents the current TransitLogic browser prototype and the latest carrier-facing workflow changes.

## Simplified carrier search

The primary search now keeps only five controls visible:

- Pickup market
- Delivery market
- Equipment
- Pickup date
- Search Loads

Country, exact ZIP/postal code, radius, margin, posted-within window, maximum deadhead, and operating assumptions remain available under **More Filters**.

## Faster workflows

Quick presets were added for:

- My Home Terminal
- My Saved Lanes
- Low Deadhead
- Highest Profit
- Posted Recently

The KPI cards are now interactive so carriers can immediately open all loads, sort by lowest deadhead, edit fuel assumptions, filter high-profit freight, or isolate loss risks.

## State and profitability foundation

The active prototype also includes:

- Centralized local browser state through `storage.js`
- Draft auto-save and recovery for Post a Load
- Shipper/customer profile defaults
- Automatic postal-based route-mile estimates
- Gross revenue, fuel, operating expense, total expense, net profit, margin, loaded RPM, all-mile RPM, and break-even calculations
- Facility/customer requirements, driver restroom status, and nearby truck-stop or washout information
- Major freight markets backed by ZIP3/FSA and full postal intelligence
- Interactive Lower 48 state freight heat and directional lane intelligence

## Repository note

The production-sized postal datasets are not duplicated in this public update folder. They remain separate from the source update because of dataset size and licensing/attribution requirements. The complete working archive is maintained separately.

## Validation

JavaScript syntax and static HTML identifier/reference checks passed. Automated browser navigation was blocked by the execution environment's administrator policy, so this update does not claim a completed automated browser-render test.
