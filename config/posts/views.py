from rest_framework import generics
from .models import Post
from .serializers import PostSerializer
from .service import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from .permissions import IsAuthorOrReadOnly


# class PostList(generics.ListCreateAPIView):
#     queryset = get_model_objects(Post)
#     serializer_class = PostSerializer


@api_view(["GET", "POST"])
@permission_classes((IsAuthenticatedOrReadOnly, ))
def post_list(request):
    if request.method == "GET":
        posts = get_model_objects(Post)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = get_model_objects(Post)
    serializer_class = PostSerializer
    permission_classes = (IsAdminUser, IsAuthorOrReadOnly,)
