from django.urls import path
from .views import EatHealthy, Excercise, MentalHealth, Materials


urlpatterns = [
    path("", Materials.as_view(), name="materials"),
    path("healthyeating/", EatHealthy.as_view(), name="eat_healthy"),
    path("excercise/", Excercise.as_view(), name="excercise"),
    path("mentalhealth/", MentalHealth.as_view(), name="mental_health"),
    
    ]