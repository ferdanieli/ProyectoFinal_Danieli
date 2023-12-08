from django.urls import path
from blog.views import show_html

urlpatterns = [
    path('show/', show_html),
]
