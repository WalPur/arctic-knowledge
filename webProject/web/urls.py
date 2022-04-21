from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path("ethnos", views.ethnoses),
    path("ethnos/<int:id>", views.ethnos),
    path("ethnos/<int:ethnosId>/article/<int:articleId>", views.article)
]
