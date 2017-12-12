from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    # Examples:
    # url(r'^$', 'TrendingEvent.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^events/$', 'TrendingEvent.views.fetch_twitter_events'),
    url(r'^data/$', 'TrendingEvent.views.get_twitter_events'),
]
