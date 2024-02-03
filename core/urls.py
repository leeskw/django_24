from django.urls import path 
from . import views 
from django.contrib.auth.views import LoginView

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    # path("signin/", views.signin, name="signin"),
    path('signin/', LoginView.as_view(template_name='core/login.html'), name='signin'),
    path("signout/", views.signout, name="signout"),
    path("profile/", views.profile, name="profile"),
    path("update-profile/", views.update_profile, name="update-profile")
]