#%%
import json
import requests
import random
import pandas as pd
from bs4 import BeautifulSoup
import numpy as np
import datetime
import time
import jieba
#%%
def strQ2B(ustring):
    ss = []
    for s in ustring:
        rstring = ""
        for uchar in s:
            inside_code = ord(uchar)
            if inside_code == 12288:  # 全形空格直接轉換
                inside_code = 32
            elif (inside_code >= 65281 and inside_code <= 65374):  # 全形字元（除空格）根據關係轉化
                inside_code -= 65248
            rstring += chr(inside_code)
        ss.append(rstring)
    return ''.join(ss)

jieba.set_dictionary('jieba_data/user_receipt.txt')
#%%
with open(file='jieba_data/simple_stop_words.txt', mode='r', encoding='utf-8') as file:
    stop_words = file.read().split('\n')
#%%
# 精確模式分詞 (cut_all=False)
def cut(data):
    seg_stop_result_list = []
    seg_result = jieba.cut(data, cut_all=False)
    for term in seg_result:
        if term not in stop_words and term != ' ':
            seg_stop_result_list.append(term)
    return seg_stop_result_list

# 字典轉list
def user_dict_list():
    user_dict_list=[]
    with open('jieba_data/user_receipt.txt','r',encoding='utf-8') as f:
        for line in f:
            user_dict_list.append(line.strip('\n'))
    return user_dict_list

def df_col(inv_id, product_name, seller_address, inv_time, gender, age):
    columns=['inv_id','product_name','seller_address','inv_time','gender','age']
    df_f = pd.DataFrame(columns=columns)
    data = [inv_id, product_name, seller_address, inv_time, gender, age]
    df_f.loc[len(df_f)] = data
    print(time,area)
    df_f.to_csv('data/receipt.csv', mode='a',index=0, header=0,encoding='utf-8-sig')
    return

#%%
# 遍歷df title是否符合自建自典
df = pd.read_csv('data/發票怪獸sample data080.csv',encoding='utf-8')
for index,row in df.iterrows():
    if [i for i in cut(row['product_name']) if i in user_dict_list()]:
        inv_id = row['inv_id']
        product_name = row['product_name']
        seller_address = row['seller_address']
        inv_time = row['inv_time']
        gender = row['gender']
        age = row['age']

        df_col(inv_id, product_name, seller_address, inv_time, gender, age)




