from django.shortcuts import render, redirect
from . models import PoductDetails, userDetail, cart, usercheck
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import accountform, userForm
from django.contrib import messages





def home(request):

    product = PoductDetails.objects.get(id = 1)
    top_10_product_topoffer = PoductDetails.objects.filter(category = 'topoffer')
    top_10_product_todaydeal = PoductDetails.objects.filter(category = 'todaydeal')

    if request.method == 'POST':
        key = request.POST.get('keyword').capitalize()
        top_10_product_topoffer = PoductDetails.objects.filter(category = 'topoffer', name__contains = key)
        top_10_product_todaydeal = PoductDetails.objects.filter(category = 'todaydeal', name__contains = key)

    return render(request, 'productpage.html' , context = {

        "top_10_product_topoffer":top_10_product_topoffer[:20],
        "top_10_product_todaydeal":top_10_product_todaydeal[:20],
        'product':product,
        })



def payment(request):

    return render(request, "productdesc.html")

def product_detail(request,id):

    product = PoductDetails.objects.get(id = id)

    return render(request, "productdesc.html",{'product':product});

def address(request):

    return render(request, "address.html");
def signin_Page(request):
    form = userForm()
    if request.method == "POST":
        print('a')
        form = userForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, "This account is created for "+username)
            userDetail.objects.create(user = User.objects.get(username = username))
            return redirect('/login')
    context = {
        'form':form
    }
    return render(request,'register.html', context)
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.info(request,'The username or password is incorrect')
            return render(request, 'login.html')
    return render(request, 'login.html')
def logoutpage(request):
    logout(request)
    return redirect('home')
def accountpage(request, id):
    user = User.objects.get(id = id)
    if not (userDetail.objects.filter(user = user)):
        a = userDetail.objects.create(user = user)
        a.save()
    detail = userDetail.objects.get(user = user)
    context = {
        'detail':detail
    }
    return render(request, 'account.html', context)
def add_to_cart(request, id1, id2):
    user = User.objects.get(id = id1)
    userDet = userDetail.objects.get(user = user)
    product = PoductDetails.objects.get(id = id2)
    user_cart = cart.objects.create(user = userDet, product = product)
    user_cart.save()

    messages.info(request, product.name+ "is added to your cart!")
    return redirect('home')
def mycart(request, id):
    user = User.objects.get(id = id)
    userdetail = userDetail.objects.get(user = user)
    user_cart = cart.objects.filter(user = userdetail)
    if user_cart:
        if request.method == 'POST':
            id_p = request.POST.get('id')
            user_pro = cart.objects.get(id = id_p)
            user_pro.quantity = request.POST.get('num')
            total1 = 0
            for i in user_cart:
                if i.product.discount:
                    total1 += float(i.product.discount)*int(i.quantity)
                else:
                    total1 += float(i.product.price)*int(i.quantity)
            user_pro.save()
            user = User.objects.get(id = id)
            userdetail = userDetail.objects.get(user = user)
            user_cart = cart.objects.filter(user = userdetail)
            context = {
                'user_cart':user_cart,
                'total':total1
            }
            return render(request, 'mycart.html', context)
        total1 = 0
        for i in user_cart:
            if i.product.discount:
                total1 += float(i.product.discount)*int(i.quantity)
            else:
                total1 += float(i.product.price)*int(i.quantity)
        context = {
            'user_cart':user_cart,
            'total':total1
        }
        return render(request, 'mycart.html', context)
    return render(request, 'mycart.html')

def del_cart(request, id):

    user_cart = cart.objects.filter(id = id)
    a = user_cart[0].user.user.id
    user_cart.delete()
    return redirect('/mycart/{}'.format(a))



def todaydeal_page(request):
    product = PoductDetails.objects.all()
    product_todaydeal = PoductDetails.objects.filter(category = 'todaydeal')
    if request.method == "POST":
        key = request.POST.get('keyword').capitalize()
        product_todaydeal = PoductDetails.objects.filter(name__contains = key, category = 'todaydeal')
    context = {
        'product':product,
        'product_todaydeal':product_todaydeal,
    }

    return render(request, 'todaydeal.html', context )


def topoffer_page(request):
    product = PoductDetails.objects.all()
    product_topoffer = PoductDetails.objects.filter(category = 'topoffer')
    if request.method == "POST":
        key = request.POST.get('keyword').capitalize()
        product_topoffer = PoductDetails.objects.filter(name__contains = key, category = 'topoffer')
    context = {
        'product':product,
        'product_topoffer':product_topoffer,
    }

    return render(request, 'todaydeal.html', context )


def veg_page(request):
    product = PoductDetails.objects.all()
    product_veg_frut = PoductDetails.objects.filter(category = 'vegetable')
    if request.method == "POST":
        key = request.POST.get('keyword').capitalize()
        product_veg_frut = PoductDetails.objects.filter(name__contains = key, category = 'vegetable')
    context = {
        'product':product,
        'product_veg':product_veg_frut,
    }

    return render(request, 'veg.html', context )




def cookingessential_page(request):
    product = PoductDetails.objects.all()
    product_cookingessential = PoductDetails.objects.filter(category = 'cookingessential')
    if request.method == "POST":
        key = request.POST.get('keyword').capitalize()
        product_cookingessential = PoductDetails.objects.filter(name__contains = key, category = 'cookingessential')
    context = {
        'product_cookingessential':product_cookingessential,
        'product':product,
    }
    return render(request, 'cookingessential.html', context )
