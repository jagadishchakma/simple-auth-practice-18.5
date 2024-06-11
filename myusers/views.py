from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout, update_session_auth_hash
from . import forms
from django.contrib.auth.decorators import login_required
# Create your views here.

#singup
def UserSignUp(request):
    if request.user.is_authenticated:
        previous_url = request.META.get('HTTP_REFERER')
        # Provide a fallback URL if HTTP_REFERER is not available
        fallback_url = 'profile'
        return redirect(previous_url or fallback_url)
    
    form = forms.UserSignUpForm()
    if request.method == 'POST':
        form = forms.UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User Signup Successfull! Please log in now....')
            return redirect('login')
        
        
    return render(request, 'signup.html', {'form': form})

#login
def UserLogin(request):
    if request.user.is_authenticated:
        previous_url = request.META.get('HTTP_REFERER')
        # Provide a fallback URL if HTTP_REFERER is not available
        fallback_url = 'profile'
        return redirect(previous_url or fallback_url)
    
    form = forms.UserLoginForm()
    if request.method == 'POST':
        form = forms.UserLoginForm(request, request.POST)
        print(form)
        if form.is_valid():
            uname = form.cleaned_data['username']
            upass = form.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request,user)
                messages.success(request, 'Logged In Successfully')
                return redirect('profile')
            messages.warning(request, 'login failed')

    return render(request, 'login.html',{'form':form})

#profile
@login_required
def UserProfile(request):
    return render(request, 'profile.html')

#logout
@login_required
def UserLogout(request):
    logout(request)
    messages.warning(request, 'Logged Out Successfully')
    return redirect('login')

@login_required
def UserPassChange(request):
    form = forms.UserPassChangeForm(request.user)
    if request.method == 'POST':
        form = forms.UserPassChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request,'Password Change Successfull')
            return redirect('profile')
    return render(request, 'passchange.html', {'form':form})

@login_required
def UserPassChange2(request):
    form = forms.UserPassChangeForm2(request.user)
    if request.method == 'POST':
        form = forms.UserPassChangeForm2(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request,'Password Change Successfull')
            return redirect('profile')
    return render(request, 'passchange.html', {'form':form})

