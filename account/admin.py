from django.contrib import admin
from .models import Account, Cart, FeedBack

# Register your models here.
admin.site.register(Account)
admin.site.register(Cart)
admin.site.register(FeedBack)
