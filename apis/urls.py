#from django.conf.urls import url
from django.urls import path, include
from .views import (
    PostListApiView,
)

urlpatterns = [
    path('api/', PostListApiView.as_view()),
]