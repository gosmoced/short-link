from django.contrib import admin
from .models import Link, Click

class ClickAdmin(admin.ModelAdmin):
    list_display = ('link', 'ip_address', 'created_at')
    readonly_fields = ('created_at',)

admin.site.register(Link)
admin.site.register(Click, ClickAdmin)