from django.views.generic import TemplateView


class Materials(TemplateView):
    template_name = "materials/materials.html"
    context_object_name = "materials"

class EatHealthy(TemplateView):
    template_name = "materials/eat_healthy.html"
    context_object_name = "materials"


class Excercise(TemplateView):
    template_name = "materials/excercise.html"
    context_object_name = "materials"

class MentalHealth(TemplateView):
    template_name = "materials/mental_health.html"
    context_object_name = "materials"