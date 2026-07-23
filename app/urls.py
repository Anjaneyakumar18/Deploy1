from django.urls import path
from app.views import test,testtemplate,Welcome
urlpatterns=[
    path("test/",test,name="testview"),
    path("testtemplate/",testtemplate,name="testtemplate"),
    path("welcome/",Welcome,name="welcome")
]