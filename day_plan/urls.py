from django.urls import path
from .views import DayPlan, NewMeal, GetMeal


urlpatterns = [
    path("", DayPlan.as_view(), name="day_plan"),
    path(
        "create_plan/<str:meal_date>/<str:meal_type>/",
        GetMeal.as_view(),
        name="get_meals",
    ),
    path(
        "create_recipe/<str:meal_date>/<str:meal_type>/<int:pk>/",
        NewMeal.as_view(),
        name="new_meal",
    ),
  
]