from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from student.serializer import StudentSerializer
from django.http.response import JsonResponse
from django.http.response import HttpResponse
from student.models import Studentapp
import json
import requests

def register(request):
    return render(request,'register.html')

# def search(request):
#     return render(request,'search.html')
# def dashboard(request):
#     return render(request, 'dashboard.html')




@csrf_exempt
def student(request):
    if(request.method=="POST"):
        studata=JSONParser().parse(request)
        Student_Serializer= StudentSerializer(data=studata)
        if(Student_Serializer.is_valid()):
            Student_Serializer.save()
            return redirect(dashboard)
            # return JsonResponse(Student_Serializer.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("No get method",status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
def login_check(request):
    try:
        getUsername=request.POST.get("username")
        getpassword =request.POST.get("password")

        getUsers =Studentapp.objects.filter(username=getUsername, password = getpassword)
        user_serializer = StudentSerializer(getUsers, many=True)
        print(user_serializer.data)
        if (user_serializer.data):
            for i in user_serializer.data:
                getID = i["id"]
                getName = i["name"]
                getUsername =i["username"]
            #session
            request.session['uid']=getID
            request.session['uname'] =getName
            # data ={"name":getName, "username":getUsername}
            # return render(request, 'dashboard.html',{"data":data})
            return redirect(dashboard)
        else:
            return HttpResponse("Invalid")

    except Studentapp.DoesNotExist:
        return HttpResponse("Invalid username or password", status=status.HTTP_404_NOT_FOUND)

    except:
        return HttpResponse("Something went wrong")

def dashboard(request):
    try:
        getUid = request.session['uid']
        getUsers = Studentapp.objects.get(id=getUid)
        admin_serialiser = StudentSerializer(getUsers)

        return render(request, 'dashboard.html',{"data":admin_serialiser.data})

    except:
        return HttpResponse("Went wrong")


@csrf_exempt
def student_list(request):
    if(request.method == "GET"):
        students = Studentapp.objects.all()
        Student_Serializer= StudentSerializer(students, many=True)
        return JsonResponse(Student_Serializer.data, safe=False)


@csrf_exempt
def studentdetail(request,id):
    try:
        students=Studentapp.objects.get(admission_number=id)
        if(request.method == "GET"):
            Student_Serializer=StudentSerializer(students)
            return JsonResponse(Student_Serializer.data, safe=False, status=status.HTTP_200_OK)

        if(request.method=="DELETE"):
            students.delete()
            return HttpResponse("deleted",status=status.HTTP_204_NO_CONTENT)

        if(request.method == "PUT"):
            studata=JSONParser().parse(request)
            Student_Serializer = StudentSerializer(students,data=studata)
            if(Student_Serializer.is_valid()):
                Student_Serializer.save()
                return JsonResponse(Student_Serializer.data,status=status.HTTP_200_OK)

            else:
                return HttpResponse("Error in serialization")

    except Studentapp.DoesNotExist:
        return HttpResponse("Invalid Student admission number",status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
def updatesearchapi(request):
    try:
        getEmpCode=request.POST.get("id")
        getEmployee=Studentapp.objects.filter(empcode=getEmpCode)
        employee_serializer=StudentSerializer(getEmployee,many=True)
        return render(request,"updateemploye.html",{"data":employee_serializer.data})
        #return JsonResponse(employee_serializer.data,safe=False,status=status.HTTP_200_OK)
    except Studentapp.DoesNotExist:
        return HttpResponse("Invalid data",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("invalid")

@csrf_exempt
def update_data_read(request):

    getid=request.POST.get("newid")
    getname=request.POST.get("newname")
    getaddress=request.POST.get("newaddress")
    getclas=request.POST.get("newclas")
    getmob=request.POST.get("newmob_num")
    getusername=request.POST.get("newusername")
    getpassword=request.POST.get("newpassword")
    mydata={'name':getname,'id':getid,'address':getaddress,'name':getname,'clas':getclas,'mob_num':getmob,'username':getusername,'password':getpassword}
    jsondata=json.dumps(mydata)
    print(jsondata)
    Apilink="http://localhost:8000/Admin/view/"+getid
    requests.put(Apilink,data=jsondata)
    return redirect(student_list)