## Michael Carlson and Kieran Perdue

## Data Source

Fast-F1 is a python package used to access and analyze Formula 1 Data, including current and historical data. It includes F1 timing data, telemetry, sessions results. 

The Fast-F1 data allows us to look at data by wrapping the unofficial F1 Live Timing APIs. It downloads raw session data, caches it locally, and exposes clean objects for laps, telemetry channels, track status, and driver metadata. The package handles API quirks, missing packets, and synchronization automatically, giving analysts consistent, high-resolution data without manual scraping. It is useful as a data stream because it provides reproducible, machine-readable session information with built-in caching, reliable timing alignment, and a stable interface for analytics, modeling, and visualization. We accessed this using a prefect flow, then storing in a duckdb database for analysis. We thought this would be a strong data source as it high volume and mostly consistent, with for our experimentation we pulled over 100k data points. 

https://docs.fastf1.dev/#

## Challenges / Obstacles

One key challenge was the instability and rate limiting of the FastF1 and underlying F1 timing endpoints, which caused intermittent session loads to fail or hang. We addressed this by adding retries with exponential backoff and better error handling around fastf1.get_session() and .load(). We also ran into incomplete or missing data for certain sessions and test events, so the pipeline was updated to explicitly skip non‑race events and handle races where no valid timing data is available. A big obstacle was simply understanding how FastF1 sessions and events are structured (years, rounds, session types, and what each object exposes), which required carefully reading the FastF1 documentation before we could reliably loop over seasons and select the correct race sessions. Another challenge was the inconsistent team naming across seasons (e.g., “Red Bull”, “Red Bull Racing”, “RBR”), which we solved via a normalization step in the cleaning phase. We also hit performance and reliability issues when trying to pull everything in one go, so we restructured the pipeline into clear stages (ingest -> clean -> analysis) with DuckDB as an intermediate store and consolidated all orchestration into ingest.py, turning a multi-step process into a single, repeatable command.

## Analysis



## Plot / Visualization

<img width="2185" height="1677" alt="track_evolution_analysis" src="https://github.com/user-attachments/assets/df94504d-2f58-4301-9e32-c85312b8da2a" />


## GitHub Repository to Code
https://github.com/mrcarlson3/F1DataStream 
