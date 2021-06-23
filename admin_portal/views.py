from django.contrib.auth.models import auth
from django.contrib import messages
# from .models import Users,Meetings,Social_links
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json
import base64
from django.core.files.base import ContentFile
from uuid import uuid4
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render, redirect


# Create your views here.

@csrf_exempt
def login_a(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user:

            if user.is_superuser:
                auth.login(request, user)
                # return HttpResponse("ADMIN PAGE!!")
                return render(request, 'index.html')

        else:
            messages.info(request, 'Invalid Crendentials')
            return redirect('login')

    else:
        return render(request, 'login.html')
        # return HttpResponse("cvghdvcua")

@login_required
def index(request):
    return render(request, 'index.html')