# Analyst Take-Home
Thanks for your interest in WeWork! As part of our company growth strategy and goal setting, we’ve been sourcing a lot of new data to improve our understanding of supply and demand drivers in different geographic markets. We’re doing this for markets and submarkets that we’re already in, as well as potential new markets.

One dataset we’ve been discussing recently is [Walk Score](https://www.walkscore.com/). We’re curious how walkability relates to different performance metrics of existing WeWork buildings, and also how it might be an indicator of a certain type of real estate market profile.

## 1. Market Data Enrichment
The `market_data.csv` file in this repo contains a sample of U.S. markets and associated real estate data. We’d like to enrich this dataset with city-level walk scores.

Walk scores for various US cities can be found in the `ws_data.json` file. Also contained in the data file are latitude and longitude coordinates for each city. 

Please take this data, transform it as necessary, and join it with the market real estate table so that that table now has three additional columns: walkscore, latitude, and longitude. Only markets for which those three values are available should be present in the new table.

If you really get stuck, you can copy the table found at the bottom of [this page](https://www.walkscore.com/cities-and-neighborhoods/), but you will need to find latitude and longitude values for each city, for part 2 below, somewhere else.

## 2. Geospatial Visualization
Plot the cities on a map, using a tool of your choice. Choose one dimension in the data (walk score, vacancy, etc.) to visualize, such that relative differences in the values can be gleaned from the map. 

## 3. Variable Relationships 
Plot the relationship between walk score and three real estate variables: inventory, vacancy, and asking rent (again using the tool of your choice). Discuss what patterns you see, if any, and briefly explain further steps you might take to explore this data.

## Deliverables

* Any code you used for the data munging steps, or a concise outline of the steps you took.
* An image of your map or a link to it if it's on the web.
* An image of your plots, along with your brief analysis and suggested further steps.

Text should be measured in paragraphs, not pages! Please don't hesitate to reach out to ian.stuart@wework.com with any questions. Thank you!
