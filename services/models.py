from django.db import models

# Create your models here.
from django.utils import timezone
from django.contrib.auth.models import User

 
class User_Profile(models.Model):
	surname = models.CharField(max_length = 32,
			blank=True,null=True)
	name = models.CharField(max_length = 32,
			blank=True,null=True)
	middlename = models.CharField(max_length = 32,
			blank=True,null=True)
	slug = models.SlugField(unique=True)
	short_bio = models.TextField(
			blank=True, null=True)
	profile_picture = models.ImageField( upload_to="images/",
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
		
	def unfollow(self,unfollow):
		self.following.remove(unfollow)
		
	def unfollower(self,unfollower):
		self.followers.remove(unfollower)

		
class Post(models.Model):
	genre = models.ForeignKey('Genre',
			blank=True,null=True)
	user = models.ForeignKey(User,
			blank=True, null=True)
	front_page = models.BooleanField(
			default = False)
	tag_users = models.CharField(max_length=250,
			blank=True,null=True,
			help_text='''tag single or several users with @username followed by space 
			\n e.g @tanya340 @mark for several users\n and @tanya for single user''')
	user_tags = models.ManyToManyField(User,
			blank=True, related_name="user_tags")
	text = models.TextField(
			blank=True,null=True)
	image1 = models.ImageField(
			blank=True,null=True)
	image2 = models.ImageField(
			blank=True,null=True)
	image3 = models.ImageField(
			blank=True,null=True)
	file = models.FileField(
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

	def tag(self):
		lis = []
		if self.tag_users:
			t = self.tag_users.split()
			for i in t:
				if '@' in i:
					lis.append(i[1:])
		r = User.objects.filter(username__in=lis)
		self.user_tags.add(*r)
		
	def __str__(self):
		return self.text
		
	
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
	