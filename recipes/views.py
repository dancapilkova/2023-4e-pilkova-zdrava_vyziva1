from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
from .models import Recipe
from .forms import NewRecipeForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q


class Recipes(ListView):
    template_name = "recipes/recipes.html"
    model = Recipe
    context_object_name = "recipes"
     
    def get_queryset(self, **kwargs):
        q = self.request.GET.get("query")
        if q:
            recipes = self.model.objects.filter(
                Q(title__icontains=q)
                | Q(instructions__icontains=q)
                | Q(cuisine_types__icontains=q)
                | Q(meal_type__icontains=q)
            )
        else:
            recipes = self.model.objects.all()
        return recipes

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

class Delete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Recipe
    success_url = "/recipes/"

    def test_func(self):
        return self.request.user == self.get_object().user
    
class Edit(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "recipes/edit.html"
    model = Recipe
    form_class = NewRecipeForm
    success_url = "/recipes/"

    def test_func(self):
        return self.request.user == self.get_object().user