from django import forms
from .models import Twix , Profile , Comment
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User 


class Twixform(forms.ModelForm):
    class Meta :
        model = Twix
        fields = ['text' , 'photo']


# class UserRegistrationForm(UserCreationForm):
#     email = forms.EmailField()
#     class Meta:
#         model = User
#         fields = ('username' ,'email','password1', 'password2')
#         # widgets = {
#         #     'username': forms.TextInput(attrs={'class': 'bg-white text-black p-2 rounded'}),
#         #     'email': forms.EmailInput(attrs={'class': 'bg-white text-black p-2 rounded'}),
#         #     'password1': forms.PasswordInput(attrs={'class': 'bg-white text-black p-2 rounded'}),
#         #     'password2': forms.PasswordInput(attrs={'class': 'bg-white text-black p-2 rounded'}),
#         # }



# profile extras form


class ProfilePicForm(forms.ModelForm):

    profile_image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'bg-black text-white p-2 rounded w-full'}), required=False)
    profile_bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'bg-black text-white p-2 rounded w-full'}), required=False)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'bg-black text-white p-2 rounded w-full'}), required=False)
    facebook_link = forms.URLField(widget=forms.URLInput(attrs={'class': 'bg-black text-white p-2 rounded w-full'}), required=False)
    instagram_link = forms.URLField(widget=forms.URLInput(attrs={'class': 'bg-black text-white p-2 rounded w-full'}), required=False)
    linkedin_link = forms.URLField(widget=forms.URLInput(attrs={'class': 'bg-black text-white p-2 rounded w-full'}), required=False)

    class Meta:
        model = Profile
        fields = ['profile_image', 'profile_bio', 'email', 'facebook_link', 'instagram_link', 'linkedin_link']

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for field in self.fields.values():
    #         field.widget.attrs.update({'class': 'bg-black text-white p-2 rounded w-full'})


# class ProfilePicForm(forms.ModelForm):
#     profile_image = forms.ImageField(
#         label="Profile Picture",
#         widget=forms.ClearableFileInput(attrs={
#             'class': 'bg-black text-white p-2 rounded w-full',
#         })
#     )
#     profile_bio = forms.CharField(
#         label="Profile Bio",
#         widget=forms.Textarea(attrs={
#             'class': 'bg-black text-white p-2 rounded w-full',
#             'placeholder': 'Profile Bio',
#             'rows': 4,
#         })
#     )
#     email = forms.CharField(
#         label="Email",
#         widget=forms.TextInput(attrs={
#             'class': 'bg-black text-white p-2 rounded w-full',
#             'placeholder': 'Email Link',
#             'type': 'url',
#         }),
#         required=False
#     )
#     facebook_link = forms.CharField(
#         label="Facebook Link",
#         widget=forms.TextInput(attrs={
#             'class': 'bg-black text-white p-2 rounded w-full',
#             'placeholder': 'Facebook Link',
#             'type': 'url',
#         }),
#         required=False
#     )
#     instagram_link = forms.CharField(
#         label="Instagram Link",
#         widget=forms.TextInput(attrs={
#             'class': 'bg-black text-white p-2 rounded w-full',
#             'placeholder': 'Instagram Link',
#             'type': 'url',
#         }),
#         required=False
#     )
#     linkedin_link = forms.CharField(
#         label="LinkedIn Link",
#         widget=forms.TextInput(attrs={
#             'class': 'bg-black text-white p-2 rounded w-full',
#             'placeholder': 'LinkedIn Link',
#             'type': 'url',
#         }),
#         required=False
#     )

#     class Meta:
#         model = Profile
#         fields = ('profile_image', 'profile_bio', 'email_link', 'facebook_link', 'instagram_link', 'linkedin_link')






class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'bg-black text-white p-2 rounded w-full',
            'placeholder': 'Enter your email',
            'type': 'email'
        })
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'bg-black text-white p-2 rounded w-full',
            'placeholder': 'Enter your username',
            'type': 'text'
        })
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'bg-black text-white p-2 rounded w-full',
            'placeholder': 'Enter your password',
            'type': 'password'
        })
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'bg-black text-white p-2 rounded w-full',
            'placeholder': 'Confirm your password',
            'type': 'password'
        })
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')



class SearchFrom(forms.Form):
    query = forms.CharField(label ='Search' , max_length=100)



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']  # Only need to include text now
        
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'bg-black text-white p-2 rounded w-full',
                'placeholder': 'Your Comment...',
            }),
        }
        
        required = {
            'text': True,  # Text is required
        }
       