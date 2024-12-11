from .models import Twix , Profile , Comment 
from django.db.models import Q
from  .forms import Twixform ,UserRegistrationForm , SearchFrom , ProfilePicForm , CommentForm
from django.shortcuts import get_object_or_404, redirect,render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib import messages






# Create your views here.

def home(request):
    return render(request , 'home.html')

@login_required
def twix_list(request):
    twixs = Twix.objects.all().order_by('-created_at').select_related('user')
    return render(request, 'twix_list.html', {'twixs':twixs})

def profile_list(request):
    if request.user.is_authenticated:
        profiles = Profile.objects.exclude(user=request.user)
        return render(request , 'profile_list.html', {'profiles':profiles})
    else:
        messages.success(request,("You Must Be Logged In To View This Page..."))
        return redirect('home')
    

def unfollow(request,pk):
    if request.user.is_authenticated:
        # get the profile to unfollow 
        profile= Profile.objects.get(user_id=pk)
        #unfollow the user
        request.user.profile.follows.remove(profile)
        # save our profile
        request.user.profile.save()

        #return message
        messages.success(request, (f"You Have Successfully Unfollowed {profile.user.username}"))
        return redirect(request.META.get('HTTP_REFERER'))

    else:
        messages.success(request, "You Must Be Logged In To View This Page...")
        return redirect('twix_list')
    

def follow(request,pk):
    if request.user.is_authenticated:
        # get the profile to follow 
        profile= Profile.objects.get(user_id=pk)
        #follow the user
        request.user.profile.follows.add(profile)
        # save our profile
        request.user.profile.save()

        #return message
        messages.success(request, (f"You Have Successfully Followed {profile.user.username}"))
        return redirect(request.META.get('HTTP_REFERER'))

    else:
        messages.success(request, "You Must Be Logged In To View This Page...")
        return redirect('twix_list')


def profile(request, pk):
    if request.user.is_authenticated:
        profile = get_object_or_404(Profile, user_id=pk) 
        twixs = Twix.objects.filter(user_id=pk)

        # Post Form Logic
        if request.method == "POST":
            # get current user
            current_user_profile = Profile.objects.get(user=request.user)
            action = request.POST.get('follow')  # Safely get the action
            
            if action == "unfollow":
                current_user_profile.follows.remove(profile)
            elif action == "follow":
                current_user_profile.follows.add(profile)
            current_user_profile.save()

        return render(request, "profile.html", {"profile": profile, 'twixs': twixs})
    else:
        messages.success(request, "You Must Be Logged In To View This Page...")
        return redirect('home')

def followers(request,pk):
    if request.user.is_authenticated:
        if request.user.id == pk:
            profiles = Profile.objects.get(user_id=pk)
            return render(request , 'followers.html', {'profiles':profiles})
        else:
            messages.success(request,("That is not you profile list."))
            return redirect('home')

    else:
        messages.success(request,("You Must Be Logged In To View This Page..."))
        return redirect('home')

def follows(request,pk):
    if request.user.is_authenticated:
        if request.user.id == pk:
            profiles = Profile.objects.get(user_id=pk)
            return render(request , 'follows.html', {'profiles':profiles})
        else:
            messages.success(request,("That is not you profile list."))
            return redirect('home')

    else:
        messages.success(request,("You Must Be Logged In To View This Page..."))
        return redirect('home')



@login_required
def twix_create(request):
    if request.method == "POST":
        form = Twixform(request.POST , request.FILES)
        if form.is_valid():
            twix = form.save(commit = False)
            twix.user = request.user
            twix.save()
            return redirect('twix_list')
    else:
        form = Twixform()
    return render(request , 'twix_form.html', {'form':form})



@login_required
def twix_edit(request, twix_id):
    twix = get_object_or_404(Twix , pk = twix_id , user = request.user)
    if request.method == 'POST':
        form = Twixform(request.POST , request.FILES , instance=twix)
        if form.is_valid():
            twix = form.save(commit= False)
            twix.user = request.user
            twix.save()
            return redirect('twix_list')
    else:
        form = Twixform(instance=twix)
    return render(request , 'twix_form.html', {'form':form})


@login_required
def twix_delete(request , twix_id):
    twix = get_object_or_404(Twix , pk=twix_id )
    if request.method == 'POST':
        twix.delete()
        return redirect('twix_list')
    return render(request ,'twix_confirm_delete.html', {'twix':twix})


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request , user)
            messages.success(request , ("You Have Successfully Registered! WELCOME!"))
            return redirect('home')
            
    else:
        form = UserRegistrationForm ()
    return render(request , 'registration/register.html', {'form':form})

def search_view(request):
    results = []
    query = None
    if request.method == 'GET':
        form = SearchFrom(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Twix.objects.filter(text__icontains=query)
        else:
            form = SearchFrom()
    return render(request, 'search.html' , {'form':form, 'results': results, 'query':query})

@login_required
def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id) 
        profile_user = Profile.objects.get(user__id=request.user.id) 
        user_form = UserRegistrationForm(request.POST or None, request.FILES or None, instance=current_user)
        
        profile_form = ProfilePicForm(request.POST or None, request.FILES or None,  instance= profile_user)

        
        if user_form.is_valid() and profile_form.is_valid():
                user_form.save()
                profile_form.save()
                login(request , current_user)
                messages.success(request, "Your profile has been updated successfully!")
                return redirect('profile', current_user.id) 
        
        return render(request, 'update_user.html', {'user_form': user_form, 'profile_form':profile_form}) 

    else:
        messages.error(request, "You must be logged in to view this page.")  
        return redirect('home')     
    


def twix_like(request,pk):
    if request.user.is_authenticated:
        twix = get_object_or_404(Twix, id=pk)
        if twix.likes.filter(id=request.user.id):
            twix.likes.remove(request.user)
        else:
            twix.likes.add(request.user)
        
        return redirect(request.META.get('HTTP_REFERER'))

    else:
        messages.error(request, "You must be logged in to view this page.") 
        return redirect('home')   

@login_required
def add_comment(request, pk):
    # Retrieve the Twix post
    twix = get_object_or_404(Twix, id=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            # Save the comment but don't commit to DB yet
            comment = form.save(commit=False)
            comment.twix = twix
            comment.user = request.user  # Associate the logged-in user with the comment
            comment.save()
            messages.success(request, "Your comment has been added.")
            return redirect('twix_list')  # Redirect to the twix list or detail view
        else:
            messages.error(request, "Error submitting the comment. Please try again.")
    else:
        form = CommentForm()

    return render(request, 'add_comment.html', {'form': form, 'twix': twix})




