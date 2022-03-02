from logging import exception
from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib import messages
from . models import Category2,JobApplied, JobApply, Job2, Company, Certificate, Contact, Curriculum, Service, StudentUser, Recruiter, AddJob
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from datetime import date

# Create your views here.


def index(request):
    service = Service.objects.all
    s = Service.objects.order_by('-name')[1:5]
    company = Company.objects.all
    certificate = Certificate.objects.all
    catt = Category2.objects.order_by('-id')[0:6]
    job2 = Job2.objects.order_by('-id')[0:4]
    data = {
        'category': category,
        'job': job2,
        'catt': catt,
        'company': company,
        'certificate': certificate,
        'service': service,
        's': s
    }
    return render(request, 'index.html', data)


def about(request):
    service = Service.objects.all
    company = Company.objects.all
    data = {

        'company': company,
        'service': service

    }
    return render(request, 'about.html', data)


def service_detail(request, slug):

    company = Company.objects.all
    service = Service.objects.all
    services = Service.objects.filter(slug=slug)
    data = {

        'service': service,
        'company': company,
        'services': services,


    }
    return render(request, 'service.html', data)


def category(request, slug):
    service = Service.objects.all

    job2 = Job2.objects.filter(slug=slug)
    data = {

        'job': job2,
        'service': service
    }

    return render(request, 'category.html', data)


def detail(request, slug):
    job2 = Job2.objects.order_by('-id')[0:4]
    company = Company.objects.filter(slug=slug)
    service = Service.objects.all

    data = {
        'company': company,
        'job': job2,
        'service': service
    }
    return render(request, 'company-details.html', data)


# def category(request,id):
#     jobs=Job.objects.filter(id=id)
#     data={

#         'jobs':jobs
#     }

#     return render(request,'category.html',data)


def job_oppening(request):
    service = Service.objects.all
    job = AddJob.objects.all
    user=request.user
    student=StudentUser.objects.get(user=user)
    apply=JobApplied.objects.filter(student=student)
    li=[]
    for i in apply:
        li.append(i.job.id)

    context = {
        'job': job,
        'service': service,
        'li':li
    }

    return render(request, 'current_job_openning.html', context)

# not use
def apply(request):
    service = Service.objects.all
    data = {

        'service': service
    }
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        city = request.POST.get('city')
        field = request.POST.get('field')
        exp = request.POST.get('exp')
        resume = request.FILES['resume']
        

        apply = JobApply(name=name, email=email, phone=phone, address=address,
                         city=city, criteria=field, exp=exp, resume=resume)
        apply.save()
        # messages.info(request,"Applied Successfully")
        # return redirect('/')

        subject = name
        message = name
        email_from = settings.EMAIL_HOST_USER
        try:
            send_mail(subject, message, email_from, [
                      'poojachauhan2102@gmail.com'])
            apply.save()
            messages.info(request, "Applied Successfully")
            return redirect('apply')

        except Exception as e:
            return redirect("apply")

    return render(request, 'apply.html', data)


def contact(request):
    service = Service.objects.all
    data = {

        'service': service
    }
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        address = request.POST.get('address', '')

        print(name)

        contact = Contact(name=name, email=email, phone=phone,
                          desc=desc, address=address)

        subject = name
        message = desc
        email_from = settings.EMAIL_HOST_USER
        try:
            send_mail(subject, message, email_from, [
                      'poojachauhan2102@gmail.com'])
            contact.save()
            messages.info(request, "Message Sent Successfully")
            return redirect('/')

        except Exception as e:
            return redirect('contact')

    return render(request, 'contact.html', data)

# not use
def userlogin(request):
    service = Service.objects.all
    data = {

        'service': service
    }
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)

            messages.success(request, 'Successfully logged In')
            return redirect("/")

        else:
            messages.error(request, 'User not Signup')
            return redirect('userlogin')

    return render(request, 'userlogin.html', data)

# not use
def signup(request):
    service = Service.objects.all
    data = {

        'service': service
    }
    if request.method == "POST":
        username = request.POST.get('username')

        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        if User.objects.filter(email=email).exists():
            messages.info(request, "Email already taken")
            return redirect("registration")

        if not username.isalnum():
            messages.error(
                request, "Username should only contain letters and numbers")
            return redirect("signup")

        if pass1 != pass2:
            messages.error(request, "Password do not matched")
            return redirect("signup")

        myuser = User.objects.create_user(username, email, pass1)

        myuser.save()

        messages.success(request, "User Created")
        return redirect("signup")

    else:

        return render(request, 'signup.html', data)


def userlogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/')


def resume(request):
    catt = Category2.objects.all
    service = Service.objects.all
    data = {
        'catt': catt,
        'service': service
    }
    if request.method == 'POST':
        name = request.POST.get('name', '')
        gender = request.POST.get('gender', '')
        address = request.POST.get('address', '')
        phone = request.POST.get('phone', '')
        resume = request.FILES['resume']
        carrier = request.POST.get('carrier', '')
        email = request.POST.get('email', '')
        salary = request.POST.get('salary', '')
        exp = request.POST.get('exp', '')

        desc = request.POST.get('desc', '')

        print(resume)

        curriculum = Curriculum(name=name, gender=gender, address=address, phone=phone,
                                resume=resume, carrier=carrier, email=email, salary=salary, exp=exp, desc=desc)
        curriculum.save()
        messages.info(request, "Successfully Submiited")
        return redirect('user_home')

    return render(request, 'resume.html', data)


def view_users(request):
    user = StudentUser.objects.all()
    context = {'user': user}
    return render(request, 'view_users.html', context)


def view_recruiters(request):
    user = Recruiter.objects.all()
    context = {'user': user}
    return render(request, 'view_recruiters.html', context)


def delete_user(request, user):
    student = User.objects.get(username=user)
    student.delete()
    return redirect('view_users')


def delete_recruiter(request, user):
    recruiter = User.objects.get(username=user)
    recruiter.delete()
    return redirect('view_recruiters')


def recruiter_accept(request):
    user = Recruiter.objects.filter(status='Accept')
    context = {'user': user}
    return render(request, 'recruiter_accept.html', context)


def recruiter_reject(request):
    user = Recruiter.objects.filter(status='Reject')
    context = {'user': user}
    return render(request, 'recruiter_reject.html', context)


def recruiter_pending(request):
    user = Recruiter.objects.filter(status='pending')
    context = {'user': user}
    return render(request, 'recruiter_pending.html', context)


def change_status(request, id):
    recruiter = Recruiter.objects.get(id=id)
    if request.method == "POST":
        s = request.POST['status']
        recruiter.status = s

        if recruiter.status == "Accept":
            recruiter.save()
            messages.info(request, 'Request Accept Successfully')
            return redirect('recruiter_pending')

        if recruiter.status == "Reject":
            recruiter.save()
            messages.info(request, 'Request Reject Successfully')
            return redirect('recruiter_pending')

        else:
            messages.info(request, 'Request Rejected')
            return render(request, 'change_status.html')

    context = {'recruiter': recruiter}
    return render(request, 'change_status.html', context)


def admin_home(request):
    return render(request, 'admin_home.html')


def admin_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user.is_staff:
            login(request, user)
            messages.info(request, 'successfully Admin Login')
            return redirect('admin_home')
            # return render(request,'admin_home.html')

        else:
            messages.info(request, 'This is not Admin')
            return redirect('admin_login')

    return render(request, 'admin_login.html')


def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user:
            try:
                user1 = StudentUser.objects.get(user=user)
                if user1.type == "student":
                    login(request, user)
                    messages.success(request, 'Successfully logged In')
                    return redirect("user_home")
                    # return render(request,"user/user_home.html")

                else:
                    messages.info(request, 'This is not Student User')
                    return redirect('user_signup')
            except:
                messages.info(request, 'Invalid StudentUser')

        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('user_signup')
    return render(request, 'user_login.html')


def recruiter_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user:
            try:
                user1 = Recruiter.objects.get(user=user)
                if user1.type == "recruiter" and user1.status == "pending":
                    login(request, user)
                    messages.success(request, 'Successfully logged In')
                    return redirect("recruiter_home")

                else:
                    messages.info(request, 'This is not Recruiter')
                    return redirect('recruiter_signup')
            except:
                messages.info(request, 'Invalid Recruiter')

        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('recruiter_signup')

    return render(request, 'recruiter_login.html')


