from django.urls import path
from .views import *


urlpatterns = [
    path('<int:pk>/', PostDetail.as_view()),
    path('', post_list),
]
