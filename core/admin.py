from django.contrib import admin
from django.utils.html import format_html
from .models import Link


# Register your models here.
class AdminLink(admin.ModelAdmin):
    readonly_fields = ('create',)
    list_display = ('usuario', 'get_url','get_code')
    ordering = ('create',)


    def get_url(self, obj):
        if obj.url:
            return format_html(f"<a href='{obj.url}' target='_blank' >{obj.url}</a>")

    get_url.short_description = 'url'


    def get_code(self, obj):
        if obj.code:
            return format_html(f"<a href='http://127.0.0.1:8000/{obj.code}' target='_blank' >{obj.code}</a>")

    get_code.short_description = 'code'


admin.site.register(Link, AdminLink)
