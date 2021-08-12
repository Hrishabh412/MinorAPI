from rest_framework import serializers
from .models import Student


#serializers are just like Forms


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        #fields = ['id','firstname', 'lastname', 'email', 'age', 'dateofbirth', 'mobileno']
        fields='__all__'


    

    
        