from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from django.http import HttpResponse
from .forms import uform
from django import forms
from django.forms.utils import ErrorList
from django.http import Http404
from .models import Myusr, Profile,User,activa
from forums.models import ThreadDB, ForumDB, Mypost,Report
from . forms import EditForm,chform
from django.core.mail import EmailMessage
import random

log = 0


def index(request):
    return render(request, 'homepage/home.html', {'log': log})


def base(request):
    return render(request, 'randomq/letter.html')


def about(request):
    return render(request, 'homepage/about.html')


def tnc(request):
    return render(request, 'homepage/tnc.html')


def faq(request):
    return render(request, 'homepage/faq.html')


def login_user(request):
    if not request.user.is_authenticated():
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    log = 1
                    login(request, user)
                    return render(request, 'homepage/home.html', {'log': log})
                else:
                    return render(request, 'homepage/login.html')
            else:
                return render(request, 'homepage/login.html')
        return render(request, 'homepage/login.html')
    else:
        logout(request)
        log = 0
        return render(request, 'homepage/login.html')


def view_profile(request):
    if not request.user.is_authenticated():
        return render(request, 'homepage/login.html')

    else:

        info = Myusr.objects.filter(user=request.user)
        pic = Profile.objects.filter(user=request.user)
        reports=ThreadDB.objects.filter(user_name=request.user).filter(flag=1)
        c=0
        fl=fl1=0
        k = 0
        for i in pic:
            if i.profile_pic is None:
                k = 0

            else:
                k = 1
        for r in reports:
            c=c+1
        if c==0:
            fl1=1
        else:
            fl=1

        all_threads = ThreadDB.objects.filter(user_name=request.user)
        all_forums = ForumDB.objects.filter()
        cu = request.user
        return render(request, 'homepage/profile.html', {'all_threads': all_threads, 'all_forums': all_forums, 'cu': cu,
                                                         'info': info, 'pic': pic, 'k': k,'fl1':fl1,'fl':fl,'reports':reports})


def edit_profile(request):
    if not request.user.is_authenticated():
        return render(request, 'homepage/login.html')
    else:

        all_threads = ThreadDB.objects.all()
        all_forums = ForumDB.objects.all()
        cu = request.user

        form = EditForm(request.POST or None, request.FILES or None)
        if Profile.objects.filter(user=request.user).exists():
            Profile.objects.get(user=request.user).delete()
        if form.is_valid():
            editings = Profile.objects.filter(user=request.user)
            editing = form.save(commit=False)
            editing.user = request.user
            editing.checker = 1
            k = 1
            editing.save()
            context = {
                "form": form,
                "pic": Profile.objects.filter(user=request.user),
                "all_threads": all_threads,
                "all_forums": all_forums,
                "cu": cu,
                "info": Myusr.objects.filter(user=request.user),
                "editing": editing,
                "k": k,
            }
            return render(request, 'homepage/profile.html', context)
        context = {
            "form": form,
            "pic": Profile.objects.filter(user=request.user),
            "all_threads": all_threads,
            "all_forums": all_forums,
            "cu": cu,
            "info": Myusr.objects.filter(user=request.user),
        }
        return render(request, 'homepage/edit_profile.html', context)


"""class userformview(View):
    form_class = uform
    template_name = 'homepage/register.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            if form.cleaned_data['password'] != form.cleaned_data['cpassword']:
                return HttpResponse("passwords dont match")
            else:
                password = form.cleaned_data['password']
                cpassword = form.cleaned_data['cpassword']
                user.set_password(password)
                user.save()
                user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    ob = Myusr()
                    ob.user = request.user
                    ob.save()

                    return render(request, 'randomq/letter.html')
                else:
                    return redirect('homepage:register')
            else:
                return redirect('homepage:register')
        else:
            return redirect('homepage:register')"""

def getreg(request):
    form=uform()
    return render(request,'homepage/register.html',{'form':form})

