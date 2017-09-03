from django.contrib import admin

# Register your models here.


from .models import Post, Comment, User_Profile, Genre, File_upload

class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ( 'published_date','user','genre','text')


class CommentAdmin(admin.ModelAdmin):
	model = Comment
	list_display = ('post','user','text','published_date','position')

	
class User_ProfileAdmin(admin.ModelAdmin):
	model = User_Profile
	list_display = ('user','picture','link','short_bio')
	prepopulated_fields = {'slug': ('user',),}
	
class GenreAdmin(admin.ModelAdmin):
	model = Genre
	list_display = ('category','about')
		
class File_uploadAdmin(admin.ModelAdmin):
	model = File_upload
	list_display = ('file','post')
	
admin.site.register(Post,PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(User_Profile, User_ProfileAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(File_upload, File_uploadAdmin)

