from django.shortcuts import render
from datetime import datetime
import random
# Create your views here.

cake_quotes = [
    "Life is short, eat the cake first!",
    "Baking is love made visible.",
    "A balanced diet is having a piece of cake in each hand.",
    "When life gives you lemons, make lemon cake!",
    "Happiness is a slice of cake.",
    "Cake: the answer to all your problems.",
    "You can't buy happiness, but you can buy cake, and that's pretty close.",
    "Keep calm and eat cake.",
    "Every day is a good day for cake.",
    "The secret ingredient is always love... and a little bit of sugar!",
    "Cake is meant to be shared.",
    "Life is what you bake it.",
    "There's no problem that cake can't solve.",
    "If you're going to have a bad day, at least have cake.",
    "In the end, all you need is cake.",
    "The only thing better than a piece of cake is two pieces of cake."
]


def home(request):
    date = datetime.now()
    greet = "Hello, guest. "
    hour = int(date.strftime("%H"))

    if hour <12:
        greet += "Good Morning"
    elif hour<17:
        greet +="Good Afternoon"
    else: 
        greet += "Good night"
    
    day = date.weekday()

    if day == 0:
        quote = "Life is short, eat the cake first!"
    elif day == 1:
        quote = "Happiness is a slice of cake."
    elif day == 2:
        quote =  "Cake is meant to be shared."
    elif day == 3:
        quote = "In the end, all you need is cake."
    elif day == 4:
        quote = "There's no problem that cake can't solve."
    elif day == 5:
        quote = "When life gives you lemons, make lemon cake!"
    elif day == 6:
        quote = "You can't buy happiness, but you can buy cake, and that's pretty close."

    return render(request, "home.html", {"greet":greet,"quote":quote})