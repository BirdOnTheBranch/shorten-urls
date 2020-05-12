from django.contrib import admin
from django.utils.html import format_html
from .models import Link


# Register your models here.
class AdminLink(admin.ModelAdmin):
    readonly_fields = ('create',)
    list_display = ('usuario', 'get_url','code')
    list_display_links = ('code',)
    ordering = ('create',)


    def get_url(self, obj):
        if obj.url:
            return format_html(f"<a href='{obj.url}' target='_blank' >{obj.url}</a>")

    get_url.short_description = 'url'


admin.site.register(Link, AdminLink)
