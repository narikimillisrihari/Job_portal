from django.shortcuts import render,get_object_or_404,redirect
from application.models import application
from application.forms import application_form
from job.models import job_model
from django.contrib.auth.models import User



# Create your views here.
def apply(request,id):
    if request.method == 'POST':
        form = application_form(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            # job.posted_by = request.user
            application.name = request.user.profile 
            application.email = request.user.email
            application.job=get_object_or_404(job_model,pk=id)
            application.save()
            return redirect('application:status')
    else:
        name=request.user
        email=name.email
        job=get_object_or_404(job_model,pk=id)
        form = application_form(initial={'name': name,'email':email,'job':job})

    return render(request,'application/apply.html',{'form':form})

def status(request):
    email=request.user.email
    print(email)
    obj=application.objects.filter(email=email)


    return render(request,'application/status.html',{'obj':obj})


def update_application_status(request, id):
    print(id)
    if request.method == 'POST':
        applications = get_object_or_404(application, id=id)
        new_status = request.POST.get('status')
        if new_status in ['applied', 'shortlisted', 'selected','reject']:
            applications.progress = new_status
            applications.save()
    return redirect('user:empdashboard')