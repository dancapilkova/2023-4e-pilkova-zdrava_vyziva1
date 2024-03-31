import datetime
import calendar
from django_reorder.reorder import reorder
from django.views.generic import TemplateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q
from .models import Meal
from recipes.models import Recipe
import random


class DayPlan(LoginRequiredMixin, TemplateView):
    template_name = "day_plan/day_plan.html"

    def get_context_data(self, **kwargs):
        today = datetime.date.today()
        days_in_mon = calendar.monthrange(today.year, today.month)[1]

        days = [
            datetime.date(today.year, today.month, day)
            for day in range(1, days_in_mon + 1)
        ]

        meals = Meal.objects.filter(
            user=self.request.user, meal_date__in=days
        ).order_by(reorder(meal_type=["breakfast", "snack", "lunch", "snack", "dinner"]))

        context = {"days": days, "meals": meals}

        return context
