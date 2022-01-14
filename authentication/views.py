from django.db import connections
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from util.fetcher import *
# Create your views here.


def register(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        request.session['name'] = name
        request.session['email'] = email
        request.session['password'] = password
        with connections['coursora_db'].cursor() as db:
            db.execute('''INSERT INTO "User"("Name", "Email", "Password")
                        VALUES(%s, %s, %s)''', [name, email, password])
            return redirect('/coursora/profile/')
    elif 'name' not in request.session:
        return render(request, 'register.html')
    else:
        return redirect('/coursora/profile/')

def login(request):
    if 'name' in request.session: 
        return redirect('/coursora/profile/')
    elif request.method == 'GET':
       return render(request, 'login.html')
    else:
        name = request.POST['name']
        password = request.POST['password']
        with connections['coursora_db'].cursor() as db:
            db.execute('''SELECT * FROM "User"
                        WHERE "Name"=%s AND "Password"=%s ''', [name, password])
            qres = dictfetchone(db)
            if qres is not None:
                request.session['name'] = qres['Name']
                request.session['email'] = qres['Email']
                request.session['password'] = qres['Password']
                return redirect('/coursora/profile')
            else:
                return redirect('/coursora/login')
                

def profile(request):
    context = { 'name':request.session['name'] }
    return render(request, 'profile.html', context )

def logout(request):
    
    del request.session['name']
    del request.session['email']
    del request.session['password']
    return redirect('/coursora/login/')
    

    