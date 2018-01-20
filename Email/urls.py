
from django.conf.urls import url,include
from django.contrib import admin
from Email import views
urlpatterns = [
    url(r'^sendmail/$',views.SendMail, name="SendMail"),

]