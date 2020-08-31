
# A very simple Flask app for creating a public API for Wikipedia summary and getting YouTube video...

from flask import Flask, redirect
from flask import request
import os
import wikipedia
import requests

app = Flask(__name__)

@app.route('/summary')
def give_summary():
    topic = request.args.get('topic')
    if topic.lower() == "anar":
        return "Anar is short form for Anupam Kumar, it is an Indian name."
    summary = wikipedia.summary(topic)
    return {"topic" : topic, "summary" : summary}

@app.route('/yt')
def playonyt():
    """Will play video on following topic, takes about 10 to 15 seconds to load"""
    title = request.args.get('title')
    redir = request.args.get('redirect')
    
    url = 'https://www.youtube.com/results?q=' + title
    count = 0
    cont = requests.get(url)
    data = cont.content
    data = str(data)
    lst = data.split('"')
    
    for i in lst:
        count+=1
        if i == 'WEB_PAGE_TYPE_WATCH':
            break
            
    if lst[count-5] == "/results":
        return ("No video found.")

    if redir == "true":
        return redirect("https://www.youtube.com"+lst[count-5], code=302)
    
    else:
        return {"title" : title, "url" : "https://www.youtube.com"+lst[count-5]}
