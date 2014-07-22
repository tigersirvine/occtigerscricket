from django.conf.urls import url
from mainapp import views
urlpatterns = [
    url(r'^$', "mainapp.views.index", name='index'),
    url(r'getBattingScGridData/$', "mainapp.views.getBattingScGridData"),
    url(r'getBowlingScGridData/$', "mainapp.views.getBowlingScGridData"),
    url(r'scorecard/$', "mainapp.views.scorecard")
]
