from django.contrib import admin
from .models import Customer, Employee, Item, Vehicle, Plan,ItemPlan
from .models import Item, ItemizedBilling, ItemCost,LaberCost
from .models import QuestionPhotoService, Photo, Question

# Register your models here.

admin.site.register(Customer)
admin.site.register(Employee)
admin.site.register(Vehicle)
admin.site.register(Plan)
admin.site.register(ItemPlan)
admin.site.register(Item)
admin.site.register(ItemizedBilling)
admin.site.register(ItemCost)
admin.site.register(LaberCost)
admin.site.register(QuestionPhotoService)
admin.site.register(Photo)
admin.site.register(Question)
