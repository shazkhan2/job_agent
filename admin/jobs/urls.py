from django.urls import path
from .views import JobListingList

urlpatterns = [
    path('job-listings/', JobListingList.as_view(), name='job-list'),
]