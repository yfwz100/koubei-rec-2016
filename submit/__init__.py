# coding: utf-8

'''
Helper module to load data set in submission format.

author Zhi <yfwz100@yeah.net>
'''

import pandas as pd
from numpy import hstack, int64


def load(dataset):
    ''' Load data files in submission format.

    :param dataset: the file to load.
    :return : the data frame.
    '''
    frame = pd.read_csv(dataset, header=None, names=['user_id', 'location_id', 'merchant_id'])
    frame = frame.groupby(['user_id', 'location_id']).merchant_id.apply(
        lambda d: pd.Series(hstack([[int(i) for i in s.split(':')] for s in d]), name='merchant_id', dtype=int64)
    ).reset_index()
    return frame[['user_id', 'location_id', 'merchant_id']]
