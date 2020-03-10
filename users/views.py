from django.shortcuts import render, redirect

from .forms import RegisterForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            return redirect('/login/')
    else:
        user_form = RegisterForm()

    return render(request, 'registration/register.html', {'user_form':user_form})

# def login(request):
#     user_form = RegisterForm()
#     return render(request, 'registration/login.html', {'user_form':user_form})

def index(request):
    return render(request, 'blogs/index.html', {'email': request.session.get('user')})