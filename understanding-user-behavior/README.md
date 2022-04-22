
# Project 3: Understanding User Behavior

### Business Context:
The Business team at a Game development company has come up with a game idea and requires support from the data science and data engineering team to build the pipeline for generating game events and tracking those events. The goal is to target interested users with a more minimal version and plan to launch the next version of game with enhanced features.  

---
## Table of contents

- [Pipeline Creation and Data Analysis](#pipeline-creation-and-data-analysis)
- [Game API](#game-api)
- [Docker Compose](#docker-compose)
- [Streaming Data and Schema Creation](#streaming-simulation-and-schema-creation)

---

## Pipeline Creation and Data Analysis
All of the instructions for creating the pipeline, as well as some initial data analysis, can be found [here](Project_3_report.ipynb).

[(Back to top)](#table-of-contents)

## Game API
The API for our game can be found [here](game_api.py).

[(Back to top)](#table-of-contents)

## Docker Compose
The Docker Compose file used to build the containers used in the pipeline is [here](docker-compose.yml).

[(Back to top)](#table-of-contents)

## Streaming Data and Schema Creation
The Python script used to generate streaming data is [here](stream-events_script.py) and the script to write events and force the schemas is [here](write_events_stream.py).

[(Back to top)](#table-of-contents)

## Tasks executed in the project

- log events to Kafka

- Assembled a data pipeline to catch these events: used Spark streaming to filter
  select event types from Kafka, landed them into HDFS/parquet to make them
  available for analysis using Presto.

- Apache Bench used to generate test data for your pipeline.

- Produced an analytics report providing a description of pipeline
  and some basic analysis of the events. 
