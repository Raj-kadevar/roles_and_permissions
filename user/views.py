from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.models import Group, Permission
from django.views.generic import ListView


class UserLoginView(LoginView):
    template_name = "user/login.html"

    def get_success_url(self):
        return reverse_lazy('home')


class GroupListView(LoginRequiredMixin,ListView):
    template_name = "user/home.html"
    queryset = Group.objects.all().order_by("id")
    context_object_name = "groups"


class ViewPermissions(LoginRequiredMixin,View):
    def get(self, request, *args, **kwargs):
        group_permissions = Group.objects.get(id=kwargs.get('id')).permissions.all()
        all_permissions = Permission.objects.all()
        return render(request,"user/display.html",{'all_permissions':all_permissions,'group_permissions':group_permissions})

    def post(self, request, *args, **kwargs):
        group_permissions = Group.objects.get(id=kwargs.get('id'))
        total_permissions = request.POST.getlist('new_selected_checkbox') + request.POST.getlist('selected_checkbox')
        group_permissions.permissions.set(total_permissions)
        group_permissions.save()
        return redirect('home')

class DeletePermissions(LoginRequiredMixin,View):
    def get(self, request, *args, **kwargs):
        Group.objects.get(id=kwargs.get('id')).delete()
        return redirect('home')


