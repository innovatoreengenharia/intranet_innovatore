from django.contrib import admin
from .models import Post, Comentarios, Like


class PostAdmin(admin.ModelAdmin):
    list_display = ("user",)
    list_display_links = ("user",)
    search_fields = ("user",)
    list_filter = ("user",)
    list_per_page = 15


admin.site.register(Post, PostAdmin)


class ComentariosAdmin(admin.ModelAdmin):
    list_display = ("user",)
    list_display_links = ("user",)
    search_fields = ("user",)
    list_filter = ("user",)
    list_per_page = 15


admin.site.register(Comentarios, ComentariosAdmin)


class LikeAdmin(admin.ModelAdmin):
    list_display = ("id", "post", "user")


admin.site.register(Like, LikeAdmin)
