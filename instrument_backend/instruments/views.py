from django.shortcuts import render

# Create your views here.
from .models import Instrument
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import InstrumentSerializer


class InstrumentViewSet(viewsets.ModelViewSet):
    ## The Main Query for the index route
    queryset = Instrument.objects.all()
    # The serializer class for serializing output
    serializer_class = InstrumentSerializer
    # optional permission class set permission level
    permission_classes = [permissions.AllowAny] #Coule be [permissions.IsAuthenticated]