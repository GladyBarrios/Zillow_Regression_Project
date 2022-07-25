import pandas as pd
import env
import numpy as np
from wrangle import wrangle_zillow


def train_validate_test_split():
    '''
    This function performs split on telco data, stratify churn.
    Returns train, validate, and test dfs.
    '''
    train_validate, test = train_test_split(df, test_size=.3, 
                                        random_state=123, stratify=df.fips)
    train, validate = train_test_split(train_validate, test_size=.05, 
                                   random_state=123,  stratify=train_validate.fips)

    return train, validate, test