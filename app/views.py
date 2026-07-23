from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from app.models import User,Student
import json
# Create your views here.

@csrf_exempt
def test(request):
    return HttpResponse("yessss")

@csrf_exempt
def testtemplate(request):
    return render(request,"hello.html")

@csrf_exempt
def Welcome(request):
    return render(request,"welcome.html")

@csrf_exempt
def takedatatemplate(request):
    return render(request,"takedata.html")


@csrf_exempt
def addStudent(request):
    data=json.loads(request.data)
    try:
        s=Student(
            name=data['name'],
            cclass=data['cclass'],
            fee=data['fee'],
            gender=data['gender']
        )
        s.save()
        return HttpResponse("Student datasuccessfully stored!!!")

    except Exception as e:
        
        return HttpResponse("Failed to save student data")
    return HttpResponse("Failed Operation!!")

@csrf_exempt
def getstudents(request):
    try:
        data=list(Student.objects.values())
        return JsonResponse(data)
    except Exception as e:
        return JsonResponse("failed to laod students data")
    return JsonResponse("failed to laod students data")
@csrf_exempt
def submitdata(request):

    if request.method == "POST":

        try:
            data = json.loads(request.body)
            u = User(
                name=data["name"],
                password=data["password"]
            )
            u.save()
            return HttpResponse("User data submitted successfully.")

        except Exception as e:
            return HttpResponse(f"Failed to submit user: {str(e)}")

    return HttpResponse("Invalid Request")

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def getall(request):

    if request.method == "GET":

        users = list(User.objects.values())

        return JsonResponse(users, safe=False)

    return JsonResponse(
        {"message": "Invalid Request"},
        status=400
    )

