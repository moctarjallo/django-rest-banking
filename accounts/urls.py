from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from accounts import views

urlpatterns = [
    path('clients/', views.ClientList.as_view()),
    path('clients/<int:pk>', views.ClientDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)