from django.db import models


# Create your models here.
from django.utils import timezone
from django.contrib.auth.models import User


class User_Profile(models.Model):
	slug = models.SlugField(unique=True)
	short_bio = models.TextField(
			blank=True, null=True)
	picture = models.ImageField("Image", upload_to="images/",
			blank=True, null=True)
	user = models.OneToOneField(User, blank=True, null=True)
	link = models.Url = models.URLField(
			blank=True, null=True)
	
	def publish(self):
		self.save()
		
	def __str__(self):
		return str(self.slug)
		

class Post(models.Model):
	genre = models.ForeignKey('Genre',
			blank=True,null=True)
	user = models.ForeignKey(User,
			blank=True, null=True)
	front_page = models.BooleanField(
			default = False)
	text = models.TextField(
			blank=True,null=True)
	created_date = models.DateTimeField(
			default=timezone.now)
	published_date = models.DateTimeField(
			blank=True, null=True)
	slug = models.SlugField(unique=True)
	
	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.slug
		
class Comment(models.Model):
	user = models.ForeignKey(User, blank=True, null=True)
	post = models.ForeignKey(Post, null=True)
	text = models.TextField()
	slug = models.SlugField(unique=True)
	created_date = models.DateTimeField(
			default=timezone.now)
	published_date = models.DateTimeField(
			blank=True, null=True)
	position = models.PositiveSmallIntegerField(
			blank=True, null=True)
	parent_comment_slug = models.SlugField(
	blank=True, null=True)
	
	def publish(self):
		self.published_date = timezone.now()
		self.save()
		
	def __str__(self):
		return self.text
		
class Genre(models.Model):
	category = models.CharField(max_length=200)
	about = models.CharField(max_length=200,
			blank=True, null=True)
			
class Following(models.Model):
	action = models.ForeignKey(User, related_name="custom_user_profile_action")
	reaction = models.ForeignKey(User, related_name="custom_user_profile_reaction" )

		
	
'''class Likes(models.Model):
	no_of_likes = models.IntegerField(
		blank=True, null=True)
	user = models.ForeignKey(User)'''
	