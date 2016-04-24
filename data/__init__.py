# coding: utf-8

import pandas as pd
from datetime import datetime as dt


# read the train log.
train = pd.read_csv(
    'data/ijcai2016_koubei_train'
    , header=None, names=['user_id', 'merchant_id', 'location_id', 'timestamp']
    , dtype=str
#   , parse_dates=[3]
#   , nrows=10
)
train['timestamp'] = train.timestamp.map(lambda d: dt.strptime(d, '%Y%m%d'))


# read the taobao data.
taobao = pd.read_csv(
    'data/ijcai2016_taobao'
    , header=None, names=['user_id', 'seller_id', 'item_id', 'category_id', 'action_id', 'timestamp']
    , dtype=str
#   , parse_dates=[5]
#   , nrows=10
)
taobao['timestamp'] = taobao.timestamp.map(lambda d: dt.strptime(d, '%Y%m%d'))


# read the merchant's info
merchant = pd.read_csv(
    'data/ijcai2016_merchant_info'
    , header=None, names=['merchant_id', 'budget', 'locations']
)
merchant['locations'] = merchant.locations.str.split(':')


# read the test set to predict.
pred = pd.read_csv(
    'data/ijcai2016_koubei_test'
    , header=None, names=['user_id', 'location_id']
)

