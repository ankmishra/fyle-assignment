from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('api/banks/', views.ApiList.as_view()),
    path('api/banks/<slug:ifsc>/', views.ApiDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)