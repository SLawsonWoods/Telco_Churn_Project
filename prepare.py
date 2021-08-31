import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer

### Function from Curriclulm

def train_validate_test_split(df, target, seed=123):
    '''
    This function takes in a dataframe, the name of the target variable
    (for stratification purposes), and an integer for a setting a seed
    and splits the data into train, validate and test. 
    Test is 20% of the original dataset, validate is .30*.80= 24% of the 
    original dataset, and train is .70*.80= 56% of the original dataset. 
    The function returns, in this order, train, validate and test dataframes. 
    '''
    train_validate, test = train_test_split(df, test_size=0.2, 
                                            random_state=seed, 
                                            stratify=df[target])
    train, validate = train_test_split(train_validate, test_size=0.3, 
                                       random_state=seed,
                                       stratify=train_validate[target])
    target= 'churn'
    return train, validate, test

###################### Prepare telco Data With Split ######################

def split_data(df):
    '''
    take in a DataFrame and return train, validate, and test DataFrames; stratify on churn.
    return train, validate, test DataFrames.
    '''
    
    # splits df into train_validate and test using train_test_split() stratifying on churn to get an even mix of churn and no         churn
    train_validate, test = train_test_split(df, test_size=.2, random_state=123, stratify=df.churn)
    
    # splits train_validate into train and validate using train_test_split() stratifying on churn to get an even mix of churn and     no churn
    train, validate = train_test_split(train_validate, 
                                       test_size=.3, 
                                       random_state=123, 
                                       stratify=train_validate.churn)
    return train, validate, test

######################### Prepare telco Data with my steps ######################

def prep_telco(df):
    '''
    This function take in the telco_churn data acquired by get_connection,
    Returns prepped df with target column turned to binary, columns dropped that were not needed, missing     values in total_charges handled by deleting those 11 rows, dropping duplicates, and changing             total_charges to numeric)
    '''
    
    # drop columns with id since I used those just to JOIN the data
    df.drop(columns=['payment_type_id','internet_service_type_id','contract_type_id'],inplace=True)

    
    # make target column binary
    df.churn.replace(to_replace=['yes','no'],value=[1,0], inplace=True)
    
    
    # drop customer_id since I have no use for it
    df.drop(columns=['customer_id'], inplace=True)
    
    
    #drop all additional services since I am not interested in exploring
    df.drop(columns=['online_security','online_backup','device_protection',
              'tech_support','streaming_tv','streaming_movies'],inplace=True)

    #find any missing values
    df.total_charges.value_counts()
    
    # count how many are missing
    df.total_charges.value_counts()
    
    # this will get rid of the rows with no value in the total_charges column
    df.drop(df[df['total_charges'].str.contains(" ")].index, inplace = True)

    # Drop duplicatesreassign and check the shape of my data.
    df = df.drop_duplicates()
    
    #pd.to_numeric(df[column])
    df['total_charges'] = pd.to_numeric(df['total_charges'])   
    
    
    df.replace(to_replace = {'churn': {'no': 0, 'yes': 1}}, inplace=True)
    
    
    #def prep_telco_modeling(df):
    '''
    This function take in the telco_churn data acquired by get_connection,
    Returns prepped df with target column turned to binary, columns dropped that were not needed, missing     values in total_charges handled by deleting those 11 rows, dropping duplicates, and changing             total_charges to numeric)
    '''
    
    # drop columns with id since I used those just to JOIN the data
    #df.drop(columns=['payment_type_id','internet_service_type_id','contract_type_id'],inplace=True)


    

    


