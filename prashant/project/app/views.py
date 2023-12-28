from django.shortcuts import render ,redirect
from django.http import HttpResponse #add
from django.template import loader #add
from .models import User  # Import your User model or create one if not already present


from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):
    return HttpResponse('Hello Brother !!')

def register(request):
    template = loader.get_template('register.html')
    return HttpResponse(template.render())

def login(request):
    template =loader.get_template('login.html')
    return HttpResponse(template.render())



def register(request):
    if request.method == 'POST':
        # Retrieve data from the form
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmPassword')

        # Basic validation (you may want to add more validation logic)
        if password != confirm_password:
            # Passwords don't match, handle this case
            return render(request, 'registration_form.html', {'error': 'Passwords do not match'})

        # Create a new User instance and save it to the database
        new_user = User(username=username, email=email, password=password)
        new_user.save()

        # Redirect to a success page or login page
        return redirect('success')  # 'success' should be replaced with the URL name of your success page

    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Login successful
            login(request, user)
            return redirect('success')  # Replace 'success' with your desired success page URL
        else:
            # Invalid login credentials, handle this case
            return render(request, 'login.html', {'error': 'Invalid username or password'})

    return render(request, 'login.html')


