from csv import unregister_dialect
from doctest import REPORT_CDIFF
from json import dump, dumps
import json
from django.db import connections
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from util.fetcher import dictfetchall, dictfetchone

def forum(request, forum_id):
    
    with connections['coursora_db'].cursor() as db:
        db.execute('''SELECT * FROM "COMMENT" WHERE "FORUM_ID"=%s ORDER BY "ID" ASC''', [forum_id])
        comments=dictfetchall(db)
        tree={}
        comment_dict={}
        users={}
        for comment in comments:
            if comment['PARENT_COMMENT_ID'] is not None and comment['PARENT_COMMENT_ID'] not in tree.keys():
                tree[comment['PARENT_COMMENT_ID']]=[]
            if comment['PARENT_COMMENT_ID'] is not None:
                tree[comment['PARENT_COMMENT_ID']].append(comment['ID'])
            comment_dict[comment['ID']]=comment
            db.execute('''SELECT * FROM "User" WHERE "ID"=%s''', [comment['USER_ID']])
            users[comment['USER_ID']]=dictfetchone(db)
        context={'tree': tree, 'comment_dict': comment_dict, 'users': users, 'forum_id': forum_id}
        print("gola")
        return render(request, 'forums/forum.html',{'context': json.dumps(context)})

@csrf_exempt   
def reply(request):
    response=json.loads(request.body)
    with connections['coursora_db'].cursor() as db:
        if 'parent_comment_id' not in response:
            db.execute('''INSERT INTO "COMMENT"("DESCRIPTION", "FORUM_ID", "USER_ID") VALUES(%s, %s, %s)''', [response['text'], response['forum_id'], request.session['id']])
        else :
            db.execute('''INSERT INTO "COMMENT"("DESCRIPTION", "FORUM_ID", "USER_ID", "PARENT_COMMENT_ID") 
            VALUES(%s, %s, %s, %s)''', [response['text'], response['forum_id'], request.session['id'], response['parent_comment_id']])
        return HttpResponse('/coursora/forum/'+str(response['forum_id'])+'/')
            