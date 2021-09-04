from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from doctors.serializers import doctorSerializer
from doctors.models import Doctor
from rest_framework.parsers import JSONParser
from rest_framework import status 
import requests
# Create your views here.

def head(request):
    return render(request,"header.html")


def add_d(request):
    return render(request,'addd.html')

def view_d(request):
    y=requests.get("http://127.0.0.1:8000/doctor/viewalld/").json()
    return render(request,'viewd.html',{"data":y})



def search_d(request):
    return render(request,'searchd.html')

def update_d(request):
    return render(request,'updated.html')


def delete_d(request):
    return render(request,'deleted.html')



@csrf_exempt
def doctor(request):
    if(request.method=="POST"):
        # mydic=JSONParser().parse(request)
        d_serial=doctorSerializer(data=request.POST)
        if (d_serial.is_valid()):
            d_serial.save()
            return JsonResponse(d_serial.data)
        else:
            return HttpResponse("error in serilazation")

    else:
        return HttpResponse("sucess")


@csrf_exempt
def doctorlist(request):
    if(request.method=="GET"):
        doctors=Doctor.objects.all()
        d_serial=doctorSerializer(doctors,many=True)
        return JsonResponse(d_serial.data,safe=False,status=status.HTTP_200_OK)

@csrf_exempt
def mydoctors(request,fetchid):
    try:
        doctor1=Doctor.objects.get(id=fetchid)
        if(request.method=="GET"):
            d_serial=doctorSerializer(doctor1)
            return JsonResponse(d_serial.data,safe=False)

        if(request.method=="DELETE"):
            doctor1.delete()
            return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)

        if(request.method=="PUT"):
            mydic=JSONParser().parse(request)
            d_serial=doctorSerializer(doctor1,data=mydic)
            if (d_serial.is_valid()):
                d_serial.save()
                return JsonResponse(d_serial.data,status=status.HTTP_200_OK)
            else:
                return JsonResponse(d_serial.errors,status=status.HTTP_400_BAD_REQUEST)

    except Doctor.DoesNotExist:
        return HttpResponse("invalid syntax",status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
def search_customer(request):
    try:
        getname=request.POST.get("doctorcode")
        print(getname)
        getcustomer=Doctor.objects.filter(doctorcode=getname)
        d_serial=doctorSerializer(getcustomer,many=True)
        return render(request,"searchd.html",{"data":d_serial.data})

        # return JsonResponse(customer_serial.data,safe=False,status=status.HTTP_200_OK)

    except Doctor.DoesNotExist:
        return HttpResponse("Invalid customer name",status=status.HTTP_404_NOT_FOUND)
    except: 
        return HttpResponse("something went wrong",status=status.HTTP_404_NOT_FOUND)   

@csrf_exempt
def update_api(request):
    try:
        getna=request.POST.get("doctorcode")
        print(getna)
        getdata=Doctor.objects.filter(doctorcode=getna)
        d_serial=doctorSerializer(getdata,many=True)
        return render(request,"updated.html",{"data":d_serial.data})

    except Doctor.DoesNotExist:
        return HttpResponse("Invalid name",status=status.HTTP_404_NOT_FOUND)

    except: 
        return HttpResponse("error",status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
def update_data(request):
    getid=request.POST.get("newid")

    getname=request.POST.get("newname")
    getemail=request.POST.get("newemail")
    getadress=request.POST.get("newaddress")
    getphno=request.POST.get("newphone")
    getspecial=request.POST.get("newspecial")
    getp=request.POST.get("newdoctorcode")


    mydata={'name':getname,'email':getemail,'address':getadress,'phone':getphno,'special':getspecial,'id':getid,'doctorcode':getp}
    jsondata=json.dumps(mydata)
    print(jsondata)
    Apilink="http://127.0.0.1:8000/doctor/viewd/" + getid
    requests.put(Apilink, data=jsondata)
    return HttpResponse("data has updated sucessfuly")




@csrf_exempt
def delete_api(request):
    try:
        getbno=request.POST.get("doctorcode")
        getc=Doctor.objects.filter(doctorcode=getbno)
        d_serial=doctorSerializer(getc,many=True)
        return render(request,"deleted.html",{"data":d_serial.data})
        # return JsonResponse(h_serial.data,safe=False,status=status.HTTP_200_OK)
    except Doctor.DoesNotExist:
        return HttpResponse("Invalid number",status=status.HTTP_404_NOT_FOUND)    
    
    except:
        return HttpResponse("something went wrong")


@csrf_exempt
def delete_data(request):
    getid=request.POST.get("newid")
    Apilink="http://127.0.0.1:8000/doctor/viewd/"+getid
    requests.delete(Apilink)
    return HttpResponse("data has deleted sucessfully")

