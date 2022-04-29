from django.contrib import admin
from . models import CarMake, CarModel, CarDealer


# Register your models here.

# CarModelInline class
class CarModelInline(admin.StackedInline):
    model = CarModel
    extra = 2


# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('model_name', 'model_type', 'model_year')
    list_filter = ['model_year']
    search_fields = ['model_name', 'model_type']


# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]
    list_display = ('make_name', 'make_description')


# Register models here
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)