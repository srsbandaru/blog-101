from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path('', views.PostList.as_view(), name = "post_list"),
    path('create/', views.PostCreate.as_view(), name = "create_post")
]