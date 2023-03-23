from rest_framework import generics
from .models import Post
from .serializers import PostSerializer, UserSerializer
from .service import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from .permissions import IsAuthorOrReadOnly
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from .service import get_model_objects


class PostViewSet(viewsets.ModelViewSet):
    queryset = get_model_objects(Post)
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnly, )


class UserViewSet(viewsets.ModelViewSet):
    user = get_user_model()

    queryset = get_model_objects(user)
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser, )


# @api_view(["GET", "POST"])
# @permission_classes((IsAuthenticatedOrReadOnly, ))
# def post_list(request):
#     if request.method == "GET":
#         posts = get_model_objects(Post)
#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == "POST":
#         try:
#             data = request.data
#
#             serializer = PostSerializer(data=data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#         except Exception as e:
#             print(e)
#
#             return Response({
#                 "data": {},
#                 "message": 'something went wrong'
#             }, status=status.HTTP_400_BAD_REQUEST)
#
#
# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = get_model_objects(Post)
#     serializer_class = PostSerializer
#     permission_classes = (IsAdminUser, IsAuthorOrReadOnly,)
#
#
# class UserList(generics.ListCreateAPIView):
#     user = get_user_model()
#
#     queryset = user.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = (IsAdminUser, )
#
#
# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     user = get_user_model()
#
#     queryset = user.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = (IsAdminUser,)
