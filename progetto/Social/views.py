from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
from Social.models import Company, Tipologia, Post
from django.shortcuts import render, get_object_or_404
from Social.models import Company, Post
from Social.forms import RegistrationForm
from django.contrib.auth import login
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from Social.forms import CompanyForm, PostForm, TipologiaForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout


def homepage(request):
    return render(request, 'base.html') 

def list_company(request):
    company = Company.objects.all()

    context = {
        'company' : company,
    }
    return render(request, 'Social/List_Company.html', context)

def list_post(request):
    post = Post.objects.all()

    context = {
        'post':post
    }
    return render(request, 'Social/List_Post.html', context)

def company_detail(request, company_id):
    company = get_object_or_404(Company, id=company_id)
    posts = Post.objects.filter(compania=company)

    context = {
        'company': company,
        'posts': posts,
    }
    return render(request, 'Social/Company_Detail.html', context)

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('homepage')
    else:
        form = RegistrationForm()
    return render(request, 'Social/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('homepage')
    else:
        form = AuthenticationForm()
    return render(request, 'Social/login.html', {'form': form})

@login_required
def create_company(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            company = form.save(commit=False)
            company.utente = request.user  # Imposta l'utente corrente
            company.save()
            return redirect('list_company')
    else:
        form = CompanyForm()
    return render(request, 'Social/create_company.html', {'form': form})
@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.utente = request.user  # Imposta l'utente corrente
            post.save()
            return redirect('list_post')
    else:
        form = PostForm()
    return render(request, 'Social/create_post.html', {'form': form})

def create_tipologia(request):
    if request.method == 'POST':
        form = TipologiaForm(request.POST)
        if form.is_valid():
            tipologia = form.save(commit=False)
            tipologia.utente = request.user  # Imposta l'utente corrente
            tipologia.save()
            return redirect('list_company')  # Redirect to a relevant page
    else:
        form = TipologiaForm()
    return render(request, 'Social/create_tipologia.html', {'form': form})

@login_required
def profile(request):
    user = request.user
    companies = Company.objects.filter(utente=user)
    posts = Post.objects.filter(utente=user)
    return render(request, 'Social/profile.html', {
        'user': user,
        'companies': companies,
        'posts': posts
    })
def user_logout(request):
    logout(request)
    return redirect('homepage')

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'Social/post_detail.html', {'post': post})

from django.shortcuts import render
from .forms import CSVUploadForm
from .ml_model import train_and_predict

def upload_and_predict(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            predictions, image_base64 = train_and_predict(csv_file)
            return render(request, 'Social/prediction_result.html', {
                'predictions': predictions,
                'image_base64': image_base64
            })
    else:
        form = CSVUploadForm()
    return render(request, 'Social/upload_csv.html', {'form': form})

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Company, Post, User

