# Employee Attrition - Case Study (ML Engineer)

## Business Problem
Attrition is a problem that impacts all businesses and it leads to significant costs for a business, including the cost of business disruption, hiring new staff and training new staff. 

Therefore, businesses, in particular their HR departments have great interest in understanding the drivers of, and minimizing staff attrition. The use of classification models to predict if an employee is likely to quit could greatly increase HR's ability to intervene on time and remedy the situation to prevent attrition.

## Instructions

You are asked to put a model in production for the HR department. For the purpose of this exercise, you will need to create a git respository in which you should complete the tasks below.

1. Create a basic ML model using the dataset provided. **This is not the focus of the assignment and serves only to complete the task below**

1. Prepare your model for deployment, implement an ML inferencing pipeline and deploy a REST endpoint that consumes the trained ML model using the technology of your choice. If possible also including aspects of model performance monitoring.

Please focus on the ML lifecycle of a project (training, prediction/inference and validation). Data science processes such as EDA, feature engineering or model optimisation are **not** the focus of this case study. 

Imagine that your work is part of a multi-person project and structure your git repository accordingly.

### Notes on Instructions

1. Python is our main language of work and must be used for this assignment. 

1. Coding style and code modularization are important aspects that will be evaluated for this task.

1. You do not have to make any slides. We recommend that you present your solution "demo style", i.e. showcasing live functionality while sharing your screen.

1. You should not spend more than 8 hours on this project. We encourage you to keep the solution simple. The purpose of the case study is to showcase code quality and deployment. Anything missing from your solution due to time, can be discussed in the demo.

    1. There are (open source) platforms for managing the end-to-end machine learning lifecycle. Feel free to use one that you feel most comfortable with.
    
    1. (Optional) If you want a challenge and want to go a step further, consider model management/versioning capabilities.

1. All materials should be prepared in English.

1. Please share the link to your git respository with us before the interview. This allows us to review the code further if we do not have time during the interview. If you have any questions about this, do not hesitate to reach out.

## Dataset
The main data source is the `employee-attrition.csv` file that contains 1470 HR entries.  Given the limited size of the data set, the model should only be expected to provide modest improvement in identification of attrition vs a random allocation of probability of attrition.


| Name | Description |
|------|-------------|
|AGE| Numerical Value |
|ATTRITION|Employee leaving the company (0=no, 1=yes) |
|BUSINESS TRAVEL|(1=No Travel, 2=Travel Frequently, 3=Tavel Rarely)|
|DAILY RATE|Numerical Value - Salary Level|
|DEPARTMENT|(1=HR, 2=R&D, 3=Sales)|
|DISTANCE FROM HOME|Numerical Value - THE DISTANCE FROM WORK TO HOME|
|EDUCATION|Numerical Value|
|EDUCATION FIELD|(1=HR, 2=LIFE SCIENCES, 3=MARKETING, 4=MEDICAL SCIENCES, 5=OTHERS, 6= TEHCNICAL)|
|EMPLOYEE COUNT|Numerical Value|
|EMPLOYEE NUMBER|Numerical Value - EMPLOYEE ID|
|ENVIROMENT SATISFACTION|Numerical Value - SATISFACTION WITH THE ENVIROMENT
|GENDER|(1=FEMALE, 2=MALE)
|HOURLY RATE|Numerical Value - HOURLY SALARY
|JOB INVOLVEMENT|Numerical Value - JOB INVOLVEMENT
|JOB LEVEL|Numerical Value - LEVEL OF JOB
|JOB ROLE|(1=HC REP, 2=HR, 3=LAB TECHNICIAN, 4=MANAGER, 5= MANAGING DIRECTOR, 6= REASEARCH DIRECTOR, 7= RESEARCH |SCIENTIST, 8=SALES EXECUTIEVE, 9= SALES REPRESENTATIVE)|
JOB SATISFACTION|Numerical Value - SATISFACTION WITH THE JOB|
MARITAL STATUS|(1=DIVORCED, 2=MARRIED, 3=SINGLE)|
MONTHLY INCOME|Numerical Value - MONTHLY SALARY|
|MONTHY RATE|Numerical Value - MONTHY RATE|
|NUMCOMPANIES WORKED|Numerical Value - NO. OF COMPANIES WORKED AT|
|OVER 18|(1=YES, 2=NO)|
|OVERTIME|(1=NO, 2=YES)|
|PERCENT SALARY HIKE|Numerical Value - PERCENTAGE INCREASE IN SALARY|
|PERFORMANCE RATING|Numerical Value - ERFORMANCE RATING|
|RELATIONS SATISFACTION|Numerical Value - RELATIONS SATISFACTION|
|STANDARD HOURS|Numerical Value - STANDARD HOURS|
|STOCK OPTIONS LEVEL|Numerical Value - STOCK OPTIONS|
|TOTAL WORKING YEARS|Numerical Value - TOTAL YEARS WORKED|
|TRAINING TIMES LAST YEAR|Numerical Value - HOURS SPENT TRAINING|
|WORK LIFE BALANCE|Numerical Value - TIME SPENT BEWTWEEN WORK AND OUTSIDE|
|YEARS AT COMPANY|Numerical Value - TOTAL NUMBER OF YEARS AT THE COMPNAY|
|YEARS IN CURRENT ROLE|Numerical Value -YEARS IN CURRENT ROLE|
|YEARS SINCE LAST PROMOTION|Numerical Value - LAST PROMOTION|
|YEARS WITH CURRENT MANAGER|Numerical Value - YEARS SPENT WITH CURRENT MANAGER|
