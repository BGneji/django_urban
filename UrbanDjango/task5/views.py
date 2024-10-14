from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import logout, login
from task5.forms import UserRegister


class User_Register(TemplateView):
    template_name = 'fifth_task/registration_page.html'

    def get(self, request):
        form = UserRegister()
        return render(request, self.template_name, {'form': form, 'title': 'Страница регистрации'})

    def post(self, request):
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            a = sign_up_by_django(username, password)
            if a:
                username = f'такой пользователь уже существует'
                return render(request, self.template_name, {'form': form, 'username': username})
            else:
                username = f'Приветствуем, {username}'
                return render(request, self.template_name, {'form': form, 'username': username})

        return render(request, self.template_name, {'form': form, 'title': 'Страница регистрации'})


dict_user = {'qwe': 12345678}


def sign_up_by_django(username, password):
    if username in dict_user:
        new_user = True
        return new_user
    else:
        dict_user[username] = password
        new_user = False
        return new_user
