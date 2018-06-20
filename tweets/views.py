from django.shortcuts import render
from django.http import HttpResponse

from requests_oauthlib import OAuth1
from .form import userForm
import json
import requests


def twitter(request):

    consumer_key = ""
    consumer_sceret = ""
    access_token = ""
    token_secret = ""

    oauth = OAuth1(consumer_key, consumer_sceret, access_token, token_secret)


    form = userForm(request.POST)
    if form.is_valid():
        username = form.cleaned_data['username']
        url = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name="+username+"&count=10&tweet_mode=extended"
        response = requests.get(url, auth=oauth)
        tweets = []
        if response.status_code == 200:
            data = response.json()
            for tweet in data:
                tweets.append(tweet['full_text'])
        else:
            tweets.append('Invalid User Names !..')
        return render(request, "home.html", {"form" : form, "tweets" : tweets, "username" : username, "code" : response.status_code == 200})
    return render(request, "home.html", {"form" : form})
