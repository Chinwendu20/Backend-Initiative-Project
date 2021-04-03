from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Create your models here.





text_validation=[RegexValidator(regex=r'^[A-Z][\w .,]+[a-zA-Z]$', message='Ensure this is a valid input corresponding to the field, check help text')]
helptext='Input should start with capital letter, separate entities by comma and space only,numbers and special characters allowed'

	
class Movies(models.Model):
	Title=models.CharField(max_length=200, validators=text_validation, help_text=helptext)
	Producer=models.CharField(max_length=200, validators=text_validation, help_text=helptext)
	#Insert Cast
	Genre=models.CharField(max_length=200, validators=text_validation, help_text=helptext)
	Cast=models.CharField(max_length=200, validators=text_validation, help_text=helptext)
	#Insert Director
	Director=models.CharField(max_length=200, validators=text_validation, help_text=helptext)
	#Insert year of production
	Year_of_production=models.DecimalField(max_digits=4, decimal_places=0)

	class Meta:
		unique_together=(('Title', 'Producer', 'Genre', 'Cast', 'Director', 'Year_of_production'))

	def __str__(self):
		return self.Title


class Rentals(models.Model):
	Purchase_price=models.PositiveIntegerField()
	Ordered_by=models.ForeignKey(User, on_delete=models.CASCADE)
	#insert datefield
	Order_date=models.DateField(auto_now_add=True)
	#insert movie rented
	Ordered_Movie=models.ForeignKey('Movies', on_delete=models.CASCADE)