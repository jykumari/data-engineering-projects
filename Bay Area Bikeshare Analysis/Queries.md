
### 1) Some Initial Queries

*Run queries using bq command line tool*

**1.a) What's the size of this dataset? (i.e., how many trips)**

*Query:*

```sql
bq query --use_legacy_sql=false '
    SELECT count(*) as dataset_size
    FROM
       `bigquery-public-data.san_francisco.bikeshare_trips`'
```

*Result:*
```sql
+--------------+
| dataset_size |
+--------------+
|       983648 |
+--------------+
```
----------------------

**1.b) What is the earliest start date and time and latest end date and time for a trip?**

*Query:*

```sql
bq query --use_legacy_sql=false '
    SELECT min(start_date) as earliest_start_date_time, max(end_date) as latest_end_date_time
    FROM `bigquery-public-data.san_francisco.bikeshare_trips`'
```

*Result:*

```sql
------------------------------------------------
| earliest_start_date_time | latest_end_date_time |
------------------------------------------------
|      2013-08-29 09:08:00 |  2016-08-31 23:48:00 |
------------------------------------------------
```
----------------------

**1.c) How many bikes are there?**

*Query:*

```sql
bq query --use_legacy_sql=false '
    SELECT  count(distinct(bike_number)) as number_of_bikes
    FROM `bigquery-public-data.san_francisco.bikeshare_trips`'
```

*Result:*
```sql
+-----------------+
| number_of_bikes |
+-----------------+
|             700 |
+-----------------+
```
----------------------

**1.d) How many trips are in the morning vs in the afternoon?**

*Query:*

* morning trip (Assumption - All Trips between 6am - 11:59:59am)

```sql
bq query --use_legacy_sql=false '
    SELECT count(trip_id) as number_of_morning_trips
    FROM `bigquery-public-data.san_francisco.bikeshare_trips` where  EXTRACT(time FROM start_date) >= "06:00:00" and EXTRACT(time FROM end_date) < "12:00:00"'
```
*Result:*

```sql
+-------------------------+
| number_of_morning_trips |
+-------------------------+
|                  387758 |
+-------------------------+
```

Afternoon trip (Assumption - All Trips between 12pm - 17:59:59pm)

```sql
bq query --use_legacy_sql=false '
    select count(trip_id) as number_of_afternoon_trips
    FROM `bigquery-public-data.san_francisco.bikeshare_trips`
    where  EXTRACT(time FROM start_date) >= "12:00:00" and EXTRACT(time FROM end_date) < "18:00:00"'
```
*Result:*

```sql
+-------------------------+
| number_of_afternoon_trips |
+-------------------------+
|                  368289 |
+-------------------------+
```

**1.e) What was the longest trip time in seconds made between two given stations? (Here the stations are San Mateo County Center' and Mezes)**

*Query:*

```sql
select max(duration_sec) from `bigquery-public-data.san_francisco.bikeshare_trips` where start_station_name = 'San Mateo County Center' and end_station_name = 'Mezes'
```
**Result:** 1334 seconds

--------------

**1.f) How many subscriber and customer trips are there?**

*Query:*

```sql
SELECT count(trip_id) as rider_trips,
CASE
    WHEN subscriber_type = "Subscriber" THEN 'total number of subscriber trips'
    WHEN  subscriber_type = "Customer" THEN 'total number of customer trips'
    ELSE 'no result'
END
FROM `bigquery-public-data.san_francisco.bikeshare_trips`
group by subscriber_type
```

*Result:*

Total number of customer trips: 136809

Total number of subscriber trips: 846839

-----------------------------------------

**1.g) What is the average duration of all the trips?**

*Query:*

```sql
SELECT
  ROUND(avg(duration_sec/60), 1) AS total_duration_min
FROM
  `bigquery-public-data.san_francisco_bikeshare.bikeshare_trips`
WHERE
  EXTRACT(DATE
  FROM
    start_date)=EXTRACT(DATE
  FROM
    end_date)
ORDER BY
  total_duration_min
LIMIT
  10
```

*Result:*

total_duration_min: 14.6 min

---------------------------------------------------------

### 2) Some more Questions in order to make recommendations:

**Q1: What are the peak months for bike trips?**

*Query:*


```sql
bq query --use_legacy_sql=false '
SELECT
  EXTRACT(Month
  FROM
    start_date) AS Month,
  COUNT(trip_id) AS monthly_trips from `bigquery-public-data.san_francisco.bikeshare_trips`
  group by Month
  order by monthly_trips desc'
```
*Result:*

```sql
+-------+---------------+
| Month | monthly_trips |
+-------+---------------+
|     8 |         95576 |
|    10 |         94378 |
|     6 |         91672 |
|     7 |         89539 |
|     9 |         87321 |
|     5 |         86364 |
|     4 |         84196 |
|     3 |         81777 |
|    11 |         73091 |
|     1 |         71788 |
|     2 |         69985 |
|    12 |         57961 |
+-------+---------------+
```