def regi(request):
    if request.method=='POST':
        form = uform(request.POST,request.FILES)
        us=request.POST.get('username','')
        existing = User.objects.filter(username__iexact=request.POST.get('username',''))
        if existing.exists():
            fly=0
            fly=1
            stri="A user with that username already exists."
            return render(request,'homepage/register.html',{'fly':fly,'stri':stri})

        eml = request.POST.get('email', '')
        if "@" not in eml:
            fly1=0
            fly1=1
            stri="Please enter valid email-id."
            return render(request,'homepage/register.html',{'fly1':fly1,'stri':stri})
        domain = eml.split('@')[1]
        domain_list = ["gmail.com", "yahoo.com", "hotmail.com","rediff.com","gmail.in", "yahoo.in", "hotmail.co.in","rediff.co.in"]
        if domain not in domain_list:
            fly2=0
            fly2=1
            stri="Please enter valid domain."
            return render(request,'homepage/register.html',{'fly2':fly2,'stri':stri})
        ema=User.objects.filter(email=eml)
        c=0
        for em in ema:
            c=c+1
        if c>0:
            raise forms.ValidationError(("Please enter a different email-id"))
        if form.is_valid():
            user = form.save(commit=False)
            firstname = request.POST.get('first_name', '')
            username = request.POST.get('username', '')
            email = request.POST.get('email', '')
            password = request.POST.get('password', '')
            cpassword = request.POST.get('cpassword', '')
            if password!=cpassword:
                fly3 = 0
                fly3 = 1
                stri = "Passwords dont match."
                return render(request, 'homepage/register.html', {'fly3': fly3, 'stri': stri})
            else:
                password = request.POST.get('password', '')
                cpassword = request.POST.get('cpassword', '')
                user.set_password(password)                
                print("in process")
                otp=random.randrange(10000,99999,2)
                print(otp)
                mail=EmailMessage('Account Activation- Potterhead','Thank you for creating an account with PotterHead!\n Your Activation OTP is '+str(otp)+'. \n\nEnter the OTP onto our page to begin your Hogwarts journey!\n\nRegards, The Potterhead Team ',to=[email])
                mail.send() 				
                print("sent")
                ac=activa()
                ac.otp=str(otp)
                ac.user1=username
                print(ac.user1)
                y = User.objects.all()

                for j in y:
                    print(y)
                    if j.username == username:
                        ac.user=j
                ac.save()
                user.is_active=False
                #user = authenticate(username=username, password=password)

                user.save()
           
                return render(request,'homepage/otp.html')
                # if user is not None:
                    # if user.is_active:
                        # login(request, user)
                        # ob = Myusr()
                        # ob.user = request.user
                        # ob.save()
                        # return render(request, 'randomq/letter.html')
                    # else:
                        # return redirect('homepage:reg')
                # else:
                    # return redirect('homepage:reg')
        else:
            return redirect('homepage:reg')

def activatt(request):
    us=activa.objects.filter(user1=request.POST.get('user1',''))
    for i in us:
        print(i.user1)
        r=request.POST.get('otp','')
        print r
        if i.otp==r:
            print "hey"
            use=User.objects.get(username=i.user1)
            use.is_active=True
            use.save()
            use.backend='django.contrib.auth.backends.ModelBackend'
            login(request,use)
            ob = Myusr()
            ob.user = request.user
            ob.save()
            print(use)			
            print(r)
            return render(request,'randomq/letter.html')

    fly4 = 0
    fly4 = 1
    stri = "Please enter a different email-id."
    return render(request, 'homepage/register.html', {'fly4': fly4, 'stri': stri})

    #return HttpResponse("Please enter a valid email-id")

"""def forgot_user(request):
        return render(request,'homepage/foruser.html')
def forgotpassword(request):
        username = request.POST.get('username','')
        print username
        obj = User.objects.filter(username=username)
        print obj
        email=request.POST.get('email','')
        print email
        subject = "Activation OTP for your PotterHead account"
        message = "Hello " + username + ",\nYour password for PotterHead is '" + obj.password + "'.\n\n-Regards:\n Pottterhead Team"
        email = EmailMessage(subject,message, to=[email])
        email.send()
        return HttpResponse("success")"""


def account_settings(request):
    if not request.user.is_authenticated():
        return render(request, 'homepage/login.html')
    else:

        all_threads = ThreadDB.objects.all()
        all_forums = ForumDB.objects.all()
        cu = request.user

        info = Myusr.objects.filter(user=request.user)
        pic = Profile.objects.filter(user=request.user)
        for i in info:
            print i.user

        k = 0
        for i in pic:
            if i.profile_pic is None:
                k = 0

            else:
                k = 1

        form = chform(request.POST or None)
        if form.is_valid():
            form1 = form.save(commit=False)
            u = User.objects.get(username__exact=request.user)

            if form.cleaned_data['password'] != form.cleaned_data['cpassword']:
                return HttpResponse("passwords dont match")
            else:
                password = form.cleaned_data['password']
                cpassword = form.cleaned_data['cpassword']

            u.set_password(password)

            u.save()
            return render(request, 'homepage/profile.html',  {'all_threads': all_threads, 'all_forums': all_forums,
                                                                   'cu': cu, 'info': info, 'pic': pic, 'k': k})
        context = {
            "form": form,
        }
        return render(request, 'homepage/account_settings.html', {'all_threads': all_threads, 'all_forums': all_forums,
                                                                  'cu': cu, 'info': info, 'pic': pic, 'k': k, 'form': form})

