# coding: utf-8

from pandas import *
from datetime import datetime as dt

def koubei(parsed_date=False):
    kb = read_csv(
        'data/ijcai2016_koubei_train', header=None, names=['user_id', 'merchant_id', 'location_id', 'timestamp']
        #   , dtype=str
        #   , parse_dates=[3]
        #   , nrows=10
    )
    if parsed_date:
        train['timestamp'] = train.timestamp.map(lambda d: dt.strptime(d, '%Y%m%d'))
    return kb

def taobao(parsed_date=False):
    # read the taobao data.
    taobao = read_csv(
        'data/ijcai2016_taobao', header=None, names=['user_id', 'seller_id', 'item_id', 'category_id', 'action_id', 'timestamp']
        #   , dtype=str
        #   , parse_dates=[5]
        #   , nrows=10
    )
    if parsed_date:
        taobao['timestamp'] = taobao.timestamp.map(lambda d: dt.strptime(d, '%Y%m%d'))
    return taobao

def merchant(parse_location=False):
    # read the merchant's info
    merchant = read_csv(
        'data/ijcai2016_merchant_info'
        , header=None, names=['merchant_id', 'budget', 'locations']
    )
    if parse_location:
        merchant['locations'] = merchant.locations.str.split(':')
    return merchant

def pred():
    # read the test set to predict.
    pred = read_csv(
        'data/ijcai2016_koubei_test', header=None, names=['user_id', 'location_id']
    )
    return pred

