from django.http import HttpResponseRedirect

def IsLoggedIn(view_func):
    def new_view_func(request):
            if request.session.get('logged_in',False):
                print("LoggedIn")
                return view_func(request)
            
            else:
                return HttpResponseRedirect('/login')
    
    return new_view_func
