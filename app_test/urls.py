
from django.contrib import admin
from django.urls import path, include
from .views import (
    DefaultListView
)

urlpatterns = [
    path("", DefaultListView.as_view(), name="default_view"),
]
