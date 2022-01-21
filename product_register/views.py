from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from .forms import ProductForm, LoginForm
from .models import Product
from .services import send_notification, save_actions, disable_form_if_needed, send_email

# Create your views here.


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/product/list')
            else:
                msg = 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})


def list(request):
    if not request.user.is_authenticated:
        return redirect('/')
    else:
        context = {'product_list': Product.objects.all()}
        return render(request, "list.html", context)


def form(request, id=0):
    user = request.user
    if not user.is_authenticated:
        return redirect('/')
    else:
        if request.method == "GET":
            if id == 0:
                form = ProductForm()
            else:
                product = Product.objects.get(pk=id)
                form = ProductForm(instance=product)
                # in case is anonymous users
                if not user.is_superuser:
                    save_actions('read', product.id, user.id)
                    disable_form_if_needed(form, user)

            return render(request, "form.html", {'form': form})
        else:
            if id == 0:
                form = ProductForm(request.POST)
            else:
                product = Product.objects.get(pk=id)
                form = ProductForm(request.POST, instance=product)
                send_email(user, product, form)
                send_notification('update', user, product)
            if form.is_valid:
                form.save()
            return redirect('/product/list')


def delete(request, id):
    if not request.user.is_authenticated:
        return redirect('/')
    else:
        product = Product.objects.get(pk=id)
        save_actions('delete', product.id, request.user.id)
        product.delete()
        return redirect('/product/list')
