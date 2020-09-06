from django.shortcuts import render
from django.http import HttpResponseRedirect
from . forms import UserCreationForm , UserLoginForm
from django.contrib.auth import get_user_model,login,logout
from . models import ActivationProfile

user = get_user_model()
# Create your views here.
def register(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {}
    context['form'] = form
    return render(request,"accounts/register.html",context) 

def user_login(request):
    context = {}
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        # query = form.cleaned_data.get('query')
        # user_obj = user.objects.get(username=username)
        user_obj = form.cleaned_data.get('user_obj')
        """
        if we use this filter method then we can
        """
        # user_obj = user.objects.filter(username=username).first
        login(request,user_obj)
        return HttpResponseRedirect('/')
    context['form'] = form
    return render(request,"accounts/login.html",context) 

def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/login/")

def activate_user_view(request,code=None,*args,**kwargs):
    print("codeeeeeeeeee",code)
    if code:
        act_profile_qs = ActivationProfile.objects.filter(key=code)
        print("act_profile_qs" , act_profile_qs)
        if act_profile_qs.exists() and act_profile_qs.count() == 1:
            act_obj = act_profile_qs.first()
            if not act_obj.expired:
                user_obj = act_obj.user
                user_obj.is_active = True
                user_obj.save()
                act_obj.expired = True
                act_obj.save()
                return HttpResponseRedirect("/login/")
    return HttpResponseRedirect("/login/")