from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from .models import Genre, Post, User_Profile, Comment
from .forms import User_Profile_Form, CommentForm, PostForm
from registration.forms import RegistrationFormUniqueEmail
from django.template.defaultfilters import slugify
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
		
@login_required
def profile_page_edit(request,slug):
	profile = User_Profile.objects.get(slug=slug)
	if profile.user != request.user:
		raise Http404
	if request.method == 'POST':
		form = User_Profile_Form(request.POST,request.FILES,instance=profile)
		if form.is_valid():
			profile = form.save(commit=False)
			profile.publish()
			return redirect('profile_page')
	else:
		form = User_Profile_Form(instance=profile)	
		return render(request,'services/profile_page_edit.html',{'profile':profile,'form':form})
		
		
@login_required
def create_profile_page(request):
	form_class = User_Profile_Form
	if request.method == 'POST':
        # grab the data from the submitted form and
        # apply to the form
		form = form_class(request.POST, request.FILES)
		if form.is_valid():
            # check if user-instance in database
			
			# create a user-instance but don't save yet
			thing = form.save(commit=False)
			thing.user = request.user
			thing.slug = slugify(thing.user)
			# save the user-instance
			thing.publish()
			
			# redirect to user profile-page
			return redirect('profile_page')
	else:
		form = form_class()
		return(render(request,'services/create_profile_page.html',{'form':form,}))

def genre_follow(request,category):
	genre = Genre.objects.get(category=category)
	genre.add_follower(request.user)
	return redirect('all_categories')
		
def genre_unfollow(request,category):
	genre = Genre.objects.get(category=category)
	genre.remove_follower(request.user)
	return redirect('all_categories')
	
def get_picture(profile):
	if profile.profile_picture:
		return True
	else:
		return False
		
@login_required
def profile_page(request,user=None):
	try:
		if user:
			try:
				user1 = User.objects.get(username=user)
				profile = User_Profile.objects.get(user=user1)
				profile_followers = profile.followers.all()
				image = get_picture(profile)
				post_filter = (Post.objects.filter(user=user1))
				post = post_filter[:10]
				post_no = len(post_filter) if len(post_filter) else 0
			except User.DoesNotExist:
				profile = User_Profile.objects.get(user=user)
				profile_followers = profile.followers.all()
				image = get_picture(profile)
				post_filter = (Post.objects.filter(user=user))
				post = post_filter[:10]
				post_no = len(post_filter) if len(post_filter) else 0
		else:
			profile = User_Profile.objects.get(user=request.user)
			profile_followers = profile.followers.all()
			image = get_picture(profile)
			post_filter = (Post.objects.filter(user=request.user))
			post = post_filter[:10]
			post_no = len(post_filter) if len(post_filter) else 0
		return (render(request,'services/profile_page.html',{
		'profile':profile,'image':image,'post':post,'post_no':post_no,'profile_followers':profile_followers
		}))
	except User_Profile.DoesNotExist:
		if (user) and (user==request.user.username):
			return redirect('create_profile_page')
		else:
			return redirect('landing_page')
			
@login_required
def user_feed(request):
	try:
		user = User_Profile.objects.get(user=request.user)
	except User_Profile.DoesNotExist:
		return redirect('create_profile_page')
	following_users = user.following.all()
	following_post = Post.objects.filter(user__in=following_users)
	category_snippet = Genre.objects.all()
	promoted_post = (Post.objects.filter(front_page = True).order_by('-published_date'))[:5]
	user_follower = user.followers.all()
	user_following = user.following.all()
	context = {'post':following_post, 'promoted_post':promoted_post,
	'category':category_snippet, 'profile':user, 'user_follower':user_follower,
	'user_following':user_following}
	return (render(request,'services/user_feed.html',context))

		
def landing_page(request):
	if request.user.is_authenticated():
		'''post_dict = {}
		genre = (Genre.objects.all())
		try:
			genre_no = len(genre)
			for i in range(genre_no):
				post_genre = genre[i]
				post = Post.objects.filter(genre = post_genre, front_page = True).order_by('-published_date')
				post_key = str(post_genre.category)
				post_dict[post_key] = post
				post_key2 = str(post_genre.category) + "1"
				post_dict[post_key2] = post_genre.category
			#return (render(request,'services/landing_page.html',post_dict,))'''
		return redirect('user_feed')
		'''except:
			#return (render(request,'services/landing_page.html'))
			return redirect('user_feed')'''
	else:
		return (render(request,'services/landing_page22.html'))
	
@login_required	
def all_categories(request):
	genre = Genre.objects.all()
	return (render(request,'services/all_categories.html',{'genre':genre}))
	
