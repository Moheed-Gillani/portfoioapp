from django.shortcuts import render,redirect,get_object_or_404,HttpResponseRedirect
from .models import Project,Details,Comment
from personal_portfolio.settings import EMAIL_HOST_USER
from django.http import HttpResponse
from django.core.mail import send_mail
from projects.forms import CustomUserCreationForm,ReviewForm
from django.urls import reverse
from projects.models import Reviews
# users/views.py
from django.contrib.auth import login
from django.templatetags.static import static
# Create your views here.
def index(request):
    context=Project.objects.all().order_by('-uploaded')
    reviews=Reviews.objects.all().order_by('-created_on')
    total=Reviews.objects.all().count()
    return render(request,'home/index.html',{'context':context,'reviews': reviews,'total':total})
def detail(request,id):
    detail=get_object_or_404(Details,Project_id=id)
    return render(request,'home/detail.html',{'detail':detail})
def add_comments(request,id):
    if request.method=='POST':
        names=request.POST.get('name')
        email=request.POST.get('email')
        Comments=request.POST.get('body')
        Details_ids=int(id)
        comment=Comment(name=names,email=email,Comment=Comments,Details_id=Details_ids)
        comment.save()
        return render(request,'home/comments.html',{'id':int(id)})
    else:
        return render(request,'home/detail.html')
def show_comments(request):
    if request.method=='POST':
        ids=request.POST.get('id')
        objects=Comment.objects.filter(Details_id=int(ids)).order_by('-created_on')
        return render(request,'home/comments.html',{'comments':objects})
def subscribe(request):
    if request.method=='POST':
        name=request.POST.get('name')
        subject=request.POST.get('subject')
        message=request.POST.get('body')
        recepient=str(request.POST.get('email'))
        send_mail(subject,message, EMAIL_HOST_USER, [recepient], fail_silently = False)
        Html="Your message delivered successfully"
        return render(request,'home/subscribe.html',{'html':Html})
    else:
        Html="Please fill the below forms to send us email"
        return render(request,'home/subscribe.html',{'html':Html})
def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST or None)
        if form.is_valid():
            user = form.save(commit=False)
            user.backend = "django.contrib.auth.backends.ModelBackend"
            user.save()
            return render(request,'home/index.html',{'success':'you have been register successfuly please login using the correct username and password'})
        else:
            return HttpResponse("form is not valid")
    return render(
            request, "users/register.html",
            {"form": CustomUserCreationForm}
        )
def add_reviews(request):
    form = ReviewForm()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        form.save()
        return redirect('/')
    else:
        return render(request, 'home/reviews.html',{'form': form})