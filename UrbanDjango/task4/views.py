from django.shortcuts import render
from django.views.generic import TemplateView


class Main_platform(TemplateView):
    template_name = 'fourth_task/platform.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context


class Games_Class(TemplateView):
    template_name = 'fourth_task/games.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Игры'
        context['games'] = ["Atomic Heart", "Cyberpunk 2077", "PayDay 2"]
        context['asd'] = 'cart'
        return context


class Cart_Class(TemplateView):
    template_name = 'fourth_task/cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Корзина'
        context['cart_content'] = "Извините корзина пуста"
        return context