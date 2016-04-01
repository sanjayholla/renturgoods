from django.contrib import admin

from .models import PersonalInfo
from .models import Orders
from .models import Reviews
from .models import Product
from .models import Category
from .models import PersonalActivity

admin.site.register(PersonalInfo)
admin.site.register(Orders)
admin.site.register(Reviews)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(PersonalActivity)