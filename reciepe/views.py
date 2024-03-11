from django.shortcuts import render,redirect
from django.http import HttpRequest
from .models import *

# Create your views here.
def home_page(request):

    if request.POST:
        name = request.POST['recipeName']
        procedure = request.POST['recipeProcedure']
        img = request.FILES.get('recipeImage')

        Recipe.objects.create(reciepe_name=name, procedure=procedure, img=img).save()

        return redirect('/home')
    context = Recipe.objects.all()
    recipes = {'recipes': context}
    return render(request,"home.html", recipes)

def delete(request, id):
    Recipe.objects.get(id=id).delete()

    return redirect('/home')
