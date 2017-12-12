# TrendingEvent
using twitter api to get trending event and analysis based in that data

Requirements
python 
django
mongodb

install following python packages:

pip install django
pip install tweepy
pip install git+https://github.com/django-nonrel/django@nonrel-1.5
pip install git+https://github.com/django-nonrel/djangotoolbox
pip install git+https://github.com/django-nonrel/mongodb-engine


go to TrendingEvent directory
python manage.py runserver 0.0.0.0:8000

Use following APIs:

GET http://127.0.0.1:8000/events/?count=1&keyword=python
params:
count = no of tweets to be fetched
keyword = comma separated list of keywords


GET http://127.0.0.1:8000/data/
no params: will fetch all the stored tweets
startswith: will fetch the tweets which are started with params value (http://127.0.0.1:8000/data/?startswith=Functions)
keyword: will fetch the tweets which has params value (http://127.0.0.1:8000/data/?keyword=checking a tool)

