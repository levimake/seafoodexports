from django.shortcuts import redirect
from .forms import LoginForm

def IsLoggedIn(view_func):
    def new_view_func(request):
            if request.session.get('logged_in',False):
                return view_func(request)
            else:
                form = LoginForm()
                return redirect('/login', {'form': form})
    return new_view_func
