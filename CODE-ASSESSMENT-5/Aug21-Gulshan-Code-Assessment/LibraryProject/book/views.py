from book.models import Books
import book
from book.serializers import Bookserializer
from django.shortcuts import render
from rest_framework.parsers import JSONParser
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse,HttpResponse
from rest_framework import status


#--------Add book Through Web-page---------#
def add(request):
    return render(request,'index1.html')




#--------Add Book through Postman---------#
@csrf_exempt
def add_book(request):
    if(request.method == "POST"):
        book= JSONParser().parse(request)
        book_serialize = Bookserializer(data=book)
        if(book_serialize.is_valid()):
            book_serialize.save()
            return JsonResponse(book_serialize.data, status = status.HTTP_200_OK)
        else:
            return HttpResponse("error")

    else:
            return HttpResponse("No get method")






#-------------view books----------------#
@csrf_exempt 
def all_view(request):
    if(request.method == "GET"):
        book= Books.objects.all()
        book_serialize =Bookserializer(book, many=True)
        return JsonResponse(book_serialize.data,safe=False, status=status.HTTP_200_OK)




#---------function for Update, Delete and view one by one-----------#
@csrf_exempt
def update(request,fetchid):
    try:
        book = Books.objects.get(id=fetchid)
        if(request.method == "GET"):
            book_serialize = Bookserializer(book)
            return JsonResponse(book_serialize.data,status=status.HTTP_200_OK)

        if (request.method == "DELETE"):
            book.delete()
            return HttpResponse("deleted",status=status.HTTP_200_OK)

        if(request.method == "PUT"):
            mybook = JSONParser().parse(request)
            book_serialize = Bookserializer(data=mybook)
            if(book_serialize.is_valid()):
                book_serialize.save()
                return JsonResponse(book_serialize.data,status=status.HTTP_200_OK)
            
    except Books.DoesNotExist:
        return HttpResponse("You Enter Invalid ID",status=status.HTTP_404_NOT_FOUND)
 





#------------view book by bookname--------------#
@csrf_exempt
def by_bookname(request,bookname):
    book = Books.objects.get(bookname=bookname)
    if(request.method == "GET"):
        book_serialize = Bookserializer(book)
        return JsonResponse(book_serialize.data,status=status.HTTP_200_OK)
    else:
        return HttpResponse("You Enter Invalid ID",status=status.HTTP_404_NOT_FOUND)