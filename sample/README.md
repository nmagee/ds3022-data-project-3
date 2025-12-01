# Sentiment Analysis on Tech Moguls and their Companies on Bluesky

## Team members
Iliana Vasslides and Claire Bassett 


## Data Source

*What data source did you work with?*
We continued to work with the BlueSky firehose for our data source. 


## Challenges / Obstacles

*What challenges did this data choice present in data gathering, processing and analysis, and how did you work through them? What methods and tools did you use to work with this data?* 


Using the Bluesky Firehose API was actually our third choice in sourcing data. The two previous APIs(GDELT News and Alien Vault OTX - Pulse Stream) retrieved data on breaking news and cyber threats. But both APIs could not handle the amount of requests that were needed for the project. Once sourcing our API and confirming its capacity, we struggled in the data processing step by determining what columns, and thus information from each message/post, we wanted to keep and use for our analysis. Besides simply choosing what information we wanted, it took us a couple tries to figure out the pattern of the nested tree to appropiately extract specific data labels. Additionally, the first time we ran our Kafka Consumer it was estimated to take over 50 hours. This was not an appropriate amount of time to ensure we had ample time to complete the cleaning and analysis. We solved this issue by removing time.sleep() from inside the consumer try block, and only having it present if there was an error consuming a record. After removing that line of code, we were able to process over 1,000 records ever 10 seconds, which was both more managable and effective for the task.

During data analysis, a challenge we struggled with was deciding how to use a sentiment analysis on our data when it was in multiple languages, not just English. We used the package langdetect to help us with this process. Using this packages, we only kept the rows that were in English to make our sentiment analysis easier. 

To perform our sentiment analysis, we used Hugging Faces transformers feature using pipeline and specifying sentiment-analysis. This package streamlined the process of evaluating messages. It was challenging to understand how the process worked, because we wanted to fully understand the power of what we were applying. We dove in to documentation and used online explanations of how the algorithm tokenized values, passed the data through transformers, completed classification, and outputed the sentiment. Overall, the package made it extremely easy to analyze the data and visualize our message. Additionally, it was challenging to ensure that we had the proper format to create the query and map the text to keywords related to each mogul and their company.



## Analysis

*Offer a brief analysis of the data with your findings. Keep it to one brief, clear, and meaningful paragraph.*

For our analysis, we compared sentiment analysis on the top 5 tech moguls compared to their respective companies. We then created two bar graphs to show the number of posts that showed each sentiment for the different tech moguls and their companies. It was unsurprising that overall the companies were mentioned in a higher number of posts than almost all of the moguls. Additionally, it was unsurprising that Elon Musk was the most mentioned tech mogul, with a much higher negative sentiment than the others given some previous and current happenings in the news and the US. On the other hand, the company Google was mentioned comparably more then some of the other companies, but the CEO had zero mentions, meaning that he is not as highly mentioned or even known in the public view of technology. The most surprising finding was that for each mogul and company alike, there was more negative sentiments than positive. We originally thought that only a few moguls or companies would have this large of a difference between the number of posts showing each sentiment, but few showed an equal sentiment of each mogul or company. This could possibly hint that BlueSky users have strong negative feelings towards technology and other monopolistic companies. Given the overall negative feelings towards these people and companies, users who post on BlueSky are more likely to post negative thoughts about technology than positive ones. 


## Plot / Visualization

*Include at least one compelling plot or visualization of your work. Add images in your subdirectory and then display them using markdown in your README.md file.*

This first graph shows the number of posts per sentiment for each of the six tech moguls we chose to analyze. 

<img src="mogul_sentiments.jpg" width="400">

This second graph shows the number of posts per sentiment for each of the tech moguls' respective companies, or one of their most well-known companies.

<img src="company_sentiments.jpg" width="400"> 


## GitHub Repository

Github Repo: https://github.com/clairembassett/bluesky-tech-sentiment/tree/main 
