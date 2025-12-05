# Team Casa Loma

## Team members

- Ethan Cao

## Data Source

What data source did you work with?
- I used LinkedIn's Job Board's guest API to manually scrape HTML data of job postings specifically for the Data Science Job Market. (Even more specifically, the data science internship job market in the United States.)

## Challenges / Obstacles

What challenges did this data choice present in data gathering, processing and analysis, and how did you work through them? What methods and tools did you use to work with this data?

- The main challenge I faced was the lack of a public API for LinkedIn's job postings, which meant I had to resort to web scraping techniques. To overcome this, I used Python's BeautifulSoup library to parse the HTML content and extract relevant job posting information. Additionally, I had to implement rate limiting and handle potential IP blocking by using proxies to avoid being detected as a bot.
  
- Another challenge was cleaning, structuring, and feature engineering of endpoints for my FastAPI as I need to ensure that not only the data is usable for meaningful analysis, but also that it is interesting enough to provide insights to the users of this dashboard. 

- The last challenge would be deploying the FastAPI on a cloud service platform called Render, and ensuring the Render can be successfully connected to my front end dashboard without CORS issues or other connectivity problems. Not to mention the design and deployment of the front end platform itself by using D3.js and HTML/CSS. I had to design and resolve bugs on both the front end and back end to ensure a smooth user experience.

## Analysis

Offer a brief analysis of the data with your findings. Keep it to one brief, clear, and meaningful paragraph.

I discovered that out of all the Data Science internship job postings collected, the majority of positions prefer proficiency in Python, SQL, Excel, PowerBI, and PowerPoint. Additionally, the skills that received significant attention over the 30 days are Apache Spark, Java, Data Bricks, and AWS. Indicating a growing demand for big data & cloud computing skills in the DS field. What's also interesting is that fact that job postings exploded during the end of October and the start of November, in which competition tend to be the highest at Monday 11:00AM and 15:00PM, the two time windows with the most amount of applications made. In contrary, competition tends ot be the lowest on Monday mornings at 6-7AM and Sunday nights at 9-11PM.

## Plot / Visualization

Include at least one compelling plot or visualization of your work. Add images in your subdirectory and then display them using markdown in your README.md file.

![Dashboard Screenshot 1](Screenshot%202025-12-02%20003646.png)

![Dashboard Screenshot 2](Screenshot%202025-12-02%20003703.png)

![Dashboard Screenshot 3](Screenshot%202025-12-02%20003821.png)

![Dashboard Screenshot 4](Screenshot%202025-12-02%20004944.png)


## GitHub Repository

https://github.com/JuneWayne/Job_Market_Stream/tree/main