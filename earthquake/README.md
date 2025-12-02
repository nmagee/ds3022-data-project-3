# Team earhtquake

## Team members: Tsion Sahle (cnb8jw) and Eden Mulugeta (unb6ny)


## Data Source

What data source did you work with?

We used the SeismicPortal FDSN Event Web Service from EMSC/EPOS to get historical earthquake data. We first tried the real-time WebSocket, but the data came in too slowly and only showed current events, which wasn’t enough for the kind of time series analysis we wanted to do. The API let us download lots of past earthquake events at once and filter by things like time, location, depth, and magnitude. This made it easy to collect the data we needed and build a complete dataset for our analysis.


## Challenges / Obstacles

What challenges did this data choice present in data gathering, processing and analysis, and how did you work through them? What methods and tools did you use to work with this data?

One challenge we faced was understanding and interpreting the earthquake data in the context of seismology, since much of it was very detailed and technical. For example, the data often provided precise latitude and longitude instead of more general regional information, which made it tricky to analyze trends by location. We also wanted to create visualizations like maps, but the high level of specificity in the data limited what we could show clearly. To work around these issues, we focused on aggregating the data into manageable time periods and regions, and used Python tools like Pandas for data processing and Matplotlib for visualizations. This allowed us to extract meaningful insights without getting lost in overly granular details.

## Analysis

Offer a brief analysis of the data with your findings. Keep it to one brief, clear, and meaningful paragraph.

Our main goal was to understand how earthquake trends have shifted over the past five years by looking at time (years and seasons), depth, and location. We found that the number of strong earthquakes (magnitude ≥ 5.0) fluctuates from year to year, with peaks in 2021 and 2025 and lower counts in 2020 and 2024, showing no consistent increase or decrease. When looking at regions, some areas consistently appear in the top-10 lists each year, including Oaxaca (Mexico), the Island of Hawaii, Eastern and Western Turkey, Western Texas, Antofagasta (Chile), and the Puerto Rico region. As a curiosity, we also explored seasonal trends and noticed slightly higher activity in Fall and lower in Winter. Overall, our analysis and visualizations connect these dimensions—time, space, and depth—to help understand where and when strong earthquakes happen, which can inform disaster preparedness, risk assessment, and planning in these frequently affected regions. Understanding these patterns is relevant in the real world because it helps governments, engineers, and emergency planners prepare for, mitigate, and respond to earthquake risks more effectively.

## Plot / Visualization

Include at least one compelling plot or visualization of your work. Add images in your subdirectory and then display them using markdown in your README.md file.

## GitHub Repository

https://github.com/edenmulugeta1/data-project-3
