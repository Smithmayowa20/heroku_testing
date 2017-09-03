
from django.forms import ModelForm, Textarea, CharField, RadioSelect

from .models import Post, Comment, User_Profile, File_upload, Image_upload1, Image_upload2, Image_upload3

from registration.forms import RegistrationFormUniqueEmail
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

class RegistroperfilForm(RegistrationFormUniqueEmail):
	first_name = CharField(required = True)
	last_name = CharField(required = True)

class PostForm(ModelForm):
	class Meta:
		model = Post
		fields = ('text',)

			
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
		
		
class File_upload_Form(ModelForm):
	class Meta:
		model = File_upload
		fields = ('file',)
		
class Image_upload1_Form(ModelForm):
	class Meta:
		model = Image_upload1
		fields = ('image',)
		
class Image_upload2_Form(ModelForm):
	class Meta:
		model = Image_upload2
		fields = ('image',)
		
class Image_upload3_Form(ModelForm):
	class Meta:
		model = Image_upload3
		fields = ('image',)