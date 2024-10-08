from datetime import datetime
from django.shortcuts import render
from django.core.cache import cache

# Create your views here.
def home_view(request):
    date = datetime.now()
    greet = "Hello"
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

    return render(request, "home.html", {"greet": greet, "quote": quote, "visit_count": visit_count})
