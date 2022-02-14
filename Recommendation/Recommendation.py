import pandas as pd
from math import *

# load dataset
ratings = pd.read_csv('ratings.csv', header= None)
ratings.columns = ['userId', 'itemId', 'rank', 'timestamp']

products = pd.read_csv('product.csv', header = None)
product = products.iloc[:, :5]
product.columns = ['itemId', 'title', 'sth', 'sb', 'url']

data = pd.merge(ratings[['userId', 'itemId', 'rank']], product, on = 'itemId')

# data = data[['userId', 'itemId', 'rank', 'title']].sort_values('userId')

dic = {}
for idx in range(len(data)):
    tmp = data.iloc[idx]

    if tmp[0] not in dic.keys():
        dic[tmp[0]] = {tmp[3]:tmp[2]}
    else:
        dic[tmp[0]][tmp[3]] = tmp[2]

class Recommendation:

    def __init__(self):
        self.dic = dic
        self.data = data
    
    def euc_dis(self, user1, user2):
        ''' calulate similarity
        '''
        user1_data = self.dic[user1]
        user2_data = self.dic[user2]

        dis = 0

        for key in user1_data.keys():
            if key in user2_data.keys():
                dis += pow(float(user1_data[key]) - float(user2_data[key]), 2)

        return self, 1/(1+sqrt(dis))

    def top10_sim(self, userId):
        ''' get top 10 items
        '''
        res = []
        for userid in self.dic.keys():
            if not userid == userId:
                _, sim = self.euc_dis(userId, userid)
                res.append((userid, sim))
        
        res.sort(key = lambda x:x[1])
        return self, res[:10]

    def rec(self, user):
        ''' make a recommendation
        '''
        _, tmp = self.top10_sim(user)
        top_sim_user = tmp[0][0]

        items = self.dic[top_sim_user]

        recs = []

        for item in items.keys():
            if item not in self.dic[user].keys():
                recs.append((item, items[item]))
        
        recs.sort(key = lambda x:x[1], reverse= True)

        return recs[:10]

# if __name__ == '__init__':

    # print('hello2')