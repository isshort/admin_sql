from django.urls import path

from nx import views

urlpatterns = [
    path('main/info/', views.MainPageInfo.as_view()),
]
