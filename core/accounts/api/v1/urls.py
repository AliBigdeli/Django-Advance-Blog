from django.urls import path,include
from . import views

app_name = 'api-v1'

urlpatterns = [
    # registration
    path('registration/',views.RegistrationApiView.as_view(),name='registration')

    # change password
    # reset password
    # login token
    # login jwt

]


