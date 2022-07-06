from django.contrib import admin
from . models import Poll

# Register your models here.
class PollAdmin(admin.ModelAdmin):
    list_display = ('id','user','question','answer1','answer2','answer3','answer4')
    
admin.site.register(Poll,PollAdmin)