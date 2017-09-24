
from django.forms import ModelForm, Textarea, CharField, RadioSelect

from .models import Post, Comment, User_Profile

from registration.forms import RegistrationFormUniqueEmail
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

class RegistroperfilForm(RegistrationFormUniqueEmail):
	first_name = CharField(required = True)
	last_name = CharField(required = True)

class PostForm(ModelForm):
	text = CharField(
        widget = Textarea(),
)
	class Meta:
		model = Post
		fields = ('text','image1','image2','image3','file')

			
class CommentForm(ModelForm):
	text = CharField(
        widget = Textarea(),
)
	class Meta:
		model = Comment
		fields = ('text',)
		
		
class User_Profile_Form(ModelForm):
	short_bio = CharField(
        widget = Textarea(),
)
	class Meta:
		model = User_Profile
		fields = ('first_name','middle_name','last_name','short_bio','profile_picture','link')
		
