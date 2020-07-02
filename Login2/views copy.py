from django.shortcuts import redirect, render
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth import logout
from django.views.generic import View

class LoginClass(View):
    templates = 'login/login.html'
    template_ok = 'Dashboard/dashboard.html'
    message = ""
    
    def get(self, request, *arg, **kargs):
        if request.user.is_authenticated:
            next_url =request.GET.get('next')
            if next_url:
                return redirect(next_url)
            else:
                return redirect('Dashboard:Dashboard')
        return render(request,self.templates,{})
    
    def post(self, request, *arg, **kargs):
        user_post = request.POST['user']
        passw_post = request.POST['pass']
        user_session = authenticate(username = user_post, password = passw_post)
        #validacion
        if user_session is not None:
            print(user_session) #fue verdadero
            login_django(request, user_session) #metodo raro que arruina todo :c
            print("line 30")
            next_url = request.GET.get('next')#tambien raro pero obtiene un valor
            if next_url:
                print("line 33") #algo verdadero
                return redirect(next_url)
            else:
                print("line 36")#no fue verdadero pero va dashboard
                return redirect('Dashboard:Dashboard')
        else:
            self.message = 'Usuario o contraseña incorrecto'
        return render(request, self.templates, self.get_contex()) 

    def get_contex(self):
        return {
            'error':self.message,
        } 

class l(View):
    def get(self, request, *arg, **kargs):
        print("l line 50")
        logout(request)
        return redirect('Login2:Login2')