@login_required	
def genre_category(request,category):
	genre = Genre.objects.get(category=category)
	post = Post.objects.filter(genre = genre, front_page = True).order_by('-published_date')
	post_2 = Post.objects.filter(genre = genre, front_page = False).order_by('-published_date')
	c = category
	paginator = Paginator(post_2, 10) # Show 25 contacts per page
	page = request.GET.get('page')
	try:
		post_2 = paginator.page(page)
	except PageNotAnInteger:
        # If page is not an integer, deliver first page.
		post_2 = paginator.page(1)
	except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
		post_2 = paginator.page(paginator.num_pages)
	return (render(request,'services/genre_category.html',{'post':post,'post_2':post_2,'category':c}))

	

class c:
	lis = []
	def commen(comment,post=None):
		if comment:
			for i in comment:
				x = Comment.objects.filter(parent_comment_no = i.pk)
				if len(x):
					c.lis.append(i)
					c.commen(x)
				else:
					c.lis.append(i)
			z = len(Comment.objects.filter(post=post))
			c.lis = c.lis[-z:]
			return(c.lis)
	
@login_required
def follow(request,user1):
	request_profile = User_Profile.objects.get(user=request.user)
	user_profile = User.objects.get(username=user1)
	person_profile = User_Profile.objects.get(user=user_profile)
	request_profile.follow(person_profile.user)
	person_profile.follower(request_profile.user)
	return redirect('profile_page2',user=person_profile.user)

	
@login_required
def unfollow(request,user1):
	request_profile = User_Profile.objects.get(user=request.user)
	user_profile = User.objects.get(username=user1)
	person_profile = User_Profile.objects.get(user=user_profile)
	request_profile.unfollow(person_profile.user)
	person_profile.unfollower(request_profile.user)
	return redirect('profile_page2',user=person_profile.user)
	
	
@login_required	
def new_post(request,category):
	form_class = PostForm
    # if we're coming from a submitted form, do this
	if request.method == 'POST':
        # grab the data from the submitted form and
        # apply to the form
		form = form_class(request.POST,request.FILES)
		if form.is_valid():
            # create an instance but don't save yet
			thing = form.save(commit=False)

            # set the additional details
			thing.user = request.user
			genre = Genre.objects.get(category = category)
			thing.genre = genre
			thing.front_page = False
			user_profile = User_Profile.objects.get(user=request.user)
			thing.user_profile = user_profile
            # save the object
			thing.publish()
			thing.tag()
            # redirect to our newly created thing
			return redirect('post_detail',pk=thing.pk)

    # otherwise just create the form
	else:
		form = form_class()
	return render(request,'services/new_post.html', {'form': form,})

@login_required
def post_detail(request,pk):
	#recent_post = (Post.objects.all().order_by('-published_date'))[0:5]
	post = get_object_or_404(Post, pk=pk)
	form = new_comment1(request,post)
	comm = Comment.objects.filter(post=post,position=1)
	comment = c.commen(comm,post)
	return (render(request,'services/post_detail.html',
	{'post':post,'comment':comment,'form':form,'tagged_users':post.user_tags.all()}))
	
@login_required		 
def new_comment(request,pk,position=0,parent_no=None):
	post = get_object_or_404(Post, pk=pk)
	form_class = CommentForm
    # if we're coming from a submitted form, do this
	if request.method == 'POST':
        # grab the data from the submitted form and
        # apply to the form
		form = form_class(request.POST)
		if form.is_valid():
            # create an instance but don't save yet
			thing = form.save(commit=False)

            # set the additional details
			thing.user = request.user
			thing.post = post
			#thing.post_slug = (thing.post).slug
			thing.position = int(position) + 1
			thing.parent_comment_no = parent_no
            # save the object
			thing.publish()
			
            # redirect to our newly created thing
			return redirect('post_detail', pk=post.pk)

    # otherwise just create the form
	else:
		form = form_class()

	return render(request,'services/new_comment.html', {
		'form': form,
	})

@login_required
def new_comment1(request,post,position=0,parent_no=None):
	form_class = CommentForm
    # if we're coming from a submitted form, do this
	if request.method == 'POST':
        # grab the data from the submitted form and
        # apply to the form
		form = form_class(request.POST)
		if form.is_valid():
            # create an instance but don't save yet
			thing = form.save(commit=False)

            # set the additional details
			if request.user.is_anonymous():
				pass
			else:
				thing.user = request.user
			thing.post = post
			#thing.post_slug = (thing.post).slug
			thing.position = int(position) + 1
			thing.parent_comment_no = parent_no
            # save the object
			thing.publish()
			
            # redirect to our newly created thing
			form_class = CommentForm
			form = form_class()
			return form

    # otherwise just create the form
	else:
		form = form_class()

	return form

	
@login_required
def edit(request,slug):
	post = Post.objects.get(slug=slug)
	if post.user != request.user:
		raise Http404
	if request.method == 'POST':
		form = PostForm(request.POST,instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.save()
			return redirect('post_detail',slug=post.slug)
	else:
		form = PostForm(instance=post)	
		return render(request,'services/edit.html',{'post':post,'form':form})