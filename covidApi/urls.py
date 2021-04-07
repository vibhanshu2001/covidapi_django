from django.contrib import admin
from django.urls import path,include
from covid import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('covid.urls')),
]
