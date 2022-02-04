from json import dump, dumps
import json
from django.db import connections
from django.shortcuts import render

from util.fetcher import dictfetchall

def forum(request, forum_id):
    with connections['coursora_db'].cursor() as db:
        db.execute('''SELECT * FROM "COMMENT" WHERE "FORUM_ID"=%s''', [forum_id])
        comments=dictfetchall(db)
        tree={}
        comment_dict={}
        parent={}
        for comment in comments:
            if comment['PARENT_COMMENT_ID'] not in tree.keys():
                tree[comment['PARENT_COMMENT_ID']]=[]
            tree[comment['PARENT_COMMENT_ID']].append(comment['ID'])
            parent[comment['ID']]=comment['PARENT_COMMENT_ID']
            comment_dict[comment['ID']]=comment
        
        context={'tree': tree, 'comment_dict': comment_dict, 'parent': parent}

        return render(request, 'forums/forum.html',{'context': json.dumps(context)})
    
