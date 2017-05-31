from django.shortcuts import render, redirect

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
            return render(request, "createCoffee.html", context)
    else:
        form = CoffeeForm()
        context['form'] = form
        return render(request, "createCoffee.html", context)


def editCoffee(request, coffee_id):
    context = {}
    coffee = Coffee.objects.get(id=coffee_id)
    context['coffee'] = coffee
    if request.method == "POST":
        form = CoffeeForm(request.POST, instance=coffee)
        context['form'] = form
        if form.is_valid():
            coffee = form.save(commit=False)
            coffee.user = request.user
            coffee.save
            form.save_m2m()
            return redirect("home")
        else:
            return render(request, "editCoffee.html", context)
    else:
        form = CoffeeForm(instance=coffee)
        context['form'] = form
        return render(request, "editCoffee.html", context)


def createBean(request):
    context = {}
    if request.method == "POST":
        form = BeanForm(request.POST)
        context['form'] = form
        if form.is_valid():
            coffee = form.save()
            return redirect("home")
        else:
            return render(request, "createCoffee.html", context)
    else:
        form = BeanForm()
        context['form'] = form
        return render(request, "createCoffee.html", context)


def editBean(request, bean_id):
    context = {}
    bean = Bean.objects.get(id=bean_id)
    context['bean'] = bean
    if request.method == "POST":
        form = BeanForm(request.POST, instance=bean)
        context['form'] = form
        if form.is_valid():
            bean = form.save()
            return redirect("home")
        else:
            return render(request, "editBean.html", context)
    else:
        form = BeanForm(instance=bean)
        context['form'] = form
        return render(request, "editBean.html", context)


def deleteBean(request, bean_id):
    Bean.objects.get(id=bean_id).delete()
    return redirect("home")


def deleteCoffee(request, coffee_id):
    Coffee.objects.get(id=coffee_id).delete()
    return redirect("home")


def createRoast(request):
    context = {}
    if request.method == "POST":
        form = RoastForm(request.POST)
        context['form'] = form
        if form.is_valid():
            roast = form.save()
            return redirect("home")
        else:
            return render(request, "createRoast.html", context)
    else:
        form = RoastForm()
        context['form'] = form
        return render(request, "createRoast.html", context)


def editRoast(request, roast_id):
    context = {}
    roast = Roast.objects.get(id=roast_id)
    context['roast'] = roast
    if request.method == "POST":
        form = RoastForm(request.POST, instance=roast)
        context['form'] = form
        if form.is_valid():
            roast = form.save()
            return redirect("home")
        else:
            return render(request, "editRoast.html", context)
    else:
        form = RoastForm(instance=roast)
        context['form'] = form
        return render(request, "editRoast.html", context)


def deleteRoast(request, roast_id):
    Roast.objects.get(id=roast_id).delete()
    return redirect("home")


def createSyrup(request):
    context = {}
    if request.method == "POST":
        form = SyrupForm(request.POST)
        context['form'] = form
        if form.is_valid():
            syrup = form.save()
            return redirect("home")
        else:
            return render(request, "createSyrup.html", context)
    else:
        form = SyrupForm()
        context['form'] = form
        return render(request, "createSyrup.html", context)


def editSyrup(request, syrup_id):
    context = {}
    syrup = Syrup.objects.get(id=syrup_id)
    context['syrup'] = syrup
    if request.method == "POST":
        form = SyrupForm(request.POST, instance=syrup)
        context['form'] = form
        if form.is_valid():
            syrup = form.save()
            return redirect("home")
        else:
            return render(request, "editSyrup.html", context)
    else:
        form = SyrupForm(instance=syrup)
        context['form'] = form
        return render(request, "editSyrup.html", context)


def deleteSyrup(request, syrup_id):
    Syrup.objects.get(id=syrup_id).delete()
    return redirect("home")


def createPowder(request):
    context = {}
    if request.method == "POST":
        form = PowderForm(request.POST)
        context['form'] = form
        if form.is_valid():
            powder = form.save()
            return redirect("home")
        else:
            return render(request, "createPowder.html", context)
    else:
        form = PowderForm()
        context['form'] = form
        return render(request, "createPowder.html", context)


def editPowder(request, powder_id):
    context = {}
    powder = Powder.objects.get(id=powder_id)
    context['powder'] = powder
    if request.method == "POST":
        form = PowderForm(request.POST, instance=powder)
        context['form'] = form
        if form.is_valid():
            powder = form.save()
            return redirect("home")
        else:
            return render(request, "editPowder.html", context)
    else:
        form = SyrupForm(instance=powder)
        context['form'] = form
        return render(request, "editPowder.html", context)


def deletePowder(request, powder_id):
    Powder.objects.get(id=powder_id).delete()
    return redirect("home")


def createOrder(request, coffee_id):
    context = {}
    coffee = Coffee.objects.get(id=coffee_id)
    context['coffee'] = coffee
    if request.method == 'POST':
        form = OrderForm(request.POST)
        context['form'] = form
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.coffee = coffee
            order.save()
            return redirect("home")
        else:
            return render(request, "createOrder.html", context)
    else:
        form = OrderForm()
        context['form'] = form
        return render(request, "createOrder.html", context)


def user_list(request):
    context = {}
    user_list = User.objects.all()
    context['user_list'] = user_list
    return render(request, 'user_list.html', context)

def user_coffees(request, user_id):
    context = {}
    user = User.objects.get(id=user_id)
    context['user'] = user
    coffees = Coffee.objects.filter(user=user)
    context['coffees'] = coffees
    return render(request, 'user_coffees.html', context)
