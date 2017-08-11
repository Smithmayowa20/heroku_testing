from django.shortcuts import render, redirect
from django.conf import settings
from .models import Genre, Post, User_Profile, Comment, Following
from .forms import User_Profile_Form, CommentForm, PostForm, FollowingForm
from django.template.defaultfilters import slugify
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


def edit_profile_page(request):
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
			return redirect('profile_page2',user=thing.user)
	else:
		form = form_class()
		return(render(request,'services/edit_profile_page.html',{'form':form,}))

		
def profile_page(request,user=None):
	try:
		if user:
			try:
				profile = User_Profile.objects.get(user=user)
			except:
				profile = User_Profile.objects.get(user=user) 
		else:
			profile = User_Profile.objects.get(user=request.user)
		if profile.picture:
			image = True
		else:
			image = False
		return (render(request,'services/profile_page.html',{'profile':profile,'image':image}))
	except:
		return redirect('landing_page')
		
def landing_page(request):
	post_dict = {}
	genre = (Genre.objects.all())
	try:
		genre_no = len(genre)
		for i in range(genre_no):
			post_genre = genre[i]
			post = Post.objects.filter(genre = post_genre, front_page = True)
			post_key = str(post_genre.category)
			post_dict[post_key] = post
			post_key2 = str(post_genre.category) + "1"
			post_dict[post_key2] = post_genre.category
		return (render(request,'services/landing_page.html',post_dict,))
	except:
		return (render(request,'services/landing_page.html'))
	
def genre_category(request,category):
	genre = Genre.objects.get(category=category)
	post = Post.objects.filter(genre = genre, front_page = True)
	post_2 = Post.objects.filter(genre = genre, front_page = False)
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
				x = Comment.objects.filter(parent_comment_slug = i.slug)
				if len(x):
					c.lis.append(i)
					c.commen(x)
				else:
					c.lis.append(i)
			z = len(Comment.objects.filter(post=post))
			c.lis = c.lis[-z:]
			return(c.lis)
	

def create_follower_following(request,user1):
	following_class = FollowingForm
	person_profile = User_Profile.objects.get(user=user1)
	person = person_profile.user
	form = following_class(request.GET)
	form.action = request.user
	form.reaction = person
	form.save()
	return redirect('profile_page')
	
def new_post(request,category):
	form_class = PostForm
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
			thing.slug = slugify(thing.text,)
			genre = Genre.objects.get(category = category)
			thing.genre = genre
			
            # save the object
			thing.publish()

            # redirect to our newly created thing
			return redirect('post_detail',slug=thing.slug)

    # otherwise just create the form
	else:
		form = form_class()

	return render(request,'services/new_post.html', {
		'form': form,
	})
	
def post_detail(request,slug):
	recent_post = (Post.objects.all().order_by('-published_date'))[0:5]
	post = Post.objects.get(slug=slug)
	form = new_comment(request,post)
	comm = Comment.objects.filter(post=post,position=1)
	comment = c.commen(comm,post)
	return (render(request,'services/post_detail.html',{'post':post,'comment':comment,'form':form,'recent':recent_post}))
	
		 
def new_comment1(request,slug,position=0,parent_slug=None):
	post = Post.objects.get(slug=slug)
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
			thing.slug = slugify(thing.text,)
			thing.position = int(position) + 1
			thing.parent_comment_slug = parent_slug
            # save the object
			thing.publish()
			
            # redirect to our newly created thing
			return redirect('post_detail', slug=post.slug)

    # otherwise just create the form
	else:
		form = form_class()

	return render(request,'services/new_comment.html', {
		'form': form,
	})

def new_comment(request,post,position=0,parent_slug=None):
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
			thing.slug = slugify(thing.text,)
			thing.position = int(position) + 1
			thing.parent_comment_slug = parent_slug
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