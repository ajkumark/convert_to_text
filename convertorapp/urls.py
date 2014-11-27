from django.conf.urls import patterns, include, url


urlpatterns = patterns('convertorapp.views',
	url(r'^$', 'index', name='index'),
)