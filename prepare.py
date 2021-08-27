import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer



###################### Prepare telco Data With Split ######################

def split_data(df):
    '''
    take in a DataFrame and return train, validate, and test DataFrames; stratify on churn.
    return train, validate, test DataFrames.
    '''
    
    # splits df into train_validate and test using train_test_split() stratifying on churn to get an even mix of churn and no churn
    train_validate, test = train_test_split(df, test_size=.2, random_state=123, stratify=df.churn)
    
    # splits train_validate into train and validate using train_test_split() stratifying on churn to get an even mix of churn and no churn
    train, validate = train_test_split(train_validate, 
                                       test_size=.3, 
                                       random_state=123, 
                                       stratify=train_validate.churn)
    return train, validate, test



def prep_telco(df):
    '''
    This function take in the telco_churn data acquired by get_connection,
    Returns prepped df with (**embarked dummy vars,
    deck dropped, and the mean of age imputed for Null values.**)
    '''
    
    # drop columns with id since I used those just to JOIN the data
df.drop(columns=['payment_type_id','internet_service_type_id','contract_type_id'],inplace=True)

    
    # make target column binary
df.churn.replace(to_replace=['yes','no'],value=[1,0], inplace=True)
    
    
    # drop customer_id since I have no use for it
df.drop(columns=['customer_id'], inplace=True)
    
    
    #drop all additional services since I am not interested in exploring
df.drop(columns=['online_security','online_backup','device_protection','tech_support','streaming_tv','streaming_movies'],inplace=True)

    # check if there are any missing values 
    df.total_charges.str.contains('')
    
    # count how many are missing
df.total_charges.value_counts()
    
  # this will get rid of the rows with no value in the total_charges column
df.drop(df[df['total_charges'].str.contains(" ")].index, inplace = True)

    # split data into train, validate, test dfs
train, validate, test = split_data(df)

    return train, validate, test


