from django.urls import path, include
from .views import *
from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('posts', PostViewSet, basename='posts')


urlpatterns = [
    path('', include(router.urls))
]

'''urls for views'''
#     path('<int:pk>/', PostDetail.as_view()),
#     path('', post_list),
#     path('users/<int:pk>/', UserDetail.as_view()),
#     path('users/', UserList.as_view()),
# ]
