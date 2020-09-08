#%%
import json
import requests
import random
import pandas as pd
from bs4 import BeautifulSoup
import numpy as np
import datetime
import time

#%%
def water():

    df = pd.read_json('news_sampleData.json')
    df.to_csv('data/news_sampleData.csv', mode='a',index=0, header=0,encoding='utf-8-sig')
    print(df)
#%%
if __name__ == "__main__":
    water()