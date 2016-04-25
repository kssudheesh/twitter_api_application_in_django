from django.shortcuts import render
import requests
from requests_oauthlib import OAuth1
import json

def index(request):
    consumer_key="XXXXXXXXX" #replace with your consumer key
    consumer_secret="XXXXXXXXX" # replace with your consumer secret
    access_token="XXXXXXXXXXXX" # replace with your access token
    access_token_secret="XXXXXXXXXXX" # replace with your access token secret
    if request.method == 'POST':
        twitter_handle = request.POST.get('screen_name')
        count = request.POST.get('count')
        auth = OAuth1(consumer_key, consumer_secret, access_token, access_token_secret)
        tweets_response = requests.get('https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name='+twitter_handle+'&count='+count, auth=auth)        
        tweets_dic = tweets_response.json()
        tweets = []
        for i in range(int(count)):
			tweets.append(tweets_dic[i]["text"])
        return render(request, 'twitter_app/index.html', {'tweets':tweets, 'handle':twitter_handle})
    else:
        return render(request, 'twitter_app/index.html', {})

