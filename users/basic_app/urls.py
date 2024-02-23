from django.conf.urls import url
from basic_app import views
from django.urls import path

app_name='basic_app'

urlpatterns=[
    #path('register/',views.register,name='register'),
    #path('',views.index,name='index')
    url(r'^register/$',views.register,name='register'),
    url(r'^$',views.index,name="index"),
    #login
    url(r'^user_login/$',views.user_login,name="user_login"),
    ]