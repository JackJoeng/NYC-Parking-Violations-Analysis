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

This project will be broken into three parts:

- Phase 1: Python Scripting
- Phase 2: Loading into ElasticSearch
- Phase 3: Visualizing and Analysis on Kibana
- Phase 4: Deploying to EC2 Instance


## Phase 1: Python Scripting	

### File Structure

  ```console
  .
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
$ docker run -v $(pwd):/app -e APP_KEY=${Your API Key} -it bigdata1:1.0 python -m main --page_size=1 --num_pages=2 --output=results.json
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
## Phase 3: Coming soon
## Phase 4: Coming soon

***Jack Yang Copy Right 2020***
https://github.com/JackJoeng/NYC-Parking-Violations-Analysis
