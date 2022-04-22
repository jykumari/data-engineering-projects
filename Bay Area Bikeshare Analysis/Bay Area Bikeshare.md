
#### Problem Statement

- Imagine that you are a data scientist at Lyft Bay Wheels (https://www.lyft.com/bikes/bay-wheels), formerly known as Ford GoBike, the company running Bay Area Bikeshare. You are trying to increase ridership, and you want to offer deals through the mobile app to do so.

- What deals do you offer though? Currently, your company has several options which can change over time.  Please visit the website to see the current offers and other marketing information. Frequent offers include:
  * Single Ride
  * Monthly Membership
  * Annual Membership
  * Bike Share for All
  * Access Pass
  * Corporate Membership
  * etc.

- Through this project, you will answer these questions:

  * What are the 5 most popular trips that you would call "commuter trips"?

  * What are your recommendations for offers (justify based on your findings)?

#### Implementation

For this project, below static tables have been used from the
the dataset **san_francisco** :

  * bikeshare_stations

  * bikeshare_status

  * bikeshare_trips


**1) Please refer to "Queries.md"**

This markdown file includes:
1) Some initial queries
2) Some more Questions in order to make recommendations

*All the queries have been run using the Google BigQuery GUI interface in the GCP or using BQ from the Linux command line.*


**2) Project_1.ipynb**

This notebook includes answer to following 2 project questions:

  * What are the 5 most popular trips that you would call "commuter trips"?

  * What are your recommendations for offers (justify based on your findings)?


Code cells have been used to run SQL commands using the "bang" command to shell out, and to load into Pandas, using the !bq

Code cells have been used to create Pandas formatted output tables, to present and support my findings

Code cells have been used to create simple data visualizations using Matplotlib to present and support my findings
