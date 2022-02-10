# import pandas as pd
# from math import *

# ratings = pd.read_csv('ratings.csv', header= None)
# ratings.columns = ['userId', 'itemId', 'rank', 'timestamp']

# products = pd.read_csv('product.csv', header = None)
# product = products.iloc[:, :2]
# product.columns = ['itemId', 'title']

# data = pd.merge(ratings[['userId', 'itemId', 'rank']], product, on = 'itemId')

# # data = data[['userId', 'itemId', 'rank', 'title']].sort_values('userId')

# dic = {}
# for idx in range(len(data)):
#     tmp = data.iloc[idx]

#     if tmp[0] not in dic.keys():
#         dic[tmp[0]] = {tmp[3]:tmp[2]}
#     else:
#         dic[tmp[0]][tmp[3]] = tmp[2]