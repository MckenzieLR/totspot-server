from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from totspotapi.models import Parent



class ParentView(ViewSet):
    def retrieve(self, request, pk):
        parent = Parent.objects.get(pk=pk)
        serializer = ParentSerializer(parent)
        return Response(serializer.data)

    # if totUser is staff get all parents else get parent who is logged in to only show parent details for parent 
    # who is logged in 
    def list(self, request):

        if request.auth.user.is_staff:
            parents = Parent.objects.all()

        else:
            parents = Parent.objects.filter(user=request.auth.user)

        serializer = ParentSerializer(parents, many=True)
        return Response(serializer.data)
    
    def update(self, request, pk):
        """Handle PUT requests for a parent

        Returns:
            Response -- Empty body with 204 status code
        """
        parent = Parent.objects.get(pk=pk)
        parent.phone_number = request.data["phoneNumber"]

        parent.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT) 

class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = (
            'id',
            'user',
            'phone_number',
            'parent_name'
        )