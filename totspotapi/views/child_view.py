from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ViewSet
from django.http import HttpResponseServerError
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from totspotapi.models import Parent, Child, Allergy, ChildAllergy

class ChildView(ViewSet):
    def create(self, request):
        """Handle CHILD operations.
        Returns
        JSON serialized child instance"""

        allergies = request.data["allergies"]
        for allergy in allergies:
            try:
                allergy_to_assign = Allergy.objects.get(pk=allergy)
            except Allergy.DoesNotExist:
                return Response({"message": "The allergy you specified does not exist"}, status = status.HTTP_404_NOT_FOUND)


        parent = Parent.objects.get(user=request.auth.user)
        child = Child.objects.create(
            first_name = request.data["firstName"],
            last_name = request.data["lastName"],
            medications = request.data["medications"],
            age= request.data["age"],
            details = request.data["details"],
            parent = parent 
        )


        for allergy in allergies:
            allergy_to_assign = Allergy.objects.get(pk=allergy)
            child_allergy = ChildAllergy()
            child_allergy.child= child
            child_allergy.allergy = allergy_to_assign
            child_allergy.save()


        serializer = ChildSerializer(child)
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    
    def list(self, request):
        """Handle GET request, all children. """
        children=Child.objects.all()
        serializer=ChildSerializer(children, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk):
        """Handle GET request for a single child. """
        child=Child.objects.get(pk=pk)
        serializer=ChildSerializer(child)
        return Response(serializer.data)
    
    def update(self, request, pk):
        """ Handle PUT request for a single child. """
        child = Child.objects.get(pk=pk)
        allergies = Allergy.objects.get(pk=request.data["allergiesId"])
        child.first_name = request.data["firstName"]
        child.last_name = request.data["lastName"]
        child.medications = request.data["medications"]
        child.allergies = allergies
        child.age = request.data["age"]
        child.details = request.data["details"]
        #post.date = request.data["date"]
        child.save()
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        child = Child.objects.get(pk=pk)
        child.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class AllergySerializer(serializers.ModelSerializer):
    """JSON serializer for posts."""
    class Meta:
        model=Allergy
        fields=('id', 'type')

class ParentSerializer(serializers.ModelSerializer):
    """JSON serializer for posts."""
    class Meta:
        model=Parent
        fields=('id', 'parent_name')


class ChildSerializer(serializers.ModelSerializer):
    """JSON serializer for children."""
    allergies = AllergySerializer(many=True, required=False)
    parent = ParentSerializer(many=False)
    class Meta:
        model=Child
        fields=('id', 'first_name', 'last_name', 'medications', 'age', 'allergies', 'details', 'parent',)
        depth=2