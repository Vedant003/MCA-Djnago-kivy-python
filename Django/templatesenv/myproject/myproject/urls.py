from django.contrib import admin
from django.urls import path
from myapp.views import hello

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello, name='hello'),
]
# http://127.0.0.1:8000/hello/