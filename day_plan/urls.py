from django.urls import path
from .views import DayPlan


urlpatterns = [
    path("", DayPlan.as_view(), name="day_plan"),
  
]