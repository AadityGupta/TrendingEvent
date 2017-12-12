from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
from settings import access_token, access_token_secret, consumer_key, consumer_secret
from django.http import HttpResponse
from models import Tweet


class StdOutListener(StreamListener):
    def __init__(self, total=100, *args, **kwargs):
        self.total = total
        self.count = 0
        super(StdOutListener, self).__init__(*args, **kwargs)

    def on_data(self, data):
        self.count += 1
        # table.insert({"text": json.loads(data)["text"]})
        print data
        Tweet(data=json.loads(data)).save()
        print "#############################"
        if self.count == self.total:
            return False
        else:
            return True

    def on_error(self, status):
        print status


def fetch_twitter_events(request):
    keywords = []
    try:
        count = int(request.REQUEST.get('count', '100'))
        data = request.REQUEST.get('keyword', None)
        if not data:
            return HttpResponse(json.dumps({"status": "failed", "reason": "count/keyword required"}),
                                content_type='application/json', status=404)
        else:
            data = data.split(",")
            keywords = [i for i in data]
    except:
        return HttpResponse(json.dumps({"status": "failed", "reason": "error in parameter count/keyword"}),
                            content_type='application/json', status=404)
    l = StdOutListener(total=count)
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    stream.filter(track=keywords)
    return HttpResponse(json.dumps({"status": "Success", "remarks": "Data has been imported"}),
                        content_type='application/json', status=200)


def get_twitter_events(request):
    data = []
    startswith = request.REQUEST.get('startswith', None)
    keyword = request.REQUEST.get('keyword', None)
    if startswith:
        records = Tweet.objects.raw_query({"data.text": {"$regex": "^"+startswith}})
    elif keyword:
        records = Tweet.objects.raw_query({"data.text": {"$regex": keyword}})
    else:
        records = Tweet.objects.raw_query({})
    for record in records:
        data.append(record.data)
    return HttpResponse(json.dumps(data), content_type='application/json', status=200)