from django.shortcuts import render

# Create your views here.
# name,address, department, college)
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
@csrf_exempt

def detail(request):
    if (request.method=="POST"):
        getName = request.POST.get("name")
        getAddress = request.POST.get("address")
        getDepartment = request.POST.get("department")
        getCollege = request.POST.get("college")
        dic={"name":getName,"address":getAddress,"department":getDepartment,"college":getCollege}
        result=json.dumps(dic)
        return HttpResponse(result)
    else:
        return HttpResponse("No Get Method")
