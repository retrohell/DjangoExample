from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import ExampleModel
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the djapp index.")
# Path: djexample/djapp/urls.py

def exampleModel(request):
    example = get_object_or_404(ExampleModel.objects.values())
    return JsonResponse(example, safe=False)

def exampleModelById(request, id):
    example = get_object_or_404(ExampleModel, id=id)
    return HttpResponse('Example: %s' % example.name)
