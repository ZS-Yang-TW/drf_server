from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse
import json

def index(request):
    return HttpResponse("Hello, world. You're at the chatapi index.")

def chatapi(request):
    if request.method == 'POST':
        try:
            # 使用json.loads解析请求体中的JSON数据
            data = json.loads(request.body)
            username = data.get('username', '')
            message = data.get('message', '')

            # 这里可以处理接收到的数据，比如保存到数据库或者其他操作

            # 返回JSON响应
            response_data = {
                'status': 'success',
                'message': 'Data received successfully',
                'username': username,
                'message': message,
            }
            return JsonResponse(response_data)

        except json.JSONDecodeError as e:
            # 如果无法解析JSON数据，返回错误响应
            response_data = {
                'status': 'error',
                'message': 'Invalid JSON data',
            }
            return JsonResponse(response_data, status=400)