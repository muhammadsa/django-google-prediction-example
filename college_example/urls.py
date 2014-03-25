from django.conf.urls import patterns, include, url

urlpatterns = patterns('college_example',
	url(r'^$', 'views.index'),
	url(r'^create/$', 'views.generate_model'),
)