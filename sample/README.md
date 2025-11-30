# Team Coco

## Team members
Iliana Vasslides and Claire Bassett 


## Data Source

*What data source did you work with?*
We continued to work with the BlueSky firehose for our data source. 


## Challenges / Obstacles

*What challenges did this data choice present in data gathering, processing and analysis, and how did you work through them? What methods and tools did you use to work with this data?* 
This data choice was actually our third choice of a source, because the two previous news APIs that we were trying to work with were not ending well. One main challenge we faced during data processing was determining what columns, aka information from each message/post, we wanted to keep and use for our analysis. Besides simply choosing what information we wanted, it took us a couple tries to figure out the pattern of the nested tree to appropiately extract specific data labels. Additionally, the first time we ran our Kafka Consumer it was taking over 10 hours and so we had to troubleshoot that in order to consume our data in an appropiate amount of time to be able to analysis as well. We solved this issue by removing time.sleep() from inside the consumer try block, and only having it present if there was an error consuming a record. After removing that line of code, we were able to process over 1,000 records ever 10 seconds, which was much more managable. 

During data analysis, a challenge we struggled with was deciding how to use a sentiment analysis on our data when it was in multiple languages, not just English. We used the package langdetect to help us with this process. Using this packages, we only kept the rows that were in English to make our sentiment analysis easier. 

To perform our sentiment analysis, we used pipline from transformers. This package made the process extremely easy and gave us nice summaries to then apply to our graphs. The only small challenges with this package was figuring out the proper format to make the text and how to map the keywords we pulled to each specific mogul and their company. 



## Analysis

*Offer a brief analysis of the data with your findings. Keep it to one brief, clear, and meaningful paragraph.*


## Plot / Visualization

*Include at least one compelling plot or visualization of your work. Add images in your subdirectory and then display them using markdown in your README.md file.*

## GitHub Repository

**ADD GITHUB REPO**
(have to make it public first)