
from django.forms import ModelForm, Textarea, CharField, RadioSelect

from .models import Post, Comment, User_Profile, Following

from registration.forms import RegistrationFormUniqueEmail
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

class RegistroperfilForm(RegistrationFormUniqueEmail):
	first_name = CharField(required = True)
	last_name = CharField(required = True)
	#kind_of_user = CharField(widget = RadioSelect(choices=TIPO))

class PostForm(ModelForm):
	class Meta:
		model = Post
		fields = ('text',)
		widgets = {
            'text': SummernoteWidget(),
        }
			
class CommentForm(ModelForm):
	class Meta:
		model = Comment
		fields = ('text',)
		widgets ={
			'summary' : Textarea(attrs={'rows':80, 'cols':20}),
			}
		
class FollowingForm(ModelForm):
	class Meta:
		model = Following
		fields = ('action','reaction')
		
		
class User_Profile_Form(ModelForm):
	class Meta:
		model = User_Profile
		fields = ('short_bio','picture','link')