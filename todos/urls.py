from django.urls import path
from . import views

urlpatterns = [
    path("", views.todo_list_create_detail_view),
    path("<int:pk>", views.todo_detail_view),
]
