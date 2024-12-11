from django.contrib import admin
from .models import Twix, Profile , Comment
from django.contrib.auth.models import User

# Register the Twix model
admin.site.register(Twix)
admin.site.register(Comment)

# Inline Profile editing within the User model admin
class ProfileInLine(admin.StackedInline):
    model = Profile

class UserAdmin(admin.ModelAdmin):
    model = User
    inlines = [ProfileInLine]

# Customize the Profile admin
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_modified', 'followers_count')  # Fields to show in the admin list view
    search_fields = ('user__username', 'user__email')  # Enable search by username or email

    # Method to count followers
    def followers_count(self, obj):
        return obj.followed_by.count()  # Count the number of followers
    followers_count.short_description = 'Followers'



