from django.views.generic import CreateView
from .models import Recipe
from .forms import NewRecipeForm

class NewRecipe(CreateView):
    template_name = "recipes/new_recipe.html"
    model = Recipe
    form = NewRecipeForm
    success_url = "/recipes/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(NewRecipe, self).form_valid(form)
