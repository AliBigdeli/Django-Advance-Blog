from django.urls import path
from .. import views

urlpatterns = [
    path("", views.ProfileApiView.as_view(), name="profile"),
]
