from django.contrib import admin
from .models import Tip

class TipAdmin(admin.ModelAdmin):
	model = Tip
	fields = ['content',]

admin.site.register(Tip, TipAdmin)

# Register your models here.
