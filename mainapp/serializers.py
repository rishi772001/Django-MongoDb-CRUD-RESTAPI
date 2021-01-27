'''
@Author: rishi
'''

from .models import StudentDetails
from rest_framework import serializers

# Create a class that links student details with the serializer
# serializer -> convert data to json string


class SerializeStudent(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StudentDetails
        fields = ('id', 'name', 'mark1', 'mark2', 'mark3', 'total')
