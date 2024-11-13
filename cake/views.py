from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Cake, Review
from .forms import ReviewForm
from .serializers import CakeSerializer
from django.shortcuts import render, get_object_or_404, redirect

@api_view(['GET'])
def cake_list(request):
    cakes = Cake.objects.all()
    serializer = CakeSerializer(cakes, many=True)
    return Response({'cakes': serializer.data})

def cake_detail_view(request, cake_id):
    cake = get_object_or_404(Cake, id=cake_id)
    reviews = cake.reviews.all()  # Obtener las reseñas relacionadas con el pastel

    # Si el usuario envía el formulario de reseña
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.cake = cake
                review.user = request.user
                review.save()
                return redirect('cake_detail', cake_id=cake.id)  # Redirigir a la misma página después de guardar
        else:
            return redirect('login')  # Redirigir al login si no está autenticado
    else:
        form = ReviewForm()  # Formulario vacío para reseñas nuevas

    return render(request, 'cake_details.html', {'cake': cake, 'reviews': reviews, 'form': form})
