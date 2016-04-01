from __future__ import unicode_literals

from django.db import models

# Create your models here.
class PersonalInfo(models.Model):
    #id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=30, default='noName')
    email = models.CharField(max_length=50)
    passwd = models.CharField(max_length=30, default='noPasswd')
    phNo = models.CharField(max_length=13, default='noNumber')
    address = models.CharField(max_length=100, default='noAddress')
    pincode = models.CharField(max_length=7, default='noCode')
    joinedOn = models.DateField()
    genderIsMale = models.BooleanField(default=False)
    def __unicode__(self):
      return self.id
#    displayPicture = models.ImageField(upload_to=upload_to='uploads/')

class AccountLoginDetails(models.model):
	personalInfoId = models.ForeignKey(PersonalInfo)
	verify = models.BooleanField(default=False)
	signedUpWithFB = models.BooleanField(default=False)
	def __unicode__(self):
      return self.id

class PersonalActivity(models.Model):
    personalInfoId = models.ForeignKey(PersonalInfo)
    lenderRating = models.DecimalField(max_digits=2, decimal_places=1)
    borrowerRating = models.DecimalField(max_digits=2, decimal_places=1)
    numberOfLenderRating = models.PositiveSmallIntegerField(default=0)
    numberOfBorrowerRating = models.PositiveSmallIntegerField(default=0)
    favourites = models.CharField(max_length=200, default='noFavourites')
    def __unicode__(self):
      return self.personalInfoId

class Category(models.Model):
    #id = models.PositiveIntegerField(primary_key=True)				#Not required. It's what django does by default with name id only
    name = models.CharField(max_length=25, blank='noCategoryName')
    parentId = models.ForeignKey(Category)						#foreignkey to same field can be done acc. to stackoverflow. I think you wanted this only
    def __unicode__(self):
      return self.id

class Product(models.Model):
    #id = models.PositiveIntegerField(primary_key=True)
    lender_id = models.ForeignKey(PersonalInfo)
    category_id = models.ForeignKey(Category)
    name = models.CharField(max_length=20, default='noName')
    description = models.CharField(max_length=160, default='noDescription')
    amount = models.PositiveSmallIntegerField()
    securityDeposit = models.PositiveIntegerField()
    addedDate = models.DateField() #Added this
    def __unicode__(self):
      return self.id
#To add the fine in db. Need some ideas

class Orders(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    borrower_id = models.ForeignKey(PersonalInfo)
    product_id = models.ForeignKey(Product)
    amount = models.PositiveSmallIntegerField()
    securityDeposit = models.PositiveIntegerField()
    finePaid = models.DecimalField(max_digits=4, decimal_places=1) #If we make a fine table, this will become redundant
    transactionDate = models.DateField()
    status = models.PositiveSmallIntegerField()
    address = models.CharField(max_length=100, default='noAddress')
    def __unicode__(self):
      return self.id

class Reviews(models.Model):
    product_id = models.ForeignKey(Orders)
    reviewBy = models.PositiveIntegerField(PersonalInfo)
    reviewFor = models.ForeignKey(PersonalInfo)
    star = models.DecimalField(max_digits=1, decimal_places=0)
    comment = models.CharField(max_length=500, default='noComment')                #how to make it varchar- WHY?
    uploadDate = models.DateField()
    numberOfUpvotes = models.PositiveSmallIntegerField()
                                                                                #Provide option of upvotes- WTF IS THIS: PARIJAT
    forBorrower = models.BooleanField(default=False)
    def __unicode__(self):
      return self.id

class votes(models.Model):
	reviewId = models.ForeignKey(Reviews)
	personalInfoId = models.ForeignKey(PersonalInfo)
	voteIsUpvote = models.BooleanField(default=True)