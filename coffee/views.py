rom
django.shortcuts
import render, redirect

# Create your views here.
from .forms import *


def main(request):
    return render(request, "main.html", {})

    def login(request):
        return render(request, "login.html", {})

        def createCoffee(request):
            context = {}
            if request.method == "POST":
                form = CoffeeForm(request.POST)
                context['form'] = form
                if form.is_valid():
                    coffee = form.save(commit=False)
                    coffee.user = request.user
                    coffee.save()
                    form.save_m2m()
                return redirect("home")
            else:
                return render(request,“createCoffee.html”, context)
                else:
                    form = CoffeeForm()
                    context['form'] = form
                     return render(request,"createCoffee.html", context)

                def editCoffee(request, coffee_id):
                    context = {}
                    coffee = Coffee.objects.get(id=coffee_id)
                    context['coffee']=coffee
                    if request.method == "POST":
                        form = CoffeeForm(request.POST, instance=coffee)
                        context['form']=form
                        if form.is_valid():
                            coffee = form.save(commit=False)
                            coffee.user = request.user
                            coffee.save
                            form.save_m2m()
                            return redirect("home")
                        else:
                            return render(request,"editCoffee.html", context)
                        else:
                            form = CoffeeForm(instance=coffee)
                            context['form']=form
                            return render(request,"editCoffee.html", context)
