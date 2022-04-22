from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path("ethnos/<int:id>", views.ethnos),
    path("ethnos/<int:ethnosId>/article/<int:articleId>", views.article),
    path("ethnos/<int:ethnosId>/article/<int:articleId>/edit", views.edit),
    path('moderation', views.moderation),
    path('news', views.news),
    path('contacts', views.contacts)
]
