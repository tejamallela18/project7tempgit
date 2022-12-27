from django.urls import path
from app2.views import*
app_Name='some2'
urlpatterns=[
    path('second/',second,name='second')
]