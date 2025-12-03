# Global Terrorism: How Has it Changed and How is it Reported?

### Authors: Teagan Britten and Vinith Jayamani 

## Data Source
Global Terrorism Database (GTD):
https://www.start.umd.edu/data-tools/GTD


## Codebook
GTD Codebook (under “GTD Codebook”):
https://www.start.umd.edu/using-gtd


Our data has been collected from two separate locations to facilitate our analysis. One of these sources is the Global Terrorism Database, or GTD, that contains information on over two hundred thousand terrorist attacks dating back to 1970. Entries include the type of attack, the location, and the suspected motive or affiliation of the attacker/s.
The other source used is the News API, which draws news articles from over one hundred and fifty thousand sources worldwide. We were able to filter the news api in order to look for specific keywords such that articles that pertained to our topic would be collected over the course of a few days. 

## Our Challenges
The News API served as fantastic access to news articles from a wide variety of news and media sources, but that impact was limited due to the restrictions on API calls. We were able to access just 100 articles at a time and, with the intent to access the most recent articles, were not able to collect nearly as many as we had intended to. Working with the Global Terrorism Database produced its own challenges, with it being such a large collection of data to manage. DuckDB acted as a very useful tool for processing and holding this data. 

## Analysis

GTD + NewsAPI synthesis: Our analysis highlights a clear contrast between long-term global terrorism patterns (GTD) and real-time media coverage (NewsAPI). The GTD dataset shows that terrorism has been historically concentrated in the Middle East, North Africa, and South Asia- events like bombing/explosion dominating both civilian and military targets. We thought it was interesting to see that there was a sharp peak between 2010–2015, driven primarily by highly lethal groups such as ISIL, the Taliban, and Boko Haram. 

![image](./visualisations/global_heatmap.png)

![image](./visualisations/fatalities_over_time.png)

Upon observing the data, it appears clear that instances and fatalities have increased reasonably consistently since 1970. This cumulated in a peak in terrorist activity in the 2010s, with over 40,000 fatalities connected to terrorism in the middle of the decade. This increase was largely fueled by a much greater number of bombings between 2010 and 2020. Armed assaults, often using firearms, also saw a significant increase during this time that further explains the numbers of fatalities seen. 

![image](./visualisations/attack_type_trends_bubble.png)

In contrast, the NewsAPI stream illustrates short-term, media-driven narratives, with coverage focused heavily on domestic shootings, reflected in the information displayed regarding the recent shooting of National Guard members in Washington, DC. While GTD captures the broad, long-term escalation and decline of terrorism worldwide, NewsAPI captures how the public hears about violence - often emphasizing immediacy, proximity, and sensational events. Together, the datasets show a strong mismatch between global terrorism reality and real-time media attention, highlighting how public perception can diverge from long-term trends.

![image](./visualisations/title_wordcloud.png)

![image](./visualisations/news_sources.png)

https://teaganabritten-dataproject3-gtd-dashboard-vbrkcv.streamlit.app/