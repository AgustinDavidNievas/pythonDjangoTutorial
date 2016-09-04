from django.contrib import admin
from polls.models import Poll #asi funciona desde la consola, pero el eclipse lo marca como bug
#from pruebaDj.polls.models import Poll #asi se arregla el bug pero no funciona desde la consola por el path
from polls.models import Choice
# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):#PollAdmin hereda de ModelAdmin
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    
    intlines = [ChoiceInline]
    list_display = ('question', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question']

admin.site.register(Poll,PollAdmin)
admin.site.register(Choice)