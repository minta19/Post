from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import get_user_model
from .models import Post
from django.contrib.auth.decorators import login_required
from .forms import PostForm,UserLoginForm,UserRegisterForm
from django.contrib.auth import logout

# Create your views here.

User=get_user_model()

def userLogin(request):
    if request.method=='POST':
        form=UserLoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            print('Username:', username)
            print('Password:', password)
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('postcreat')
            else:
                form.add_error(None, 'Invalid username or password.')
    else:
        form = UserLoginForm()
    return render(request, 'registration/login.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
           user= form.save()
           login(request,user)
           return redirect('login') 
    else:
        form = UserRegisterForm()
    return render(request, 'registration/signup.html', {'form': form})

def Post_list(request):
    posts=Post.objects.all()
    context={
        "posts":posts
    }
    return render(request,'PostApp/post_list.html',context)

@login_required
def Post_creation(request):
    if request.method=='POST':
        form=PostForm(request.POST,request.FILES)
        if form.is_valid():
            if request.user.is_authenticated:
               post=form.save(commit=False)
               post.user=request.user
               post.save()
               return redirect('postcreat')
    else:
        form = PostForm()
    return render(request, 'PostApp/create_post.html', {'form': form})
 
def userLogout(request):
    logout(request)
    return redirect('login')  
