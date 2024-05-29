from django.contrib import admin
from consumer_app.models import UserData,Product,Cart,CartHistory
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ["name","email"]#"service_title")#,"service_des")


class CartAdmin(admin.ModelAdmin):
    list_display = ["id",'email','product',"image",'quantity']#"service_title")#,"service_des")


class CartHistoryAdmin(admin.ModelAdmin):
    list_display = ["id",'email','product',"image",'quantity']#"service_title")#,"service_des")

admin.site.register(UserData,UserAdmin)
admin.site.register(Cart,CartAdmin)
admin.site.register(CartHistory,CartHistoryAdmin)
admin.site.register(Product)
