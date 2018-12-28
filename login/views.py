from django.shortcuts import render
import json
from django.http import HttpResponse, JsonResponse
from .models import User
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate


# Create your views here.
def index(request):
    return render(request, 'login.html')



# Please review documents of Django and check how to use the authentication module provided by the framework.
# https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Authentication
@csrf_protect
def auth(request):
    # return JsonResponse({'status': 'fail'})
    user = authenticate(username=request.POST['id'], password=request.POST['pw'])
    if user is not None:
        return JsonResponse({'status': 'success',
                             'id': user.get_username(),
                             'char': user.character})

    else:
        return JsonResponse({'status': 'fail'})

