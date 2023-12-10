from django.urls import path
from accounts.views import login_request, logout_request

urlpatterns = [
    path('login/', login_request, name="Login"),
    path('logout/', logout_request, name="Logout"),
]