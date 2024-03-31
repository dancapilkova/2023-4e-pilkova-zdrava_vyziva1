from django.urls import path
from .views import Socials, EditProfile

urlpatterns = [
    path("user/<slug:pk>/", Socials.as_view(), name="profile"),
    path("edit/<slug:pk>/", EditProfile.as_view(), name="edit_profile"),
]