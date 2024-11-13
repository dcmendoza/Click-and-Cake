from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Cake
from .serializers import CakeSerializer

@api_view(['GET'])
def cake_list(request):
    cakes = Cake.objects.all()
    serializer = CakeSerializer(cakes, many=True)
    return Response({'cakes': serializer.data})
