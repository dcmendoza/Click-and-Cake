from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from cake.models import Cake  # Importa el modelo Cake desde la app 'cake'
from order.models import Order  # Importa el modelo Order desde la app 'order'
from .forms import CakeForm, OrderForm, UserForm 
from django.http import JsonResponse

# Create your views here.

# Vista principal del dashboard que renderiza el archivo HTML único
def dashboard_home(request):
    return render(request, 'dashboard.html')

# Vista para listar los objetos de un modelo específico
def model_list(request, model_name):
    model_map = {
        'cakes': Cake,
        'orders': Order,
        'users': User,
    }
    model_class = model_map.get(model_name)

    if model_class is None:
        return JsonResponse({'error': 'Modelo no encontrado'}, status=404)

    objects = model_class.objects.all()
    return render(request, 'partials/model_list.html', {'model_name': model_name, 'objects': objects})

# Vista para mostrar o editar un objeto específico
from .forms import CakeForm, OrderForm, UserForm  # Asegúrate de importar el formulario de usuario

def model_detail(request, model_name, object_id):
    model_map = {
        'cakes': Cake,
        'orders': Order,
        'users': User,
    }
    model_class = model_map.get(model_name)
    if not model_class:
        return JsonResponse({'error': 'Modelo no encontrado'}, status=404)

    obj = get_object_or_404(model_class, id=object_id)

    # Selección de formulario
    if model_name == 'cakes':
        form = CakeForm(request.POST or None, request.FILES or None, instance=obj)
    elif model_name == 'orders':
        form = OrderForm(request.POST or None, instance=obj)
    elif model_name == 'users':
        form = UserForm(request.POST or None, instance=obj)
    else:
        form = None

    if request.method == 'POST' and form and form.is_valid():
        form.save()
        return JsonResponse({'success': True})

    # Renderizamos el formulario o el detalle del objeto en HTML
    return render(request, 'partials/model_detail.html', {
        'model_name': model_name,
        'obj': obj,
        'form': form
    })

# Vista para crear un nuevo objeto
def create_object(request, model_name):
    form = None
    if model_name == 'cakes':
        form = CakeForm(request.POST or None, request.FILES or None)
    elif model_name == 'orders':
        form = OrderForm(request.POST or None)
    elif model_name == 'users':
        form = UserForm(request.POST or None)

    if request.method == 'POST' and form and form.is_valid():
        form.save()
        return JsonResponse({'success': True})
    elif request.method == 'POST':
        return JsonResponse({'success': False, 'errors': form.errors}, status=400)

    return render(request, 'partials/create_object.html', {
        'model_name': model_name,
        'form': form
    })
