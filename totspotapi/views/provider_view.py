from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from totspotapi.models import Provider



class ProviderView(ViewSet):
    def retrieve(self, request, pk):
        provider = Provider.objects.get(pk=pk)
        serializer = ProviderSerializer(provider)
        return Response(serializer.data)

    def list(self, request):
        providers = Provider.objects.all()
        serializer = ProviderSerializer(providers, many=True)
        return Response(serializer.data)
    
    def update(self, request, pk):
        """Handle PUT requests for a parent

        Returns:
            Response -- Empty body with 204 status code
        """
        provider = Provider.objects.get(pk=pk)
        provider.phone_number = request.data["phoneNumber"]

        provider.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT) 



class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = (
            'id',
            'user',
            'provider_name',
            'phone_number'
        )