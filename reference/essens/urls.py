from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^$', views.reference, name='reference'),
    url(r'^home/$', views.home, name='home'),
    url(r'^reference/$', views.reference, name='reference'),
    url(r'^core/$', views.core, name='core'),
    url(r'^basicio/$', views.basicio, name='basicio'),
    url(r'^basicsetops/$', views.basicsetops, name='basicsetops'),
    url(r'^basictraversal/$', views.basictraversal, name='basictraversal'),
    url(r'^basicchange/$', views.basicchange, name='basicchange'),
    url(r'^basicanalysis/$', views.basicanalysis, name='basicanalysis'),

]