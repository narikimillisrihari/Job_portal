# registration/views.py

from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from user.models import Profile
from .forms import UserForm, ProfileForm

def signup(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            username = user_form.cleaned_data['username']
            email = user_form.cleaned_data['email']
            password = user_form.cleaned_data['password']
            is_employee = profile_form.cleaned_data['is_employee']
            is_job_seeker = profile_form.cleaned_data['is_job_seeker']

            if User.objects.filter(username=username).exists():
                return render(request, 'signup.html', {'error': 'Username already exists.', 'user_form': user_form, 'profile_form': profile_form})

            user = User.objects.create_user(username=username, email=email, password=password)
            profile = Profile.objects.create(user=user, is_employee=is_employee, is_job_seeker=is_job_seeker)
            login(request, user)
            return redirect('user:login')  
    else:
        user_form = UserForm()
        profile_form = ProfileForm()

    return render(request, 'user/signup.html', {'user_form': user_form, 'profile_form': profile_form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        profile = Profile.objects.get(user=user)
        print(user)
        print(user.password)
        if user is not None:
                login(request, user)
                next_page = request.GET.get('next')
                if profile.is_employee==True:
                    return redirect('user:empdashboard')
                else:
                    return redirect('user:jobdashboard')

        else:
            return render(request, 'user/login.html', {'error': 'Invalid username or password.'})
    else:
        return render(request, 'user/login.html', {})
@login_required
def empdashboard(request):
    user = request.user
    return render(request,'user/employee_dashboard.html',{'user':user})

@login_required
def jobdashboard(request):
    user = request.user
    return render(request,'user/jobseeker_dashboard.html',{'user':user})


@login_required
def home(request):
    user = request.user
    try:
        profile = Profile.objects.get(user=user)
    except Profile.DoesNotExist:
        profile = None  # Handle the case where no profile exists
    
    context = {
        'user': user,
        'profile': profile,
    }
    return render(request, 'user/home.html', context)

@login_required
def list(request):
    obj = Profile.objects.all()
    return render(request, 'user/sample.html', {'obj': obj})

@login_required
def delete_user(request, id):
    item = get_object_or_404(Profile, id=id)
    item.user.delete()  # This will delete the user and the associated profile
    print("item is deleted")
    return redirect('user:list')

@login_required
def logout_view(request):
    logout(request)
    return redirect('user:login')
