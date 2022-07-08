from django.contrib import admin
from .models import Designation_Mst,Employee_Mst
# Register your models here.
@admin.register(Designation_Mst)
class admina(admin.ModelAdmin):
    list_display=['id','designaton']


@admin.register(Employee_Mst)
class admina(admin.ModelAdmin):
    list_display=['id','first_name','last_name','designationld','date_of_joining','salary']
