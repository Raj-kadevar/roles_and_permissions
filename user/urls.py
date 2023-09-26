
from django.urls import path

from user.views import UserLoginView, GroupListView, ViewPermissions, UserRegistration, UserListView, \
    DeleteUser, DeletePermissions, ViewUserPermissions

urlpatterns = [
    path('',UserLoginView.as_view(),name="login"),
    path('home/',GroupListView.as_view(),name="home"),
    path('users/',UserListView.as_view(),name="users"),
    path('registrationform/',UserRegistration.as_view(),name="registrationform"),
    path('ViewPermissions/<int:id>',ViewPermissions.as_view(),name="ViewPermissions"),
    path('DeletePermissions/<int:id>', DeletePermissions.as_view(), name="DeletePermissions"),
    path('viewuserpermissions/<int:id>', ViewUserPermissions.as_view(), name="viewuserpermission"),
    path('deleteuserpermissions/<int:id>', DeleteUser.as_view(), name="deleteuserpermissions"),
]
