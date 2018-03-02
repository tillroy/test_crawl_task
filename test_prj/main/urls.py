from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main, name='main'),
    # url(r'curr_data/(?P<pk>[0-9]+)/$', views.curr_list, name='curr_list_data'),
    url(r'curr_data/(?P<pk>[0-9]+)', views.curr_list, name='curr_list_data'),
]