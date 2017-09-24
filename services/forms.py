
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
		widgets = {
            'parameters': Textarea(attrs={'cols': 3, 'rows': 1}),
   }
			
class CommentForm(ModelForm):
	class Meta:
		model = Comment
		fields = ('text',)
		widgets = {
            'parameters': Textarea(attrs={'cols': 30, 'rows': 1}),
   }
		
		
		
class User_Profile_Form(ModelForm):
	class Meta:
		model = User_Profile
		fields = ('first_name','middle_name','last_name','short_bio','profile_picture','link')
		widgets = {
            'parameters': Textarea(attrs={'cols': 30, 'rows': 1}),
   }
	