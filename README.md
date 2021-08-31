# Telco_Churn_Project
A project determining drivers of churn amoung customers.
Classification Project

Project Summary

**Project Objectives**
Document code, process (data acquistion, preparation, exploratory data analysis and statistical testing, modeling, and model evaluation), findings, and key takeaways in a Jupyter Notebook report.
Create modules (acquire.py, prepare.py) that make your process repeateable.
Construct a model to predict customer churn using classification techniques.
Deliver a 5 minute presentation consisting of a high-level notebook walkthrough using your Jupyter Notebook from above; your presentation should be appropriate for your target audience.
Answer panel questions about your code, process, findings and key takeaways, and model.

**Business Goals**
Find drivers for churn at Telco. Why are customers churning?
Construct a ML classificiation model that accurately predicts churn for each customer.
Document the process well enough to be presented or read like a report.

**Audience**
The Codeup Data Science Team.

Project Deliverables

A Jupyter Notebook Report
A README.md
A CSV file 
A .py file for aquiring and preparing the data.
A notebook presentation

Project Context
The dataset I am using comes from the Codeup database.

Data Dictionary

senior_citizen: Indicates if customer is a senior citizen                        (int)
tenure: Months customer has subscribed to service                                (int)
monthly_charges:  Dollar cost per month                                          (float)
total_charges:  Dollar cost accumulated during tenure                            (float)
internet_extras: Indicates if customer pays for internet add-ons                 (int)
streaming_entertainmen: Indicates if customer has streaming movies or tv         (int)
family:  Indicates if customer has dependents or partner                         (int)
gender_Male: Indicates if customer identifies as male                            (int)
phone_service_Yes: Indicates if customer has at least 1 phone line               (int)
paperless_billing_Yes: Indicates if customer uses paperless billing              (int)
churn_Yes: Indicates if customer has left the company                            (int)
contract_type_Month-to-month: Indicates if customer pays on a monthly basis      (int)
contract_type_One_year: Indicates if customer pays annually                      (int)
contract_type_Two_year: Indicates if customer pays bi-annually                   (int)
internet_service_type_DSL: Indicates if customer has DSL internet                (int)
internet_service_type_Fiber_optic: Indicates if customer has fiber optic internet(int)
internet_service_type_None: Indicates if customer does not have internet         (int)
payment_type_Bank_transfer: Indicates if customer pays using a bank account      (int)
payment_type_Credit_card: Indicates if customer pays using a credit card         (int)
payment_type_Electronic_check: Indicates if customer pays using e-check          (int)
payment_type_Mailed_check: Indicates if customer pays using paper check          (int)


Initial Hypotheses
Hypothesis 1 - Electronic check payment type has a higher rate of churn than the rest.
alpha = .05
$H_0$: Payment type is independent of churn.
$H_a$: Churn is dependent on payment type.
Outcome: I rejected the Null Hypothesis; there is a difference in ...
Hypothesis 2 - A larger monthly bill drives churn.
alpha = .05
$H_0$: Churn is independent of monthly_charges amount.
$H_a$: Churn is dependent on monthly_charges amount.
Outcome: I rejected the Null Hypothesis; there is a difference in ...
Hypothesis 3 - Churn is dependent on tenure.
alpha = .05
$H_0$: Those with a higher tenure are just as likely to churn as those with a lower tenure.
$H_a$: Those with a higher tenure are less likely to churn than those with a lower tenure
Outcome: I rejected the Null Hypothesis; there is a difference in ...
Hypothesis 4 Internet service type effects churn rate
alpha = .05
$H_0$: Internet service type is independent of churn.
$H_a$: Churn is dependent on internet service type.
Outcome: I rejected the Null Hypothesis; there is a difference in ...
Hypothesis 5 Senior citizens churn at a higher rate than other customers
alpha = .05
$H_0$: Being a senior citizen is independent of churn.
$H_a$: Churn is dependent on whether or not a customer is a senior citizen.
Outcome: I rejected the Null Hypothesis; there is a difference in ...


Executive Summary - Conclusions & Next Steps
I found that all of the classification models I created, LogisticRegression, DecisionTree, RandomForest, and KNeighbors predicted the species of Iris equally well using the features sepal_width, sepal_length, petal_length, petal_width.
I chose my DecisionTree model as my best model with a 90% accuracy rate for predicting my target value, species. This model outperformed my baseline score of 33% accuracy, so it has value.
Some initial exploration and statistical testing revealed that engineering some new features like petal area or sepal area might help my models predict with even more accuracy, and with more time, I would like to test this hypothesis.

Pipeline Stages Breakdown

Plan
Create README.md with data dictionary, project and business goals, come up with initial hypotheses.
Acquire data from the Codeup Database and create a function to automate this process. Save the function in an acquire.py file to import into the Final Report Notebook.
Clean and prepare data for the first iteration through the pipeline, MVP preparation. Create a function to automate the process, store the function in a prepare.py module, and prepare data in Final Report Notebook by importing and using the funtion.
Clearly define three hypotheses, set an alpha, run the statistical tests needed, reject or fail to reject the Null Hypothesis, and document findings and takeaways.
Establish a baseline accuracy and document well.
Train three different classification models.
Evaluate models on train and validate datasets.
Choose the model with that performs the best and evaluate that single model on the test dataset.
Create csv file with the customer id, the probability of the target values, and the model's prediction for each observation in my test dataset.
Document conclusions, takeaways, and next steps in the Final Report Notebook.
 
Plan -> Acquire
Store functions that are needed to acquire data from the customers, contract_type, internet_service_types and payment_types tables from the telco database on the Codeup data science database server; make sure the acquire.py module contains the necessary imports to run my code.
The final function will return a pandas DataFrame.
Import the acquire function from the acquire.py module and use it to acquire the data in the Final Report Notebook.
Plot distributions of individual variables.



Plan -> Acquire -> Prepare

Plan -> Acquire -> Prepare -> Explore


Plan -> Acquire -> Prepare -> Explore -> Model


Plan -> Acquire -> Prepare -> Explore -> Model -> Deliver


