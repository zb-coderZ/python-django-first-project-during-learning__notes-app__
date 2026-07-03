from django.contrib import admin
from .models import Note,store,certificate,Reviews


# Register your models here.
class reviewInline(admin.TabularInline):
    model=Reviews
    extra=2

class noteAdmin(admin.ModelAdmin):
    list_display=('name','created_At','description')
    inlines=[reviewInline]

class storeAdmin(admin.ModelAdmin):
    list_display=('name','location')
    filter_horizontal=('note_varities',)    

class certificateAdmin(admin.ModelAdmin):
    list_display=('certificate_name','issue_date')    

admin.site.register(Note,noteAdmin)
admin.site.register(store,storeAdmin)
admin.site.register(certificate,certificateAdmin)
