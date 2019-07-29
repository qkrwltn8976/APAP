from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib import auth

User = get_user_model()


def load_backend(path):
    return import_string(path)()


def _get_backends(return_tuples=False):
    backends = []
    for backend_path in settings.AUTHENTICATION_BACKENDS:
        backend = load_backend(backend_path)
        backends.append((backend, backend_path) if return_tuples else backend)
    if not backends:
        raise ImproperlyConfigured(
            'No authentication backends have been defined. Does '
            'AUTHENTICATION_BACKENDS contain anything?'
        )
    return backends


def get_backends():
    return _get_backends(return_tuples=False)

def signin(request):
	if request.method == "POST":
			username = request.POST["username"]
			password = request.POST["password"]
			user = auth.authenticate(request, username=username, password=password)
			if user is not None:
				auth.login(request, user)
				return redirect('home')
			else:
				return render(request, 'authservice/signin.html', {'error' : 'incorrect'})
	else:
		return render(request, 'authservice/signin.html')


def signup(request):
	if request.method == "POST":
		if request.POST["password1"] == request.POST["password2"]:
			user = User.objects.create_user(
			username=request.POST["username"], password=request.POST["password1"])
			auth.login(request, user)
			return redirect('home')
	return render(request, 'authservice/signup.html')


def index(request):
	return render(request, 'index.html')


# def logout(request):
# 	absuth.logout(request):
# 	return redirect('signin')
