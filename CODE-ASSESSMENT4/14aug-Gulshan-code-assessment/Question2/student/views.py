
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

# name,admission number, roll number, college, parent name
@csrf_exempt
def detail(request):
    if (request.method=="POST"):
        getName = request.POST.get("name")
        getAdmission_num = request.POST.get("admission_num")
        getRoll_no = request.POST.get("rollno")
        getCollege = request.POST.get("college")
        getParent_name = request.POST.get("parentname")
        dic={"name":getName,"admission_num":getAdmission_num,"rollno":getRoll_no,"college":getCollege,"parentname":getParent_name}
        result=json.dumps(dic)
        return HttpResponse(result)
    else:
        return HttpResponse("No Get Method")
