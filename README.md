# Analyzing Millions of NYC Parking Violations

**Problem Statement:**

Parking violations do not affect your driving record, however, they sometimes can lead to serious consequences such as expensive fines and your vehicles being “booted,” towed, or even impounded. The goal of this project is to conduct an analysis on a dataset containing millions of NYC parking violations since January 2016. 


**Dataset**

The Open Parking and Camera Violations dataset was initially loaded with all violations contained in the mainframe database as of May 2016. 

### Dataset API : https://data.cityofnewyork.us/resource/nc67-uf89.json


## Principles of Big Data Technologies: 
- Containerization 
- Terminal navigation
- Python scripting 
- Artifact deployment 
- AWS EC2 provisioning

**Project Phases**

This project will be broken into four phases:

- Phase 1: Python Scripting
- Phase 2: Loading into ElasticSearch
- Phase 3: Visualizing and Analysis on Kibana
- Phase 4: Deploying to EC2 Instance


## Phase 1: Python Scripting	

### File Structure

  ```console
  ├── Dockerfile
  ├── main.py
  ├── requirements.txt
  └── src
      └── bigdata1
          └── api.py
  ```
**Running in Local:**


1. Git clone the repository 

2. Build image from Dockerfile
```
$ docker build -t bigdata1:1.0 .
```
3. Run the following command line:
```
$ docker run -v ${pwd}:/app -e APP_KEY=${Your API Key} -it bigdata1:1.0 python -m main --page_size=1 --num_pages=2 --output=results.json
```

#### Key arguments:
 - APP_KEY: https://data.cityofnewyork.us/login

- --page_size: This command line argument will ask for how many records to request from the API per call.

- --num_pages: If this command line argument is not provided, the script will continue requesting data until the entirety of the content has been exhausted. If this argument is provided, continue querying for data num_pages times.

- --output: If this command line argument is not provided, the script will simply print results to stdout. If provided, the script will write the data to the file (in this case, results.json).


**Running on EC2:**

1. Run the following command line: 

```
$ sudo docker run -e APP_KEY=${YOUR API KEY} -v ${pwd}:/app/out -it jackjoeng/bigdata1:1.0 python -m main --page_size=1 --num_pages=2 --output=./out/results.json 
```

## Phase 2: Coming soon

### File Structure

```console
├── Dockerfile
├── main.py
├── requirements.txt
├── docker-compose.yml
└── src
└── bigdata1
└── opcvapi.py
└── elasticsearch.py
```
**Running in Local:**

1. Git clone the repository (Phase 2)

2. Build image from Dockerfile
```
$ docker build -t bigdata1:1.0 .
```
3. Start ElasticSearch and Kibana
```
$ docker-compose up -d
```
4. Run ElasticSearch and Kibana
```
$ docker-compose run -v ${PWD}:/app -e APP_TOKEN=${YOUR API KEY} pyth /bin/bash
```
5. Run the following command:
```
$ python -m main --page_size=100 --num_pages=100 --output=results.json
```
This will load citibike dock data into Elasticsearch at a cadence of once / 30s.

6. Querying elasticsearch via curl
```
curl http://localhost:9200/bigdata1/violations/_search?q=state:NY&size=1
```

Alternatively, in your web browser run 
```
http://localhost:9200/bigdata1/violations/_search?q=state:NY&size=1
```

![Line_Chart](/Phase_2/image/output.png)

7. Shutting off
```
docker-compose down
```

## Phase 3: Visualizing and Analysis on Kibana

#### Open Kibana in your web browser; http://localhost:5601 

#### Define a time field

![Time_Field](/Phase_3/image/issueDate.png)

### Visualizations:

1. Top 5 Most Frequent Violations
#### Pie Chart
![Pie_Chart](/Phase_3/image/pie.png)

2. Top 10 Plates Ranked by No. of Violations
#### Heatmap
![Heatmap](/Phase_3/image/heatmap.png)

3. No. of Summons Issued by Each Agency Per Year 
#### Bar Chart 1
![Bar_Chart1](/Phase_3/image/bar1.png)

4. Top 5 Counties with Highest Average Reduction Amount
#### Bar Chart 2
![Bar_Chart2](/Phase_3/image/bar2.png)

5. No. of Issued Summons Per Year
#### Line Chart
![Line_Chart](/Phase_3/image/line.png)

#### Dashboard:
![Dashboard](/Phase_3/image/line.png)

## Phase 4: Coming soon

***Jack Yang Copy Right 2020***
https://github.com/JackJoeng/NYC-Parking-Violations-Analysis
