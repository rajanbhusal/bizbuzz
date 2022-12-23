from django.shortcuts import render, redirect
from . models import Profile, Message
from . forms import MessageForm, CustomUserCreationForm, ProfileForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
# Create your views here.


def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, "users/profiles.html", context)


def userProfile(request, pk):
    profileObj = Profile.objects.get(id=pk)
    posts = profileObj.post_set.all()
    context = {'profileObj': profileObj, 'posts': posts}
    return render(request, "users/profile.html", context)


@login_required(login_url='login')
def sendMessage(request, pk):
    sender = request.user.profile
    receipient = Profile.objects.get(id=pk)
    form = MessageForm()
    if request.method == 'POST':
        form = MessageForm(request.POST, request.FILES)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = sender
            message.receipient = receipient
            message.save()
            messages.success(request, "message sent")
            return redirect('inbox')
    context = {'form': form}
    return render(request, "users/message_form.html", context)


@login_required(login_url='login')
def inbox(request):
    user = request.user.profile
    all_messages = Message.objects.filter(receipient=user)
    context = {'all_messages': all_messages}
    return render(request, "users/inbox.html", context)


@login_required(login_url='login')
def viewMessage(request, pk):
    message = Message.objects.get(id=pk)
    message.is_read = True
    all_messages = Message.objects.distinct().filter(
        Q(sender=message.sender, receipient=request.user.profile) |
        Q(sender=request.user.profile, receipient=message.sender)
    )
    context = {'message': message,
               'sender': message.sender, 'all_messages': all_messages}
    return render(request, "users/message.html", context)


def createUser(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            messages.success(request, "User account created")
            return redirect('updateUser')
        else:
            messages.error(request, "Error in creating user account")
    context = {'form': form}
    return render(request, "users/user_form.html", context)


@login_required(login_url='login')
def updateUser(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Account Updated!")
            return redirect('users')
        else:
            messages.error(request, "Error in updating Profile")
    context = {'form': form}
    return render(request, "users/update-user.html", context)


@login_required(login_url='login')
def logoutUser(request):
    messages.success(request, "Loggout Out Successfully!")
    logout(request)
    return redirect('login')


def loginUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if username:
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, "Logged In Successfully!")
                return redirect('posts')
            else:
                messages.error(request, "Username and passwords do not match")
        else:
            messages.error(request, "User doesnot exist")
    context = {}
    return render(request, "users/login.html", context)
