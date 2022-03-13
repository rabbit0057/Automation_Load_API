# Locust Automation Project

Locust with Python. 

The collection of tests contains:
- List breeds
- List by breed, using a random breed from the earlier listing result
- Random image


## Getting Started

just download the project or clone repository. You need to install packages using pip according to requirements.txt file.
Run the command below in terminal:

```
$ pip install -r requirements.txt
```

## Installation

Install python 3 and pip3 in your machine, all the steps are available in this [link](https://docs.locust.io/en/stable/installation.html)

For MacOS 
```
brew install locust
```

## To Run

To run in a single mode,
```
locust -f locust_load_test.py
```
then go to `http://localhost:8089/` and then enter the number of users and the rampup time to get started


To run in headless, generate html report and logfile,
```
locust -f locust_load_test.py -u 1 -r 1 -t 10s --headless --print-stats --host=https://dog.ceo/api -L DEBUG --logfile demo_report.log --html Report.html
```

Report.html 

<img width="1041" alt="Screenshot 2022-03-14 at 2 09 07 AM" src="https://user-images.githubusercontent.com/5949627/158078372-b722ecc9-0983-4de7-af1e-c1d8fc9c47f4.png">


<img width="1062" alt="Screenshot 2022-03-14 at 2 09 15 AM" src="https://user-images.githubusercontent.com/5949627/158078379-b9e4bcf0-0d1d-4188-a1fa-0a5ee8db4eea.png">



<img width="541" alt="Screenshot 2022-03-14 at 2 10 04 AM" src="https://user-images.githubusercontent.com/5949627/158078380-29b07ba8-440d-4141-a886-1865d87e07d6.png">
