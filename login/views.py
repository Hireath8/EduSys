from django.shortcuts import render
import json
from django.http import HttpResponse, JsonResponse
from .models import User
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_protect


# Create your views here.
def index(request):
    return render(request, 'login.html')


@csrf_protect
def auth(request):
    users = get_object_or_404(User)
    # return JsonResponse({'status': 'fail'})
    try:
        ans = User.objects.get(UserName=request.POST['id'])
    except (KeyError, User.DoesNotExist):
        return JsonResponse({'status': 'fail'})
        # return HttpResponse(json.dumps({'status': 'fail'}))
    else:
        return JsonResponse({'status': 'success',
                             'id': ans.UserName,
                             'char': ans.Character})
        # return render(request, 'success.html', json.dumps({'status': 'success',
                                                          # 'id': ans.UserName,
                                                          # 'char': ans.Character})