**Q2: What's the peak time of day for bike riding**

*Query:*

```sql
bq query --use_legacy_sql=false '
SELECT
  EXTRACT(hour
  FROM
    end_date) AS hour, count(trip_id) as trips
  from `bigquery-public-data.san_francisco.bikeshare_trips`
group by hour
order by trips desc'
```
*Result:*

```sql
+------+--------+
| hour | trips  |
+------+--------+
|   17 | 129072 |
|    8 | 123941 |
|    9 | 108459 |
|   18 |  96317 |
|   16 |  81238 |
|    7 |  56198 |
|   19 |  47273 |
|   10 |  44897 |
|   12 |  44867 |
|   13 |  43805 |
|   15 |  43264 |
|   14 |  37531 |
|   11 |  36959 |
|   20 |  25371 |
|    6 |  17274 |
|   21 |  16571 |
|   22 |  11369 |
|   23 |   6826 |
|    5 |   4303 |
|    0 |   3450 |
|    1 |   1681 |
|    4 |   1329 |
|    2 |   1046 |
|    3 |    607 |
+------+--------+
```

**Q3: How is the trip trend by month between the most popular stations over the years ?**

*Query:*

```sql
bq query --use_legacy_sql=false '
SELECT
  EXTRACT(year
  FROM
    start_date) AS year, EXTRACT(month
  FROM
    start_date) AS month, count(trip_id) as trip
  from `bigquery-public-data.san_francisco.bikeshare_trips`
  where start_station_name = "Harry Bridges Plaza (Ferry Building)" and end_station_name = "Embarcadero at Sansome"
group by year, month
order by month desc'
```

*Result:*

```SQL
+------+-------+------+
| year | month | trip |
+------+-------+------+
| 2013 |    12 |  164 |
| 2015 |    12 |  147 |
| 2014 |    12 |  194 |
| 2015 |    11 |  195 |
| 2013 |    11 |  171 |
| 2014 |    11 |   37 |
| 2014 |    10 |  215 |
| 2013 |    10 |  279 |
| 2015 |    10 |  242 |
| 2015 |     9 |  276 |
| 2014 |     9 |  306 |
| 2013 |     9 |  300 |
| 2016 |     8 |  353 |
| 2014 |     8 |  373 |
| 2015 |     8 |  298 |
| 2013 |     8 |   31 |
| 2014 |     7 |  319 |
| 2016 |     7 |  237 |
| 2015 |     7 |  351 |
| 2015 |     6 |  304 |
| 2014 |     6 |  291 |
| 2016 |     6 |  273 |
| 2016 |     5 |  334 |
| 2014 |     5 |  276 |
| 2015 |     5 |  341 |
| 2015 |     4 |  275 |
| 2016 |     4 |  248 |
| 2014 |     4 |  211 |
| 2015 |     3 |  319 |
| 2016 |     3 |  258 |
| 2014 |     3 |  219 |
| 2016 |     2 |  226 |
| 2015 |     2 |  222 |
| 2014 |     2 |  169 |
| 2015 |     1 |  283 |
| 2014 |     1 |  216 |
| 2016 |     1 |  197 |
+------+-------+------+
```
**Q4: What is the trip time for most of the rides. Show top 5 trip durations**

*Query:*

```sql
bq query --use_legacy_sql=false '
SELECT
  count(trip_id) as number_of_rides,
  round((duration_sec/60), 1) AS total_duration_min
FROM
  `bigquery-public-data.san_francisco_bikeshare.bikeshare_trips`
GROUP BY
  duration_sec
ORDER BY number_of_rides desc
limit 5'
```

*Result:*

```SQL
---------------------------------------
| number_of_rides | total_duration_min |
---------------------------------------
|            2880 |                6.0 |
|            2852 |                6.3 |
|            2841 |                6.5 |
|            2822 |                6.0 |
|            2819 |                6.4 |
---------------------------------------
```

**Q5: Average duration of ride for subscriber vs customer**

*Query:*

```SQL
bq query --use_legacy_sql=false '
SELECT
  subscriber_type,
  ROUND(avg(duration_sec/60), 1) AS total_duration_min
FROM
  `bigquery-public-data.san_francisco_bikeshare.bikeshare_trips`
GROUP BY
  subscriber_type
ORDER BY
  total_duration_min DESC'
```
*Result:*

```SQL
+-----------------+--------------------+
| subscriber_type | total_duration_min |
+-----------------+--------------------+
| Customer        |               50.0 |
| Subscriber      |               10.5 |
+-----------------+--------------------+
```
