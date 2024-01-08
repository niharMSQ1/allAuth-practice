from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def greet(request):
    return render(request, "index.html")
    # return JsonResponse({
    #     "message":"Hello World!"
    # })

@csrf_exempt
def dashboard(request):
    return render(request, "dashboard.html")