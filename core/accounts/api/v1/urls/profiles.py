from django.urls import path, include
from .. import views

urlpatterns = [
    path("", views.ProfileApiView.as_view(), name="profile"),
]
