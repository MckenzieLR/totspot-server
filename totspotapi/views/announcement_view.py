from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from totspotapi.models import Announcement, Provider
from django.contrib.auth.models import User

class AnnouncementView(ViewSet):

    def retrieve(self, request, pk):
        """Handle GET requests for single comment

        Returns:
            Response -- JSON serialized comment
        """
        announcement = Announcement.objects.get(pk=pk)
        serializer = AnnouncementSerializer(announcement)
        return Response(serializer.data)
    
    def list(self, request):
        """Handle GET requests to get all comments

        Returns:
            Response -- JSON serialized list of comments
        """

        announcements = Announcement.objects.all()
        serializer = AnnouncementSerializer(announcements, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        """Handle POST operations

        Returns:
        Response -- JSON serialized comment instance"""
        provider = Provider.objects.get(user=request.auth.user)
        announcement = Announcement.objects.create(
            provider = provider,
            date = request.data["date"],
            content = request.data["content"]
        )
        serializer = AnnouncementSerializer(announcement)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests for a comment

        Returns:
            Response -- Empty body with 204 status code
        """
    
       
        announcement = Announcement.objects.get(pk=pk)
        announcement.content = request.data["content"]

        announcement.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        announcement = Announcement.objects.get(pk=pk)
        announcement.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class ProviderSerializer(serializers.ModelSerializer):
    """JSON serializer for posts."""
    class Meta:
        model=Provider
        fields=('id', 'full_name')

class AnnouncementSerializer(serializers.ModelSerializer):
    provider = ProviderSerializer(many=False)
    class Meta:
        model = Announcement
        fields = ('id', 'provider', 'content', 'date', )
        depth=2