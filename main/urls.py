from django.urls import path

from .views import BookApiView, CategoryApiView

urlpatterns = [
    path('book/', BookApiView.as_view()),
    path('book/<int:pk>/', BookApiView.as_view()),
    path('category/', CategoryApiView.as_view()),
    path('category/<str:title>/', CategoryApiView.as_view()),
]