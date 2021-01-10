from django.contrib import admin
from .models import Post, Photo, Subject
from core.admin import CommonAdmin


class PhotoInline(admin.TabularInline):
    model = Photo
    show_change_link = True


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    pass


@admin.register(Post)
class PostAdmin(CommonAdmin):
    fieldsets = [
        (
            "Post Properties",
            {"fields": ("title", "content", "category", "created_by")},
        ),
        ("Many To Many Field", {"fields": ("subject",)}),
    ]
    filter_horizontal = ("subject",)
    list_display = ("id", "title", "category", "created_by")
    list_filter = CommonAdmin.list_filter + ("category", "created_by")
    inlines = [PhotoInline]
    search_fields = ("title",)
    list_display_links = ("title",)
