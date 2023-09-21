
from django.urls import path

from user.views import UserLoginView, GroupListView, ViewPermissions, DeletePermissions

urlpatterns = [
    path('',UserLoginView.as_view(),name="login"),
    path('home/',GroupListView.as_view(),name="home"),
    path('ViewPermissions/<int:id>',ViewPermissions.as_view(),name="ViewPermissions"),
    path('DeletePermissions/<int:id>',DeletePermissions.as_view(),name="DeletePermissions"),
]
