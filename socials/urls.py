from django.urls import path
from .views import Socials

urlpatterns = [
    path("user/<slug:pk>/", Socials.as_view(), name="profile"),
]