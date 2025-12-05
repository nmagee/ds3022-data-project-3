# Team Corinne

## Team members
Corinne Fogarty


## Data Source

What data source did you work with?
The NBA API

## Challenges / Obstacles

What challenges did this data choice present in data gathering, processing and analysis, and how did you work through them? What methods and tools did you use to work with this data?

Working with this API, I had to familiarize myself with how the data was set up and excatly what I wanted to look at. This look a lot of googling, looking at others work, and using some Large Language models as a launching point to get started with the data. The NBA API was also pretty unstable. I had to work around timeout issues when getting data, by including try and excepts for timeout errors. Also, the NBA API requires strong headers because it expects browser traffic not scripts, so I had to use headers that would match chrome traffic. To work through this, I added a dictionary of the strong headers necessary for this to work. To work with this data I used prefect to ingest it and duckdb to store and perform transformations on it. Python was used for visualizations, specifically matplotlib and seaborn. 

## Analysis

Offer a brief analysis of the data with your findings. Keep it to one brief, clear, and meaningful paragraph.

My plots are showing me that on average, the amount of rest days a team has does not significantly impact the point they score in a game or their win rate. The points scored stays consistent at just over 100 and the win rate stays steady between 0.4 and 0.6. However, the plot comparing rest days to average plus minus shows a different trend. Average plus minus is at -0.9 with 1 rest day yet improves to around 0.2 with 3 or 4 rest days. The negative plus-minus stat means that after one rest day, teams are usually outscored by their opponent, but with more rest days, they are outscoring the opponent. This suggests that more than one rest day is most beneficial to teams as it is more likely they will outscore opponents and therefore win the game. This plot showed a drop off after 5 rest days which could also suggest too much time without a game negtauvely effects teams, maybe because a loss of momentum or the feeling of being in a high-stakes scenario.


## Plot / Visualization

Include at least one compelling plot or visualization of your work. Add images in your subdirectory and then display them using markdown in your README.md file.

![Rest Days Vs. Plus-Minus](rest_vs_plus_minus.png)

## GitHub Repository

https://github.com/corinnefog/ds3022-project3/tree/main
