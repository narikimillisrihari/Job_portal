from django.shortcuts import render,redirect,get_object_or_404
from job.models import job_model
from job.forms import job_model_form
from django.contrib.auth.decorators import login_required
from application.models import application

# Create your views here.
@login_required
def job_creation(request):
    if request.method == 'POST':
        form = job_model_form(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            # job.posted_by = request.user
            job.posted_by = request.user.profile 
            job.save()
            return redirect('job:job_list')
    else:
        user=request.user

        form = job_model_form(initial={'posted_by': user})
    return render(request, 'job/job_form.html', {'fm': form})


@login_required
def job_list(request):
    user=request.user 
    print(user)
    print(user.id)
    id=user.id
    jobs_created=job_model.objects.filter(posted_by=id)

    obj=job_model.objects.all()
    return render(request,'job/job_list.html',{'list':jobs_created})


@login_required
def jobseeker_list(request):
    obj=job_model.objects.all()
    return render(request,'job/jobseeker_list.html',{'list':obj})


@login_required
def job_details(request,id):
    obj=get_object_or_404(job_model,pk=id)
    return render(request,'job/job_details.html',{'data':obj})


@login_required
def job_delete(request,id):
    obj=get_object_or_404(job_model,pk=id)
    obj.delete()

    return redirect('job:job_list')

def applications(request):
    user_id=request.user.id
    print(user_id)
    job_ids = job_model.objects.filter(posted_by=user_id).values_list('id', flat=True)
    print(list(job_ids))

    application_list = application.objects.filter(job__in=job_ids)
    print(application_list)
    return render(request,'job/received_applications.html',{'applications':application_list})


