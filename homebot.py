#!/usr/bin/env python
# coding: utf-8
import tweepy
import datetime

CONSUMER_KEY = "YOUR_CONSUMER_KEY"
CONSUMER_SECRET = "YOUR_CONSUMER_SECRET"
ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
ACCESS_TOKEN_SECRET = "YOUR_ACCESS_TOKEN_SECRET"
auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth_handler=auth)

##フォロワーの取得,ファイルへの書き込み
#f = open('follower.txt', 'w')
#for n in tweepy.Cursor(api.followers).items():
#  f.writelines(n.screen_name + ',')
#f.close()

#ランダムにフォロワーを抜き出す
import random
follower = []
for line in open('follower.txt','r'):
   follower = line.split(',')

random.shuffle(follower)
d = datetime.datetime.today()
#リプライ内容の作成
for i in range(1,5):
  if d.hour >= 6 and d.hour < 12:
    str = '@' + follower[i] + 'ちゃん、朝からえらいえらい！'
    api.update_status(str)
  elif d.hour >= 12 and d.hour < 20:
    str = '@' + follower[i] + 'ちゃん、お昼もえらいえらーい！'
    api.update_status(str)
  else:
    str = '@' + follower[i] + 'ちゃん、夜になってもえらいえらーい！'
    api.update_status(str)
  
  


