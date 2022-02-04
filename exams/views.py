from django.shortcuts import redirect, render
from django.db import connections
from django.http import HttpResponse
from util.dictfunc import multiget

from util.fetcher import *

def exam(request, exam_id):
    with connections['coursora_db'].cursor() as db:
        db.execute('''SELECT * 
        FROM "EXAM" JOIN  "CONTENT" ON ("EXAM"."CONTENT_ID"="CONTENT"."ID")
        JOIN "Course" ON ("CONTENT"."COURSE_ID"="Course"."ID")
        JOIN "COURSE_REGISTRATION" 
        ON ("COURSE_REGISTRATION"."COURSE_ID"="Course"."ID" AND "COURSE_REGISTRATION"."STUDENT_ID"=%s)''', [request.session['id']])

        registered=dictfetchall(db)
        # print(registered is None)
        # return HttpResponse(registered)
        if not registered:
           return HttpResponse('course not registered')

        if request.method=='POST':
            return HttpResponse(request.POST['1'])
        else :
            db.execute('''SELECT * FROM QA WHERE EXAM_ID=%s''', [exam_id])
            questions=dictfetchall(db)
            return render(request, 'exams/questions.html', {'questions':questions, 'exam_id': exam_id})

