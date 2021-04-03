from rest_framework import  serializers
from .models import Movies, Rentals
from django.contrib.auth.models import User
from django.db import models




class MoviesSerializer(serializers.ModelSerializer):
	class Meta:
		model=Movies
		fields='__all__'
class RentalsSerializer(serializers.ModelSerializer):
	class Meta:
		model=Rentals
		fields='__all__'


field_set=('first_name', 'last_name', 'username', 'email')
class UserSerializer(serializers.ModelSerializer):
		class Meta:
				model=User
				fields=field_set
		def validate(self, data):
			for field in data:
				if  data[field]=="":
					raise serializers.ValidationError('All inputs are required, please')
			return data
		



	


	