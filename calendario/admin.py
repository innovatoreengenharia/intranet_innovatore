from django.contrib import admin

from .models import Events


class EventsAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "name", "start", "end", "public")
    list_display_links = (
        "user",
        "name",
    )
    search_fields = (
        "user",
        "name",
        "start",
    )
    list_filter = (
        "user",
        "name",
    )
    list_per_page = 20


admin.site.register(Events, EventsAdmin)
