from django.db import models
from cake.models import *
from account.models import *
# Create your models here.
class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    cake = models.ForeignKey(Cake, on_delete=models.CASCADE, related_name='cake_reviews')
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='reviews_given')
    comment = models.TextField()
    rating = models.FloatField()
    date = models.DateField(auto_now_add=True)