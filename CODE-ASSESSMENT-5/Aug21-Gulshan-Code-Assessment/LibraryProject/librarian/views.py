from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
# Create your views here.
from librarian.serializers import LibSerializer
from django.http.response import JsonResponse,HttpResponse
from librarian.models import Librarian
from rest_framework import status


#--------------Register----------------#
def register(request):
    return render(request,'index.html')


#------------Login--------------------#
def login(request):
    return render(request,'login.html')




#--------Function for adding the librarian---------#
@csrf_exempt
def lib_add(request):
    if(request.method == "POST"):
        lib= JSONParser().parse(request)
        lib_serialize = LibSerializer(data=lib)
        if(lib_serialize.is_valid()):
            lib_serialize.save()
            return JsonResponse(lib_serialize.data, status = status.HTTP_200_OK)
        else:
            return HttpResponse("error")

    else:
            return HttpResponse("No get method")




#---------function for view all the librarian---------#

@csrf_exempt 
def all_lib(request):
    if(request.method == "GET"):
        lib= Librarian.objects.all()
        lib_serialize =LibSerializer(lib, many=True)
        return JsonResponse(lib_serialize.data,safe=False, status=status.HTTP_200_OK)







#---------function for Update, Delete and view one by one-----------#

@csrf_exempt
def update(request,id):
    try:
        lib = Librarian.objects.get(id=id)
        if(request.method == "GET"):
            lib_serialize = LibSerializer(lib)
            return JsonResponse(lib_serialize.data,status=status.HTTP_200_OK)

        if (request.method == "DELETE"):
            lib.delete()
            return HttpResponse("deleted")

        if(request.method == "PUT"):
            mylib = JSONParser().parse(request)
            lib_serialize = LibSerializer(data=mylib)
            if(lib_serialize.is_valid()):
                lib_serialize.save()
                return JsonResponse(lib_serialize.data,status=status.HTTP_200_OK)
            
    except Librarian.DoesNotExist:
        return HttpResponse("You Enter Invalid ID",status=status.HTTP_404_NOT_FOUND)






#----------search librarian by enroll_code-----------#
@csrf_exempt
def search_By_enroll_code(request,enroll_code):
        lib = Librarian.objects.get(enroll_code=enroll_code)
        if(request.method == "GET"):
            lib_serialize = LibSerializer(lib)
            return JsonResponse(lib_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("You Enter Invalid ID",status=status.HTTP_404_NOT_FOUND)

