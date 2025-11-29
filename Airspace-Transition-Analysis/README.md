# Team Airspace

## Team members
- Brian Hockett (mgh2xx)


## Data Source

**What data source did you work with?**

- OpenSky API (https://openskynetwork.github.io/opensky-api/rest.html#all-state-vectors)
  - Used the /states/all endpoint to poll real-time aircraft state vectors, including position, altitude, velocity, and metadata. This endpoint was queried repeatedly to build the flight dataset.

- ESRI ArcGIS Airspace Boundaries API
  - Queried once to retrieve static U.S. airspace boundary geometry and attributes in GeoJSON. Used for enrichment of flight dataset and expanded analysis.


## Challenges / Obstacles

**What challenges did this data choice present in data gathering, processing and analysis, and how did you work through them? What methods and tools did you use to work with this data?**

&emsp;This data choice presented a number of challenges, at all stages of ELT + Analysis. 

&emsp;At the gathering/extraction stage, understanding the query parameters and rate limits was a significant challenge. The 4,000 API credits per day limit and the fact that the credits per API call varied depending on the total area of the call forced me to make a choice between analyzing a small area at high frequency, or a large area at a lowwer frequency. I made the decision to analyze a larger area (the Continental U.S) at low frequency (1 call every 90 seconds), which allowed me to ensure I would never go over the rate limit. Similarly, API access tokens lasted only 30 minutes, so I had to include a step in my producer script to check if my token was valid, and request a new one if it was not. I used Kafka to 


## Analysis

**Offer a brief analysis of the data with your findings. Keep it to one brief, clear, and meaningful paragraph.**


## Plot / Visualization

**Include at least one compelling plot or visualization of your work. Add images in your subdirectory and then display them using markdown in your README.md file.**

<table>
  <tr>
    <td><img src="StreamlitApp.png" width="1250"/></td>
  </tr>
  <tr>
    <td><img src="Cruising_Density.png" width="1250"/></td>
  </tr>
  <tr>
    <td><img src="Traffic_Density.png" width="1250"/></td>
  </tr>
  <tr>
    <td><img src="Planes_by_Airspace.png" width="1250"/></td>
  </tr>
</table>



## GitHub Repository

https://github.com/brianhockett/Airspace-Transition-Analysis
