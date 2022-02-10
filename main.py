"""
# My first app
Here's our first attempt at using streamlit to build a app:
"""

import streamlit as st
import pandas as pd
import numpy as np
import time
import random
from Recommendation.Recommendation import *
from PIL import Image
import requests
from io import BytesIO

r = Recommendation()

st.title('Recommendation System')

left_column, right_column = st.columns(2)

with left_column:
    chosen_user = st.radio(
        'Who are you?',
        ("Jones Wan", "Chang Liu", "Chris Liu", "Jiayi Li", 
        "Ganmin Wu", "Tianxing Wang", "Yadi Yang", "Yong Yang"))

add_button = right_column.button('Press me!')

if add_button:
    'Welcome! My dear', chosen_user, '!'

    with st.spinner('Wait for recommendation...'):
        res = r.rec(random.choice(list(r.dic.keys())))
        res_ = [i[0] for i in res]
        urls = []
        for result in res:
            urls.append(r.data['url'][r.data['title'] == result[0]].iloc[0])

        imgs = []
        for url in urls:
            response = requests.get(url)
            imgs.append(Image.open(BytesIO(response.content)))

    st.success('Done!')
    'You might be interested in these items:'
    st.image(imgs, caption = res_, width = 140)