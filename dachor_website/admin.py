from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from dachor_website.models import Profile


class ProfileInline(admin.StackedInline):
    """
    Embedded/Inline version of django admin for Profile fields
    """
    model = Profile
    can_delete = False


class UserAdmin(BaseUserAdmin):
    """
    Adapt default django user admin view to include the fields from Profile
    """
    inlines = (ProfileInline,)


# Re-register UserAdmin with our custom version
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
