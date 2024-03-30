from django.urls import path
from .views import NewRecipe, Recipes, Detail, Delete, Edit

urlpatterns = [
    path("new/", NewRecipe.as_view(), name="new_recipe"),
    path("", Recipes.as_view(), name="recipes"),
    path("<slug:pk>/", Detail.as_view(), name="detail"),
    path("delete/<slug:pk>/", Delete.as_view(), name="delete"),
     path("edit/<slug:pk>/", Edit.as_view(), name="edit"),
]
