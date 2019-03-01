from django.contrib import admin
from raccoonapp.models import Raccoon,Photo
# Register your models here.
#admin.site.register(Raccoon)

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass

class PhotoInline(admin.TabularInline):
    model = Photo
    extra=1

@admin.register(Raccoon)
class RaccoonAdmin(admin.ModelAdmin):
    pass
    list_display = ['name','age','parent']
    list_editable =['parent']
    list_filter=['parent','age']
    readonly_fields= ['admin_t']
    inlines= [PhotoInline]
