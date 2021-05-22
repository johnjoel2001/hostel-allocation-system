from django.contrib import admin
from.models import*
from accounts.models import Contact
from accounts.models import Choice


admin.site.register(Contact)

admin.site.register(Student)

admin.site.register(Choice)

# Register your models here.
