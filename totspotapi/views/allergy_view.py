from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from totspotapi.models import Allergy

class AllergyView(ViewSet):

    def retrieve(self, request, pk):
        """Handle GET requests for single comment

        Returns:
            Response -- JSON serialized comment
        """
        allergy = Allergy.objects.get(pk=pk)
        serializer = AllergySerializer(allergy)
        return Response(serializer.data)
    
    def list(self, request):
        """Handle GET requests to get all comments

        Returns:
            Response -- JSON serialized list of comments
        """

        allergies = Allergy.objects.all()
        serializer = AllergySerializer(allergies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        """Handle POST operations

        Returns:
        Response -- JSON serialized comment instance"""
        allergy = Allergy.objects.create(
            type = request.data["type"]
        )
        serializer = AllergySerializer(allergy)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests for a comment

        Returns:
            Response -- Empty body with 204 status code
        """
    
       
        allergy = Allergy.objects.get(pk=pk)
        allergy.type = request.data["type"]
        allergy.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    # def destroy(self, request, pk):
    #     allergy = Allergy.objects.get(pk=pk)
    #     allergy.delete()
    #     return Response(None, status=status.HTTP_204_NO_CONTENT)

class AllergySerializer(serializers.ModelSerializer):
    class Meta:
        model = Allergy
        fields = ('id', 'type')