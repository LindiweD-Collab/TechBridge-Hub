
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Client, Project, Task, Communication

class ProjectInline(admin.TabularInline):
    model = Project
    extra = 0  
    fields = ('title', 'status', 'start_date', 'end_date') 
    show_change_link = True 


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    """
    Customizes the Admin view for the Client model.
    """
 
    list_display = ('name', 'contact_person_name', 'contact_email', 'date_added')
 
    search_fields = ('name', 'contact_email')
 
    inlines = [ProjectInline]


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    """
    Customizes the Admin view for the Project model.
    """
    list_display = ('title', 'client', 'status', 'start_date', 'end_date')
 
    list_filter = ('status', 'client')
    search_fields = ('title', 'description')
   
    autocomplete_fields = ('client',)

admin.site.register(User, UserAdmin)

admin.site.register(Task)
admin.site.register(Communication)
