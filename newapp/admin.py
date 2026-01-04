from django.contrib import admin
from .models import Member

class MemberAdmain(admin.ModelAdmin):
    list_display="firstname","lastname","email","phonenumber","country"

admin.site.register(Member,MemberAdmain)