# Team Airspace

## Team members
- Brian Hockett (mgh2xx)


## Data Source

**What data source did you work with?**

- OpenSky API (https://openskynetwork.github.io/opensky-api/rest.html#all-state-vectors)
  - Used the /states/all endpoint to poll real-time aircraft state vectors, including position, altitude, velocity, and metadata. This endpoint was queried repeatedly to build the flight dataset.

- ESRI ArcGIS Airspace Boundaries API
  - Queried once via the ArcGIS FeatureServer query operation to retrieve static U.S. airspace boundary geometry and attributes in GeoJSON. Used for enrichment of flight dataset and expanded analysis.


## Challenges / Obstacles

What challenges did this data choice present in data gathering, processing and analysis, and how did you work through them? What methods and tools did you use to work with this data?


## Analysis

Offer a brief analysis of the data with your findings. Keep it to one brief, clear, and meaningful paragraph.


## Plot / Visualization

Include at least one compelling plot or visualization of your work. Add images in your subdirectory and then display them using markdown in your README.md file.

## GitHub Repository

https://github.com/
