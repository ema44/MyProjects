from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse,request
from .models import YouthCenter
from django.views import generic
from django.http import HttpResponse
from .forms import ProfileForm
from .models import Profile
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.views import View
from django.contrib import messages
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView
from . import models
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class FormMessageMixin(object):
  @property
  def form_valid_message(self):
   return NotImplemented
  form_invalid_message = 'Please correct the errors below.'
  def form_valid(self, form):
   messages.success(self.request, self.form_valid_message)
   return super(FormMessageMixin, self).form_valid(form)
  def form_invalid(self, form):
    messages.error(self.request, self.form_invalid_message)
    return super(FormMessageMixin, self).form_invalid(form)




@login_required(login_url='login')
def userlist(request):
    user_list = User.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(user_list, 10)
    try:
     users = paginator.page(page)
    except PageNotAnInteger:
           users = paginator.page(1)
    except EmptyPage:
           users = paginator.page(paginator.num_pages)
    return render(request, 'YouthCenter/userlist.html', { 'users': users })


class SignUpView(CreateView):
 template_name = 'YouthCenter/signup.html'
 form_class = UserCreationForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.info(request, ' user successfully registered')
            return redirect('home-center')
    else:
        form = SignUpForm()
    return render(request, 'YouthCenter/signup.html', {'form': form})
def home(request):
    messages.info(request, ' user successfully redirected to the homepage')
    return render(request,'YouthCenter/home.html')
@login_required(login_url='login')
def dashboard(request):
    messages.info(request, ' user.request["username"] successfully redirected to the dashboard')

    return render(request,'YouthCenter/dashboard.html')

class CenterCreate(LoginRequiredMixin,FormMessageMixin, CreateView):

  model = YouthCenter
  fields = ['center_name', 'place_of_center','stsus_of_center','user','file','description','center_total_youth']
  template_name = 'YouthCenter/create.html'


class TotalList(ListView):

  model = YouthCenter
  template_name = 'YouthCenter/viewall.html'
  context_object_name = 'totalcenters'

class CenterDetailView(DetailView):
  model = YouthCenter
  template_name = 'YouthCenter/detail.html'
  context_object_name = 'totalcenters'

class CenterUpdateView(LoginRequiredMixin,  FormMessageMixin, UpdateView):
 model = YouthCenter
 fields = ['center_name', 'place_of_center','stsus_of_center','user','file','description','center_total_youth']
 template_name = 'YouthCenter/update.html'
 success_url = '/success/'
 form_valid_message = 'The document was successfully updated!'
 form_invalid_message = 'There are some errors in the form below.'

def success(request):
    messages.info(request, ' an object is successfully updated')
    return render(request,'YouthCenter/success.html')
class CenterDeleteView(DeleteView):
    model = YouthCenter
    template_name = 'YouthCenter/delete.html'
    success_url = "/removal/"
def removal(request):
    messages.info(request, ' an object is successfully removed')
    return render(request,'YouthCenter/removal.html')





def SaveProfile(request):
    amanuel = False

    if request.method == "POST":
        # Get the posted form
        MyProfileForm = ProfileForm(request.POST, request.FILES)

        if MyProfileForm.is_valid():
            profile = Profile()
            profile.name = MyProfileForm.cleaned_data["name"]
            profile.picture = MyProfileForm.cleaned_data["picture"]
            profile.save()
            amanuel = True
    else:
        MyProfileForm = ProfileForm()

    return render(request, 'YouthCenter/saved.html', locals())







