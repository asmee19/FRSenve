from django.contrib import admin
from .models import user
from .models import Contact

admin.site.register(user)

admin.site.register(Contact)

# Register your models here.
