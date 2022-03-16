from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
    IsAdminUser,
)
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .paginations import DefaultPagination
from .filters import PostFilters
from .serializers import PostSerializer, CategorySerializer
from ...models import Post, Category
from .permissions import IsOwnerOrReadOnly

# Example for Function Based View
"""
from rest_framework.decorators import api_view,permission_classes
from rest_framework import status
from django.shortcuts import get_object_or_404

@api_view(["GET","POST"])
@permission_classes([IsAuthenticatedOrReadOnly])
def postList(request):
    if request.method == "GET":
        posts = Post.objects.filter(status=True)
        serializer = PostSerializer(posts,many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

@api_view(["GET","PUT","DELETE"])
@permission_classes([IsAuthenticatedOrReadOnly])
def postDetail(request,id):  
    post = get_object_or_404(Post,pk=id,status=True)
    if request.method == "GET":
        serializer = PostSerializer(post)    
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = PostSerializer(post,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == "DELETE":
        post.delete()
        return Response({"detail":"item removed successfully"},status=status.HTTP_204_NO_CONTENT)
"""

# Example for ApiView in Class Based View
'''
from rest_framework.views import APIView
class PostList(APIView):
    """getting a list of posts and creating new posts"""
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer

    def get(self,request):
        """retriveing a list of posts"""
        posts = Post.objects.filter(status=True)
        serializer = PostSerializer(posts,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        """creating a post with provided data"""
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class PostDetail(APIView):
    """ getting detail of the post and edit plus removing it """
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer

    def get(self,request,id):
        """ retriveing the post data """
        post = get_object_or_404(Post,pk=id,status=True)
        serializer = self.serializer_class(post)    
        return Response(serializer.data)

    def put(self,request,id):
        """ editing the post data """
        post = get_object_or_404(Post,pk=id,status=True)
        serializer = PostSerializer(post,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self,request,id):
        """ deleting the post object """
        post = get_object_or_404(Post,pk=id,status=True)
        post.delete()
        return Response({"detail":"item removed successfully"},status=status.HTTP_204_NO_CONTENT)
'''

# Example for GenericApiView in Class Based View
'''
class PostList(ListCreateAPIView):
    """getting a list of posts and creating new posts"""
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)


class PostDetail(RetrieveUpdateDestroyAPIView):
    """ getting detail of the post and edit plus removing it """
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)    
'''

# Example for ViewSet in CBV


class PostModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # filterset_fields = {'category':["exact","in"], 'author':["exact"],'status':["exact"]}
    filterset_class = PostFilters
    search_fields = ["title", "content"]
    ordering_fields = ["published_date"]
    pagination_class = DefaultPagination


class CategoryModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
