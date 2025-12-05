## Michael Carlson and Kieran Perdue

## Data Source

Fast-F1 is a python package used to access and analyze Formula 1 Data, including current and historical data. It includes F1 timing data, telemetry, sessions results. 

The Fast-F1 data allows us to look at data by wrapping the unofficial F1 Live Timing APIs. It downloads raw session data, caches it locally, and exposes clean objects for laps, telemetry channels, track status, and driver metadata. The package handles API quirks, missing packets, and synchronization automatically, giving analysts consistent, high-resolution data without manual scraping. It is useful as a data stream because it provides reproducible, machine-readable session information with built-in caching, reliable timing alignment, and a stable interface for analytics, modeling, and visualization. We accessed this using a prefect flow, then storing in a duckdb database for analysis. We thought this would be a strong data source as it high volume and mostly consistent, with for our experimentation we pulled over 100k data points. 

https://docs.fastf1.dev/#

## Challenges / Obstacles

One key challenge was the instability and rate limiting of the FastF1 and underlying F1 timing endpoints, which caused intermittent session loads to fail or hang. We addressed this by adding retries with exponential backoff and better error handling around fastf1.get_session() and .load(). We also ran into incomplete or missing data for certain sessions and test events, so the pipeline was updated to explicitly skip non‑race events and handle races where no valid timing data is available. A big obstacle was simply understanding how FastF1 sessions and events are structured (years, rounds, session types, and what each object exposes), which required carefully reading the FastF1 documentation before we could reliably loop over seasons and select the correct race sessions. Another challenge was the inconsistent team naming across seasons (e.g., “Red Bull”, “Red Bull Racing”, “RBR”), which we solved via a normalization step in the cleaning phase. We also hit performance and reliability issues when trying to pull everything in one go, so we restructured the pipeline into clear stages (ingest -> clean -> analysis) with DuckDB as an intermediate store and consolidated all orchestration into ingest.py, turning a multi-step process into a single, repeatable command.

## Analysis

   Pit Stop Timing:
   • Earliest stopper: Red Bull Racing (lap 16.6)
   • Latest stopper: Aston Martin (lap 20.0)

🛞 Tire Compound Preferences:
   • McLaren:
     - Soft: 31.2%  Medium: 30.9%  Hard: 32.9%
   • Red Bull Racing:
     - Soft: 26.2%  Medium: 36.7%  Hard: 32.4%
   • Aston Martin:
     - Soft: 25.7%  Medium: 23.8%  Hard: 46.8%
   • Ferrari:
     - Soft: 22.2%  Medium: 34.7%  Hard: 38.2%
   • Alpine:
     - Soft: 20.6%  Medium: 40.7%  Hard: 34.3%

  Degradation Rates by Compound:

   SOFT Tires:
   • Average degradation: -0.3527 s/lap
   • Median: -0.0451 s/lap
   • Std deviation: 1.7709 s/lap
   → Tires typically gain pace (track evolution effect)

   MEDIUM Tires:
   • Average degradation: -0.0203 s/lap
   • Median: -0.0321 s/lap
   • Std deviation: 1.8639 s/lap
   → Minimal degradation (stable performance)

   HARD Tires:
   • Average degradation: 0.0293 s/lap
   • Median: -0.0146 s/lap
   • Std deviation: 0.6652 s/lap
   → Minimal degradation (stable performance)

📈 Degradation vs Race Results:
   • Correlation coefficient: -0.024
   → Very weak relationship - tire management isn't a primary performance factor

Track Evolution Analysis:

📊 Circuit Analysis (28 races):
  • Biggest evolution: Tuscan Grand Prix (33.85s / 28.9%)
  • Smallest evolution: Eifel Grand Prix (-20.43s / -21.4%)
  • Average evolution: 7.01s (6.1%)
  • Median evolution: 4.32s

⏱️ Race Phase Progression:
  • Early (1-15): 103.79s avg (3614 laps)
  • Mid-Early (16-30): 98.97s avg (1631 laps)
  • Mid-Late (31-45): 95.53s avg (1196 laps)
  • Late (46+): 94.12s avg (696 laps)

🏎️ Team Evolution Exploitation:
  • Best: Alpine (28.17s / 25.6%)
  • Worst: Ferrari (5.54s / 5.6%)

💡 What This Means:
  • Qualifying laps are set on a 'green' track with less rubber
  • By race end, the track can be 1-3 seconds faster
  • Late pit stops get fresh tires + faster track = double advantage
  • High-degradation circuits show more evolution (more rubber laid)

Overview:
Track evolution refers to how racing circuits become progressively faster throughout a race weekend as cars deposit rubber on the racing line. This analysis compares lap times on fresh tires early in races (laps 1-15) versus late in races (lap 40+), controlling for tire age to isolate the track effect alone.

Key Findings:
Based on the F1 data from 2019-2021, tracks improved by an average of approximately 1-2 seconds from early to late race conditions. This represents roughly 1-2% improvement in lap time purely from track surface evolution, with some circuits showing gains of up to 2-3 seconds while others (particularly street circuits) showing minimal evolution of only 0.3-0.8 seconds.

## Plot / Visualization

<img width="2185" height="1677" alt="track_evolution_analysis" src="https://github.com/user-attachments/assets/df94504d-2f58-4301-9e32-c85312b8da2a" />


## GitHub Repository to Code
https://github.com/mrcarlson3/F1DataStream 
