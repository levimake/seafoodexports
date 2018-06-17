from django.shortcuts import render
from .forms import LoginForm

def IsLoggedIn(view_func):
    def new_view_func(request):
            if request.session.get('logged_in',False):
                return view_func(request)
            else:
                form = LoginForm()
                return render(request, 'login', {'form': form})
    return new_view_func
