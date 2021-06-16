from django.shortcuts import render,redirect
from .models import Food,Consume


# Create your views here.
def index(request):

    if request.method=="POST":
        food_consumed = request.POST['food_consume']
        consume = Food.objects.get(name=food_consumed)
        user = request.user
        consume = Consume(user=user,food_consumed=consume)
        consume.save()
        foods = Food.objects.all()
        consumed_food = Consume.objects.filter(user=request.user)

    
    else:
        consumed_food = Consume.objects.filter(user=request.user)
        foods = Food.objects.all()
    return render(request,'myapp/index.html',{'foods':foods,'consumed_food':consumed_food})

