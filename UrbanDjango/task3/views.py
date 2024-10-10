from django.shortcuts import render
from django.views.generic import TemplateView


class Main_platform(TemplateView):
    template_name = 'third_task/platform.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['href_games'] = 'games'
        context['href_cart'] = 'cart'
        return context


class Games_Class(TemplateView):
    template_name = 'third_task/games.html'


class Cart_Class(TemplateView):
    template_name = 'third_task/cart.html'
