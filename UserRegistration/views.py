from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User
from django.http import JsonResponse
from UserRegistration.send_mail import mail


# Create your views here.

def index(request):
    #return HttpResponse('<p> Hiiiiiiii </p>')
    return render(request, 'index.html')

def register(request):
     data ={}
     if request.method == "POST":
         print(request.POST)
         firstname = request.POST.get("first_name")
         lastname = request.POST.get("last_name")
         email = request.POST.get("email")
         phone = request.POST.get("phone")
         dob = request.POST.get("dob")
         try:
             user = User(firstname= firstname, lastname= lastname, email = email, phone= phone, dob = dob).save()
             data['firstname'] = firstname
             data['lastname'] = lastname
             data['email'] = email
             data['phone'] = phone
             data['dob'] = dob
             data['status'] = 1
             mail(email, firstname)
         except Exception as e:
             print(e)
             data['status'] = 0
            #mail(firstname, email)
            #return HttpResponse(request, '<p> Data Save </p>')
     return JsonResponse(data, safe=False)


def delete(request):
    d={}
    id=request.GET.get("id")
    try:
        User.objects.filter(id=id).delete()
        d['status'] = 1
    except:
        d['status'] = 0
    return JsonResponse(d, safe=False)

def view(request):
    d={}
    user = User.objects.filter().values()
    d['user_data']=list(user)
    return JsonResponse(d, safe=False)




