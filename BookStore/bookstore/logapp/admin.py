from django.contrib import admin
from .models import User
import csv
from django.http import HttpResponse

# Register your models here.
# admin.site.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=['first_name','email','phonenumber']
admin.site.register(User,UserAdmin)
def export_log(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="User.csv"'
    writer = csv.writer(response)
    writer.writerow(['Usename', 'Phonenumber','Email'])
    user = queryset.values_list('first_name', 'phonenumber','email')
    for i in user:
        writer.writerow(i)
    return response


export_log.short_description = 'Export to csv'
