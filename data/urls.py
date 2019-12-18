from django.urls import path

from data import views
from data.views import IndexView

urlpatterns = [
    path('', IndexView.as_view()),
    path('search/', views.search, name='search')
]
