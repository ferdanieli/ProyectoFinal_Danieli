from django.urls import path
from accounts.views import login_request, logout_request, register_request, editar_request, editar_avatar_request

urlpatterns = [
    path('login/', login_request, name="Login"),
    path('update/', editar_request, name="Update"),
    path('logout/', logout_request, name="Logout"),
    path('register/', register_request, name="Sign Up"),
    path('avatar/', editar_avatar_request, name="Avatar"),
]