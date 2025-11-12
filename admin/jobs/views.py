from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import JobListing
from .serializers import JobListingSerializer

class JobListingList(generics.ListAPIView):
    queryset = JobListing.objects.all()
    serializer_class = JobListingSerializer