def recruiter_signup(request):
    if request.method == "POST":
        name = request.POST['name']
        company = request.POST['company']
        email = request.POST['email']
        phone = request.POST['phone']
        gender = request.POST['gender']
        image = request.FILES['image']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(email=email).exists():
            messages.info(request, "Email already taken")
            return redirect("recruiter_signup")

        if pass1 != pass2:
            messages.info(request, "Password do not matched")
            return redirect("recruiter_signup")

        user = User.objects.create_user(
            username=name, email=email, password=pass1)
        Recruiter.objects.create(user=user, company=company, mobile=phone,
                                 image=image, gender=gender, type="recruiter", status="pending")

        messages.success(request, "Recruiter Created")
        return redirect("recruiter_login")

    return render(request, 'recruiter_signup.html')


def user_signup(request):
    if request.method == "POST":
        name = request.POST['name']
        address = request.POST['address']
        email = request.POST['email']
        phone = request.POST['phone']
        gender = request.POST['gender']
        image = request.FILES['image']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=name).exists():
            messages.info(request, "Username already taken")
            return redirect("user_signup")

        if User.objects.filter(email=email).exists():
            messages.info(request, "Email already taken")
            return redirect("user_signup")

        if pass1 != pass2:
            messages.info(request, "Password do not matched")
            return redirect("user_signup")

        
        user = User.objects.create_user(
            username=name, email=email, password=pass1)
        StudentUser.objects.create(
            user=user, address=address, mobile=phone, image=image, gender=gender, type="student")

        messages.success(request, "User Created")
        return redirect("user_login")

    return render(request, 'user_signup.html')


def add_job(request):
    if request.method == "POST":
        title = request.POST['title']
        cname = request.POST['company_name']
        loc = request.POST['location']
        sal = request.POST['salary']
        exp = request.POST['exp']
        sd = request.POST['start_date']
        ed = request.POST['end_date']
        city = request.POST['city']
        desc = request.POST['desc']
        logo = request.FILES['logo']
        rec = request.user
        recruiter = Recruiter.objects.get(user=rec)

        addjob=AddJob.objects.create(
            recruiter=recruiter, title=title, company_name=cname, location=loc, salary=sal, experience=exp, start_date=sd, end_date=ed,city=city,desc=desc,logo=logo,creationdate=date.today())
        addjob.save()
        messages.info(request,'Successfully Job Post')
        return redirect('add_job')
    return render(request, 'add_job.html')


def apply_job(request,id):
    user=request.user
    student=StudentUser.objects.get(user=user)
    job=AddJob.objects.get(id=id)
    date1=date.today()
    if job.end_date < date1:
        messages.info(request,'Job is expired')
    elif job.start_date > date1:
        messages.info(request,'Job is not open')

    else:
        if request.method=='POST':
            resume=request.FILES['resume']
            JobApplied.objects.create(student=student,job=job,resume=resume,applydate=date.today())
            messages.info(request,'Successfully Applied')
    return render(request,'apply_job.html')

def candidate_applied(request):
    applied=JobApplied.objects.all
    context={'appliedjobs':applied}
    return render(request,'candidate_applied.html',context)

def user_home(request):
    user=request.user
    recruiter=StudentUser.objects.get(user=user)
    if request.method == "POST":
        name = request.POST['name']
        address = request.POST['address']
        email = request.POST['email']
        phone = request.POST['phone']
        gender = request.POST['gender']
        
        recruiter.user.user=name
        recruiter.address=address
        recruiter.user.email=email
        recruiter.mobile=phone
        recruiter.gender=gender
        recruiter.save()
        
        messages.success(request, "User profile Updated")
        return redirect("user_home")
   
    context={'user':recruiter}
    return render(request, 'user_home.html',context)


def recruiter_home(request):
    user=request.user
    recruiter=Recruiter.objects.get(user=user)
    if request.method == "POST":
        name = request.POST['name']
        company = request.POST['company']
        email = request.POST['email']
        phone = request.POST['phone']
        gender = request.POST['gender']
        
        recruiter.user.user=name
        recruiter.company=company
        recruiter.user.email=email
        recruiter.mobile=phone
        recruiter.gender=gender
        recruiter.save()
        
        messages.success(request, "User profile Updated")
        return redirect("recruiter_home")
   
    context={'user':recruiter}
    return render(request, 'recruiter_home.html',context)


def search(request):
    service = Service.objects.all
    query = request.GET.get('query')
    job = Job2.objects.filter(name__icontains=query)

    data = {
        'job': job,
        'service': service
    }

    return render(request, 'search.html', data)
