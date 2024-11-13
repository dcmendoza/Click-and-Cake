from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import RegisterForm
from .models import Cart
from cake.models import Cake
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.urls import reverse

# Create your views here
def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Extract cleaned data
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            # Create user and hash the password
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name
            )
            # Authenticate the user and log them in
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to home after successful registration
                return redirect('home')
            else:
                messages.error(request, 'Authentication failed after registration.')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = RegisterForm()
    return render(request, 'account/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Extract username and password from the form
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            # Authenticate the user
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)  # Log the user in
                return redirect('home')  # Redirect to home after login
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid login credentials. Please try again.")
    else:
        form = AuthenticationForm()

    return render(request, 'account/login.html', {'form': form})

def logout_view(request):
    logout(request)  # Cierra la sesión del usuario
    messages.success(request, "You have successfully logged out.")
    return redirect('login')  # Redirige a la página de inicio

@login_required
def cart_view(request):
    # Obtener el carrito del usuario actual
    cart = get_object_or_404(Cart, user=request.user)

    # Obtener los detalles de cada pastel en el carrito
    items = []
    for cake_id_str, quantity in cart.cake_quantities.items():
        try:
            cake = Cake.objects.get(id=int(cake_id_str))
            items.append({
                'cake': cake,
                'quantity': quantity,
                'total_price': cake.price * quantity
            })
        except Cake.DoesNotExist:
            pass  # Ignorar si el pastel no existe

    # Calcular el precio total del carrito
    total_price = sum(item['total_price'] for item in items)

    return render(request, 'account/cart.html', {
            'items': items,
            'total_price': total_price,
            'update_cart_item_url': reverse('update_cart_item'),
            'remove_from_cart_url': reverse('remove_from_cart')
        })

@require_POST
@login_required
def update_cart_item(request):
    cart = get_object_or_404(Cart, user=request.user)
    cake_id = request.POST.get('cake_id')
    quantity = int(request.POST.get('quantity', 1))

    # Validar que la cantidad sea positiva
    if quantity < 1:
        return JsonResponse({'success': False, 'message': 'Quantity must be at least 1.'}, status=400)

    # Actualizar la cantidad del artículo en el carrito
    if str(cake_id) in cart.cake_quantities:
        cart.cake_quantities[str(cake_id)] = quantity
        cart.save()
        return JsonResponse({'success': True, 'message': 'Quantity updated successfully.'})
    else:
        return JsonResponse({'success': False, 'message': 'Item not in cart.'}, status=404)
    
@require_POST
@login_required
def remove_from_cart(request):
    cart = get_object_or_404(Cart, user=request.user)
    cake_id = request.POST.get('cake_id')

    # Eliminar el artículo si está en el carrito
    if str(cake_id) in cart.cake_quantities:
        del cart.cake_quantities[str(cake_id)]
        cart.save()
        return JsonResponse({'success': True, 'message': 'Item removed from cart.'})
    else:
        return JsonResponse({'success': False, 'message': 'Item not in cart.'}, status=404)