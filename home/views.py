import json
from datetime import datetime
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from account.models import Cart
from django.shortcuts import render
from django.core.cache import cache
import requests
from django.http import HttpResponse
from cake.models import Cake
from .report_generator import ExcelReportGenerator, PDFReportGenerator

# Create your views here.
def home_view(request):
    date = datetime.now()
    user = request.user

    # Verificar si el usuario está autenticado y tiene un primer nombre
    if user.is_authenticated and user.first_name:
        greet = f"Hello {user.first_name}, "
    else:
        greet = "Hello, "

    # Obtener la hora actual y el mensaje correspondiente
    hour = int(date.strftime("%H"))
    if hour < 12:
        greet += "Good Morning!"
    elif hour < 17:
        greet += "Good Afternoon!"
    else:
        greet += "Good Night!"

    # Diccionario para asignar una cita diaria
    quotes = {
        0: "Life is short, eat the cake first!",
        1: "Happiness is a slice of cake.",
        2: "Cake is meant to be shared.",
        3: "In the end, all you need is cake.",
        4: "There's no problem that cake can't solve.",
        5: "When life gives you lemons, make lemon cake!",
        6: "You can't buy happiness, but you can buy cake, and that's pretty close.",
    }

    # Obtener la cita correspondiente al día de la semana
    day = date.weekday()
    quote = quotes.get(day, "Enjoy your day with a slice of cake!")  # Default por si acaso

    visit_count = cache.get('visit_count', 0)  # Obtener el valor actual del caché
    visit_count += 1  # Incrementar el contador
    cache.set('visit_count', visit_count, timeout=None)

    #API para saber el clima de medellín

    city = 'Medellin'

    apikey = '9d0c4174e8fb1086e926aceb76b4deca'
    URL = 'https://api.openweathermap.org/data/2.5/weather'
    params ={'q':city,'appid': apikey, 'units':'metric'}
    r = requests.get(url=URL, params=params)
    res = r.json() 
    icon = res['weather'][0]['icon']
    temp = res['main']['temp']
    country = res['sys']['country']

    return render(request, "home.html", {"greet": greet, "quote": quote, "visit_count": visit_count,'icon': icon,'temp': temp,'country': country,'city':city})

def menu_view(request):
    cakes = Cake.objects.all()  # Obtenemos todos los objetos Cake de la base de datos
    return render(request, 'menu.html', {'cakes': cakes})

def generate_report(request, report_type):
    # Obtener todos los productos
    products = Cake.objects.all()
    
    if report_type == 'excel':
        report_generator = ExcelReportGenerator()
    elif report_type == 'pdf':
        report_generator = PDFReportGenerator()
    else:
        return HttpResponse("Tipo de reporte no soportado.", status=400)
    
    # Generar el reporte
    report = report_generator.generate_report(products)
    
    # Preparar la respuesta para la descarga
    if report_type == 'excel':
        response = HttpResponse(report, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=productos.xlsx'
    elif report_type == 'pdf':
        response = HttpResponse(report, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename=productos.pdf'
    return response

@require_POST
@login_required  # Asegúrate de que el usuario esté autenticado
def add_to_cart(request):
    try:
        data = json.loads(request.body)  # Decodifica el JSON del cuerpo de la solicitud
        cake_id = data.get('cake_id')  # Obtén el `cake_id` del JSON
        quantity = data.get('quantity', 1)  # Obtén la cantidad, predeterminada a 1
        print("Cake ID:", cake_id)  # Para verificar si se está recibiendo correctamente

        # Verificar que el pastel existe
        try:
            cake = Cake.objects.get(id=cake_id)
        except Cake.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Cake not found.'}, status=404)

        # Obtener o crear el carrito asociado al usuario
        cart, created = Cart.objects.get_or_create(user=request.user)

        # Agregar el pastel al carrito
        cart.add_cake(cake_id, quantity)

        return JsonResponse({'success': True, 'message': 'Cake added to cart successfully.'})
    
    except json.JSONDecodeError:
        return JsonResponse({'success': False, 'message': 'Invalid JSON format.'}, status=400)
