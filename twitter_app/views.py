from django.shortcuts import render
import requests
from requests_oauthlib import OAuth1
import json

def index(request):
    consumer_key="FhldcDcUvxTc5sMgGX4ZiPnmu"
    consumer_secret="skdRnITjxu8tXleSfbjeu153sZZ0OKQyZ2qvinYRNDH7PWiPD7"
    access_token="3255927978-LHMCwq262HY7T474kTSmSFHfsCPR4Ct5sNXPHUA"
    access_token_secret="EbEUetFFEiPV4sPQOEqTKg8awAIp8XbDJYo82SbfN9meH"
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