def fruit_page(request):
    product = PoductDetails.objects.all()
    product_fruit = PoductDetails.objects.filter(category = 'fruit')
    if request.method == "POST":
        key = request.POST.get('keyword').capitalize()
        product_fruit = PoductDetails.objects.filter(name__contains = key, category = 'fruit')
    context = {
        'product_fruit':product_fruit,
        'product':product,
    }
    return render(request, 'fruit.html', context )


def spices_page(request):
    product = PoductDetails.objects.all()
    product_spices = PoductDetails.objects.filter(category = 'spices')
    if request.method == "POST":
        key = request.POST.get('keyword').capitalize()
        product_spices = PoductDetails.objects.filter(name__contains = key, category = 'spices')
    context = {
        'product_spices':product_spices,
        'product':product,
    }
    return render(request, 'spices.html', context )


def house_page(request):
    product = PoductDetails.objects.all()
    product_house = PoductDetails.objects.filter(category = 'houseware')
    if request.method == "POST":
        key = request.POST.get('keyword').capitalize()
        product_house= PoductDetails.objects.filter(name__contains = key, category = 'houseware')
    context = {
        'product_house':product_house,
        'product':product,
    }
    return render(request, 'house.html', context )



def school_page(request):
    product = PoductDetails.objects.all()
    product_school = PoductDetails.objects.filter(category = 'school')
    if request.method == "POST":
        key = request.POST.get('keyword').capitalize()
        product_school= PoductDetails.objects.filter(name__contains = key, category = 'school')
    context = {
        'product_school':product_school,
        'product':product,
    }
    return render(request, 'school.html', context )

def packagedfood_page(request):
    product = PoductDetails.objects.all()
    product_packagedfood = PoductDetails.objects.filter(category = 'packagedfood')
    if request.method == "POST":
        key = request.POST.get('keyword').capitalize()
        product_pantry = PoductDetails.objects.filter(name__contains = key, category = 'packagedfood')
    context = {
        'product_packagedfood':product_packagedfood,
        'product':product,
    }
    return render(request, 'packagedfood.html', context )

def beverges_page(request):
    product = PoductDetails.objects.all()
    product_beverges = PoductDetails.objects.filter(category = 'beverges')
    if request.method == "POST":
        key = request.POST.get('keyword').capitalize()
        product_beverges = PoductDetails.objects.filter(name__contains = key, category = 'beverges')
    context = {
        'product_beverges':product_beverges,
        'product':product,
    }
    return render(request, 'beverges.html', context )

def cleaning_page(request):
    product = PoductDetails.objects.all()
    product_cleaning = PoductDetails.objects.filter(category = 'cleaning')
    if request.method == "POST":
        key = request.POST.get('keyword').capitalize()
        product_pantry = PoductDetails.objects.filter(name__contains = key, category = 'cleaning')
    context = {
        'product_cleaning':product_cleaning,'product':product,
    }
    return render(request, 'cleaning.html', context )

def personalcare_page(request):
    product = PoductDetails.objects.all()
    product_personalcare = PoductDetails.objects.filter(category = 'personalcare')
    if request.method == "POST":
        key = request.POST.get('keyword').capitalize()
        product_pantry = PoductDetails.objects.filter(name__contains = key, category = 'personalcare')
    context = {
        'product_personalcare':product_personalcare,
        'product':product,
    }
    return render(request, 'personalcare.html', context )

def pantry_page(request):

    product = PoductDetails.objects.all()
    product_pantry = PoductDetails.objects.filter(category = 'pantry')

    if request.method == 'POST':
        key = request.POST.get('keyword').capitalize()
        product_pantry = PoductDetails.objects.filter(name__contains = key, category = 'pantry')



    return render(request, 'pantry.html', context = {
        'product_pantry':product_pantry,
        'product':product,

    } )

def toy_page(request):
    product = PoductDetails.objects.all()
    product_toy = PoductDetails.objects.filter(category = 'toy')
    if request.method == "POST":
        key = request.POST.get('keyword').capitalize()
        product_stationery = PoductDetails.objects.filter(name__contains = key, category = 'toy')

    context = {
        'product_toy':product_toy,
        'product':product,
    }
    return render(request, 'toy.html', context )


def stationery_page(request):
    product = PoductDetails.objects.all()
    product_stationery = PoductDetails.objects.filter(category = 'stationery')
    if request.method == "POST":
        key = request.POST.get('keyword').capitalize()
        product_stationery = PoductDetails.objects.filter(name__contains = key, category = 'stationery')

    context = {
        'product_stationery':product_stationery,
        'product':product,
    }
    return render(request, 'stationery.html', context )

def update_account(request, id):
    user = userDetail.objects.get(user = id)
    form = accountform(instance=user)
    print(form)
    if request.method == "POST":
        form = accountform(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('/accoutn/{}'.format(id))
    context = {
        'form':form
    }
    return render(request, 'update.html', context)

def checkout(request, id):
    user = userDetail.objects.get(user = User.objects.get(id = id))
    context ={
        'user_i':user
    }
    return render(request, 'checkout.html', context);

