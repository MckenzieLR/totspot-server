from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ViewSet
from django.http import HttpResponseServerError
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from totspotapi.models import Parent, Post

class PostView(ViewSet):
    def create(self, request):
        """Handle POST operations.
        Returns
        JSON serialized post instance"""
        parent = Parent.objects.get(user=request.auth.user)
        post = Post.objects.create(
            content = request.data["content"],
            date= request.data["date"],
            parent = parent 
        )
        serializer = PostSerializer(post)
        return Response(serializer.data)
    
    def list(self, request):
        """Handle GET request, all posts. """
        # parent = Parent.objects.get(user=request.auth.user)
        posts=Post.objects.all()
        serializer=PostSerializer(posts, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk):
        """Handle GET request for a single post. """
        post=Post.objects.get(pk=pk)
        serializer=PostSerializer(post)
        return Response(serializer.data)
    
    def update(self, request, pk):
        """ Handle PUT request for a single post. """
        post = Post.objects.get(pk=pk)
        post.content = request.data["content"]
        #post.date = request.data["date"]
        post.save()
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        post = Post.objects.get(pk=pk)
        post.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class ParentSerializer(serializers.ModelSerializer):
    """JSON serializer for posts."""
    class Meta:
        model=Parent
        fields=('id', 'parent_name')


class PostSerializer(serializers.ModelSerializer):
    """JSON serializer for posts."""
    parent = ParentSerializer(many=False)
    class Meta:
        model=Post
        fields=('id', 'content', 'date', 'parent', )
