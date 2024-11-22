from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Profile

# Unregister Groups
admin.site.unregister(Group)

# Add Profile info to User
class ProfileInline(admin.StackedInline):
    model = Profile

# Extend User Model
class UserAdmin(admin.ModelAdmin):
    model = User
    # Only display username and profile fields
    fields = ["username"]
    inlines = [ProfileInline]

# Unregister initial User
admin.site.unregister(User)

# Reregister User and Profile
admin.site.register(User, UserAdmin)