from django.urls import path,include
from django.conf.urls import url
from second_app import views
urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^user/',views.user,name='user')
    
]