from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.models import Group, Permission
from django.views.generic import ListView, CreateView

# from user.forms import RegistrationForm

users = get_user_model()
class UserLoginView(LoginView):
    template_name = "user/login.html"
    def get_success_url(self):
        return reverse_lazy('home')


class GroupListView(LoginRequiredMixin,ListView):
    template_name = "user/home.html"
    queryset = Group.objects.all().order_by("id")
    context_object_name = "groups"

class UserListView(LoginRequiredMixin,ListView):
    template_name = "user/users.html"
    queryset = users.objects.all().order_by("id")
    context_object_name = "users"


class ViewPermissions(LoginRequiredMixin,View):
    def get(self, request, *args, **kwargs):
        group_permissions = Group.objects.get(id=kwargs.get('id')).permissions.all()
        all_permissions = Permission.objects.all()
        return render(request,"user/display.html",{'all_permissions':all_permissions,'group_permissions':group_permissions})

    def post(self, request, *args, **kwargs):
        group_permissions = Group.objects.get(id=kwargs.get('id'))
        total_permissions = request.POST.getlist('new_selected_checkbox') + request.POST.getlist('selected_checkbox')
        group_permissions.permissions.set(total_permissions)
        return redirect('home')

class DeletePermissions(LoginRequiredMixin,View):
    def get(self, request, *args, **kwargs):
        Group.objects.get(id=kwargs.get('id')).delete()
        return redirect('home')


class UserRegistration(LoginRequiredMixin, CreateView):

    form_class = UserCreationForm
    template_name = 'user/form.html'

    def post(self, request, *args, **kwargs):
        user = UserCreationForm(request.POST)
        if user.is_valid():
            user_data = user.save()
            user_data.set_password(user_data.password)
            user_data.save()
            return redirect('home')

        else:
            errors = user.errors
            return render(request, "user/form.html", {"errors": errors, "form": user})



class ViewUserPermissions(LoginRequiredMixin,View):

    def get(self, request, *args, **kwargs):
        checkpermissions(request.user)
        user = users.objects.get(id=kwargs.get('id'))
        user_permissions = Permission.objects.filter(user=user)
        all_permissions = Permission.objects.all()
        return render(request,"user/user_permissions.html",{'all_permissions':all_permissions,'user_permissions':user_permissions})

    def post(self, request, *args, **kwargs):
        user = users.objects.get(id=kwargs.get('id'))
        total_permissions = request.POST.getlist('new_selected_checkbox') + request.POST.getlist('selected_checkbox')
        user.user_permissions.set(total_permissions)
        return redirect('users')


class DeleteUser(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        users.objects.get(id=kwargs.get('id')).delete()
        return redirect('users')

def checkpermissions(user):
    if not (user.has_perm('auth.view_user')  and  user.has_perm('auth.add_user')):
        raise ObjectDoesNotExist