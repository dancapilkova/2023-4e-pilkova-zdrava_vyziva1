from django.views.generic import CreateView, ListView, DetailView
from .models import Recipe
from .forms import NewRecipeForm
from django.contrib.auth.mixins import LoginRequiredMixin


class Recipes(ListView):
    template_name = "recipes/recipes.html"
    model = Recipe
    context_object_name = "recipes"

class Detail(DetailView):
    template_name = "recipes/detail.html"
    model = Recipe
    context_object_name = "recipe"

class NewRecipe(LoginRequiredMixin, CreateView):
    template_name = "recipes/new_recipe.html"
    model = Recipe
    form_class = NewRecipeForm
    success_url = "/recipes/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(NewRecipe, self).form_valid(form)

