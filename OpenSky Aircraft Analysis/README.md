# Team OpenSky Aircraft Analysis

## Team Members
Margaux Reynolds

## Data Source

The data source I chose was the OpenSky Network States API, which provides real-time information on every aircraft currently in the air around the world. The API returns thousands of aircraft state vectors (position, country of origin, speed, altitude, etc.) with each request. I collected multiple API calls (each one representing a real-time snapshot) over time and stored them in DuckDB using a Prefect workflow.

## Challenges / Obstacles
What challenges did this data choice present in data gathering, processing and analysis, and how did you work through them? What methods and tools did you use to work with this data?

Even though the OpenSky API is straightforward to call, the volume and structure of the data created a few challenges. Each API response returns thousands of aircraft as long lists of values, so I had to carefully map each index to the correct field before inserting the data into my database. Another challenge was organizing repeated API calls in a clean way. I solved this by building a small Prefect pipeline that handled initialization, fetching, and insertion into DuckDB. After collecting almost 100,000 raw records, I created a separate cleaned table with readable timestamps, speed conversions, and filtered coordinates. Using DuckDB made it easy to run SQL queries during analysis, and Prefect helped keep the ingestion process organized and repeatable.

## Analysis

Offer a brief analysis of the data with your findings. Keep it to one brief, clear, and meaningful paragraph.

Over the three-minute collection window, the OpenSky API returned about 89,000 cleaned aircraft observations. The data shows a clear imbalance in aircraft origin, with the United States contributing by far the largest share of flights, followed by a much smaller group of countries like Australia, Canada, and China. The speed distribution highlights two main populations: commercial aircraft cruising between roughly 350–500 knots, and a separate cluster of slow or stationary aircraft close to zero knots, likely reflecting planes taxiing or parked on the ground. Aircraft counts across snapshots remained relatively steady, with only minor fluctuations as flights entered or exited real-time coverage. Overall, the dataset provides a useful short-term snapshot of global air traffic and reveals stable, interpretable patterns in aircraft origins and movement.

## Plot / Visualization

![Top Countries](visualizations/top_countries.png)

![Speed Histogram](visualizations/speed_histogram.png)

![Aircraft Over Time](visualizations/aircraft_over_time.png)
## GitHub Repository

https://github.com/margauxreynolds/opensky-flights-analysis
