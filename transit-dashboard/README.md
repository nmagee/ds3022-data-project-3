# Team 

## Team Nyla Upal and Liam Ward



## Data Source

What data source did you work with?     
[API Docs](https://developer.wmata.com/docs/services/5476363f031f590f3809255b/operations/5476363f031f590d34cfc4f8)
We chose to work with bus route and stop data from the Washington Metropolitan Area Transit Authority API. It provides live bus locations, deviations, and trip metadata for the DC metro area. We chose this as it had continuously updating data on the buses, and it gave their longitude and latitude so they would be able to be displayed on a map.     

## Challenges / Obstacles

The tools used were Redpanda as a streaming platform for ingesting bus data. Docker Compose for container orchestration for reproducihbility and easy setup. Redis for in-memory data storage. DuckDB as a database for storing and querying bus positions. Streamlit and Plotly to create the interactive dashboard for real-time visualization and analysis.  

In order to get the continuous data from the bus position api, we used Apache Kafka to have a producer that got the positions of all the buses every 30 seconds. We then also had a consumer that read from the created bus positions topic and then wrote the bus information to a duckdb file. From this, the app file creates a dashboard using streamlit that has the live positions of the buses. Initially just using the bus position only gave the disconnected positions of the buses, so we had to use the path details api to get the entire routes and display those on the map as well. We also had issues getting the streamlit platform to refresh and update, which is why we had to use the streamlit autorefresh package to have it refresh every 30 seconds as the producer pulled updated positions. 

## Analysis

Offer a brief analysis of the data with your findings. Keep it to one brief, clear, and meaningful paragraph.    
- **Deviation Analysis**: The dashboard summarizes average, late, early, and on-time bus deviations per route.
- **Route Trends**: Visualizations reveal which routes experience the most delays or early arrivals.
- **Real-World Relevance**: Insights can inform transit planners and riders about service reliability.


## Plot / Visualization
     
![/workspaces/Transit-Dash/Visualization.png](Visualization.png)
*Live map of bus positions and deviation summary for a selected route.*

## GitHub Repository

https://github.com/liamward26/Transit-Dash
