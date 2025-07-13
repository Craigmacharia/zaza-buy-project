from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ProductForm
from .models import Product, Sale


# ------------------------------
# Authentication
# ------------------------------
def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')


# ------------------------------
# Dashboard
# ------------------------------
@login_required(login_url='/')
def dashboard(request):
    return render(request, 'dashboard.html')


# ------------------------------
# Product CRUD
# ------------------------------
@login_required(login_url='/')
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Product added successfully.")
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})


@login_required(login_url='/')
def product_list(request):
    products = Product.objects.all().order_by('-created_at')
    return render(request, 'admin/view_products.html', {'products': products})


@login_required(login_url='/')
def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Product updated successfully.")
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'edit_product.html', {'form': form, 'product': product})


@login_required(login_url='/')
def view_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'view_product.html', {'product': product})



@login_required(login_url='/')
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        messages.success(request, "Product deleted successfully.")
        return redirect('product_list')
    return render(request, 'delete_product.html', {'product': product})


# ------------------------------
# Sales View
# ------------------------------
@login_required(login_url='/')
def view_sales(request):
    sales = Sale.objects.all().order_by('-created_at')
    return render(request, 'view_sales.html', {'sales': sales})


@login_required(login_url='/')
def product_list(request):
    products = Product.objects.all().order_by('-created_at')
    return render(request, 'view_products.html', {'products': products})


