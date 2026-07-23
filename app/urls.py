from django.urls import path
from app.views import test,testtemplate,Welcome,submitdata,getall,takedatatemplate
urlpatterns=[
    path("test/",test,name="testview"),
    path("testtemplate/",testtemplate,name="testtemplate"),
    path("welcome/",Welcome,name="welcome"),
    path("submitdata/",submitdata,name="submitdata"),
    path("getall/",getall,name="getall"),
    path("takedata/",takedatatemplate,name="takedata"),
]