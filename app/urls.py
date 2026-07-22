from django.urls import path
from app.views import test,testtemplate
urlpatterns=[
    path("test/",test,name="testview"),
    path("testtemplate/",testtemplate,name="testtemplate")
]