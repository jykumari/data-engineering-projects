
# Project 2: Tracking User Activity

A tech firm has an existing service that delivers assessments, and now lots of different customers want to publish their assessments on it. The purpose of this project is to get ready for data scientists who work for these customers to run queries on the data.

# Tasks as a data engineer

Prepare the infrastructure to land the data in the form and structure it needs
to be to be queried.

Requirements:

- Publish and consume messages with Kafka
- Use Spark to transform the messages.
- Use Spark to transform the messages so that we can land them in HDFS

# This markdown file includes:

#### 1) History file

```
a) History from Spark run : spark_history_jkumari.txt

b) History of console : jkumari-history.txt
```

#### 2) Docker file:

- Please refer to <docker-compose.yml> in the current directory.


#### 3)  A report in form of ipynb file :

```
<Project_2_report.ipynb>
```

The report describes the pipeline and steps for:

- Setup
- Publish and consume messages with Kafka
- Spark to transform the messages that includes steps for unrolling nested json file, creating forced Schema
- Writing to HDFS
- Exit spark and get history
- Docker-compose down


Above steps also includes description of my assumptions, and explanation on different parts of the
pipeline

#### a) Few points about data itself:

- The given data is about the assessments of different exams. Each element in the data includes fields such as exam_name, questions, details of assessments such as total questions, correct and incorrect questions etc. Also, the questions field has user completion status, user's selection of response out of the available options for the questions.


#### b) Issues with the data and how I resolved it.

- The given data is a nested structure and hence used techniques such as json load, unrolling json and finally creating forced schema to extract data from nested structure in order to run required queries and derive meaningful insights. Using Forced schema helped to enforce the required structure of data and pull fields from nested json, that were needed for querying.
