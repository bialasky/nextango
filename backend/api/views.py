from django.shortcuts import render
from rest_framework import viewsets
from .models import Item
from .serializers import ItemSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

class ItemViewSet(viewsets.ModelViewSet):
  queryset = Item.objects.all()
  serializer_class = ItemSerializer

@api_view(['GET'])
def api_root(request, format=None):
  data = {
      'message': "Welcome to the Django Backend API",
      'version': "1.0",
      'endpoints': {
          'admin': reverse('admin:index', request=request, format=format),
          'api': reverse('api-root', request=request, format=format),
          'items': reverse('item-list', request=request, format=format),
      }
  }
  if request.accepted_renderer.format == 'html':
      return render(request, 'api_root.html', {'data': data})
  return Response(data)