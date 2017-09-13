
from django.forms import ModelForm, Textarea, CharField, RadioSelect

from .models import Post, Comment, User_Profile

from registration.forms import RegistrationFormUniqueEmail
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

class RegistroperfilForm(RegistrationFormUniqueEmail):
	first_name = CharField(required = True)
	last_name = CharField(required = True)

class PostForm(ModelForm):
	class Meta:
		model = Post
		fields = ('text','image1','image2','image3','file')

			
class CommentForm(ModelForm):
	class Meta:
		model = Comment
		fields = ('text',)
		widgets ={
			'summary' : Textarea(attrs={'rows':80, 'cols':20}),
			}
		
		
class User_Profile_Form(ModelForm):
	class Meta:
		model = User_Profile
		fields = ('short_bio','picture','link')
		
