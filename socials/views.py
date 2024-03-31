from django.views.generic import TemplateView
from .models import Profile

class Socials(TemplateView):
    template_name = "socials/profile.html"

    def get_context_data(self, **kwargs):
        profile = Profile.objects.get(user=self.kwargs["pk"])
        context = {
            "profile": profile,
        }

        return context

