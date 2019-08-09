from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib import auth
from main import views as m_views



User = get_user_model()


# def load_backend(path):
#     return import_string(path)()


# def _get_backends(return_tuples=False):
#     backends = []
#     for backend_path in settings.AUTHENTICATION_BACKENDS:
#         backend = load_backend(backend_path)
#         backends.append((backend, backend_path) if return_tuples else backend)
#     if not backends:
#         raise ImproperlyConfigured(
#             'No authentication backends have been defined. Does '
#             'AUTHENTICATION_BACKENDS contain anything?'
#         )
#     return backends


# def get_backends():
#     return _get_backends(return_tuples=False)

def signin(request):
       return render(request, 'authservice/signin.html')

def login(request):
   if request.method == "POST":
         username = request.POST["username"]
         password = request.POST["password"]
         user = auth.authenticate(request, username=username, password=password)
         if user is not None:
            auth.login(request, user)
            return redirect('main:home' )
         else:
            return render(request, 'authservice/signin.html', {'error' : 'username or password is incorrect.'})
   else:
      return render(request, 'authservice/signin.html')

# def gotosignup(request):
#        return render(requst, 'authservice/signup.html')

def register(request):
       return render(request, 'authservice/signup.html')

def signup(request):
   if request.method == "POST":
      if request.POST["password1"] == request.POST["password2"]:
         try:
            user = User.objects.get(username=request.POST['username'])
            return render(request, 'authservice/signup.html', {'error': 'Username has already been taken'})
         except User.DoesNotExist:
            username=""
            password1=""
            user = User.objects.create_user(
               request.POST['username'], password=request.POST['password1'],  email=request.POST["email"])
            auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('main:home')
      else:
         return render(request, 'authservice/signup.html', {'error': 'Passwords must match'})
   else:
      # User wants to enter info
      return render(request, 'authservice/signup.html')

   #       username=""
   #       password1=""
   #       user = User.objects.create_user(username = request.POST["username"], password=request.POST["password1"], email=request.POST["email"])
   #       user = auth.authenticate(username=username, password=password1)
   #       auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
   #       return redirect('main:home', {'username' : username})
   # return render(request, 'authservice/signup.html')


def index(request):
   return render(request, 'index.html')

def logout(request):
   auth.logout(request)
   return redirect('authservice:signin')

# def logout(request):
#    absuth.logout(request):
#    return redirect('signin')