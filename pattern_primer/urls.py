from django.conf.urls.defaults import patterns, url

from pattern_primer import views

urlpatterns = patterns('',
    url('^$',
        views.PatternsView.as_view(),
        name='pattern_primer')

)
