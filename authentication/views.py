from django.db import connections
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from util.dictfunc import multidel, multiget, multiset
from util.fetcher import *
# Create your views here.

def home(request):
    return render(request,'home.html')


def register(request):
    if request.method=='POST':
        name, email, password=multiget(request.POST, ['name', 'email', 'password'])
        multiset(request.session, ['name', 'email', 'password'], [name, email, password])
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
        name, password=multiget(request.POST, ['name', 'password'])
        with connections['coursora_db'].cursor() as db:
            db.execute('''SELECT * FROM "User"
                        WHERE "Name"=%s AND "Password"=%s ''', [name, password])
            qres = dictfetchone(db)
            if qres is not None:
                multiset(request.session, ['name', 'email', 'password'], multiget(qres, ['Name', 'Email', 'Password']))
                return redirect('/coursora/profile')
            else:
                return redirect('/coursora/login')
                

def profile(request):
    context = { 'name':request.session['name'] }
    return render(request, 'profile.html', context )

def logout(request):
    multidel(request.session, ['name', 'email', 'password'])
    return redirect('/coursora/login/')
    

    