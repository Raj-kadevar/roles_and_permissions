
from django.urls import path

from user.views import UserLoginView, GroupListView, ManagePermissions, ViewPermissions, DeletePermissions

urlpatterns = [
    path('',UserLoginView.as_view(),name="login"),
    path('home/',GroupListView.as_view(),name="home"),
    path('ManagePermissions/<int:id>',ManagePermissions.as_view(),name="ManagePermissions"),
    path('ViewPermissions/<int:id>',ViewPermissions.as_view(),name="ViewPermissions"),
    path('DeletePermissions/<int:id>',DeletePermissions.as_view(),name="DeletePermissions"),
]
