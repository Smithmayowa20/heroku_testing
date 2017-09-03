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
	followers = models.ManyToManyField(User,
			blank=True,related_name="followers")
	following = models.ManyToManyField(User,
			blank=True,related_name="following")
	
	def publish(self):
		self.save()
		
	def __str__(self):
		return str(self.slug)
		
	def follow(self,follow):
		self.following.add(follow)
		
	def follower(self,follower):
		self.followers.add(follower)
		

		
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
	user_profile = models.ForeignKey('User_Profile',
			blank=True,null=True)

	
	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.text
		
class File_upload(models.Model):
	file = models.FileField(
		blank=True,null=True)
	post = models.ForeignKey(Post,
		blank=True,null=True)
		
	def __str__(self):
		return str(self.file)
	
class Image_upload1(models.Model):
	image = models.ImageField(
		blank=True,null=True)
	post = models.ForeignKey(Post,
		blank=True,null=True)
		
	def __str__(self):
		return str(self.file)	

class Image_upload2(models.Model):
	image = models.ImageField(
		blank=True,null=True)
	post = models.ForeignKey(Post,
		blank=True,null=True)
		
	def __str__(self):
		return str(self.file)
		
class Image_upload3(models.Model):
	image = models.ImageField(
		blank=True,null=True)
	post = models.ForeignKey(Post,
		blank=True,null=True)
		
	def __str__(self):
		return str(self.file)
	
class Comment(models.Model):
	user = models.ForeignKey(User, blank=True, null=True)
	post = models.ForeignKey(Post, null=True)
	text = models.TextField()
	created_date = models.DateTimeField(
			default=timezone.now)
	published_date = models.DateTimeField(
			blank=True, null=True)
	position = models.PositiveSmallIntegerField(
			blank=True, null=True)
	parent_comment_no = models.PositiveSmallIntegerField(
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
			
'''class Following(models.Model):
	action = models.ForeignKey(User, related_name="custom_user_profile_action")
	reaction = models.ForeignKey(User, related_name="custom_user_profile_reaction" )'''

		
	
'''class Likes(models.Model):
	no_of_likes = models.IntegerField(
		blank=True, null=True)
	user = models.ForeignKey(User)'''
	