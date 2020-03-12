from uuid import uuid4
from django.db import models

class seller(models.models):
  #  "Information about the seller"
    name_book = models.CharField(max_length=50, editable=False, null=True)
    shotr_des = models.TextField(blank=True)
    genre = models.CharField(max_length=50, blank=True)
    publisher = models.CharField(max_length=50, blank=True)
    name_seller = models.CharField(max_length=50, editable=False, null=True)
    author = models.ForeignKey(author, on_delete=models.CASCADE)
    #author is defined as foreign key to link to author table
    isbn= models.UUIDField(primary_key=True, default=uuid4, editable=False)
    contact_no= models.IntegerField()
    def __book__(self):
        return self.name_book
    def __author__(self):
        return self.author
class borrower(models.Model):
   # "Informaiton about the borrower or User"
    name_book=models.CharField(max_length=50, editable=False, null=True)
    author=models.CharField(max_length=50, editable=False, null=True)
    name_borrower=models.CharField(max_length=50, editable=False, null=True)
    contact_no=models.IntegerField()
    def __book__(self):
        return self.name_book
    def __author__(self):
       return self.author
class author(models.Model):
    author=models.CharField(max_length=50, editable=False, null=True)