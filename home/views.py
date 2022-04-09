from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Todo
from .serilizer import TodoSerilizer
from home import serilizer
# Create your views here.


# For handeling all routes in default.
@api_view(['GET','POST','PATCH'])
def api(request):
    if request.method == 'GET':
        return Response({
            'status':200,
            'message':'Yes  Django Rest Freamwork is working ',
            'method_called':'GET'
        })
    if request.method == 'POST':
        return Response({
            'status':200,
            'message':'Yes  Django Rest Freamwork is working ',
            'method_called':'POST'
        })
    if request.method == 'PATCH':
        return Response({
            'status':200,
            'message':'Yes  Django Rest Freamwork is working ',
            'method_called':'PATCH'
        })

# To List all todo Items
@api_view(['GET'])
def list_all_todo_item(request):
    todo_objs = Todo.objects.all()
    serilizer = TodoSerilizer(todo_objs, many=True)
    return Response({
        'status':True,
        'message':'Todo fached',
        'data':serilizer.data
    })

# To add todo items
@api_view(['POST'])
def add_todo_item(request):
    try:
        data = request.data 
        serilizer = TodoSerilizer(data = data)
        # print(serilizer.data)

        if serilizer.is_valid():
            serilizer.save()
            return Response({
                'status':True,
                'message':'Todo item add success',
                'data':serilizer.data
            })
        else:
            return Response({
                'status':False,
                'message':'invalid data',
                'data':serilizer.errors
            })    
    except Exception as e:
        print(e)
        return Response({
            'status':False,
            'message':'something went wrong..'
        })        
@api_view(['PATCH'])
def patch_todo(request):
    try:
        data = request.data
        if not data.get('id'):
            return Response({
                'status':False,
                'message':'id is required',
                'data':{}
            })
        obj = Todo.objects.get(id=data.get('id'))
        serilizer = TodoSerilizer(obj,data = data, partial=True)

        if serilizer.is_valid():
            serilizer.save()
            return Response({
                'status':True,
                'message':'update success',
                'data':serilizer.data
            })
        return Response({
            'status':False,
            'message':'invalid data',
            'data':serilizer.errors
        })

    except Exception as e:
        print(e)
        return Response({
            'status':False,
            'message':'invalid id',
            'data':serilizer.errors
        })    
