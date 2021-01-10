from django.contrib import admin
from django.utils.safestring import mark_safe
from django.shortcuts import resolve_url
from .models import Comment, CComment
from core.admin import CommonAdmin


class CommonAdmin(CommonAdmin):
    fieldsets = [
        (
            "Comment Properties",
            {"fields": ("content",)},
        ),
    ]
    list_display = ("format_content", "created_by")
    list_filter = CommonAdmin.list_filter + ("created_by",)
    search_fields = ("content",)
    readonly_fields = ("deleted_at",)
    list_display_links = ("format_content",)

    def format_content(self, obj):
        return f"{obj.content[:12]}..."

    format_content.short_description = "content"


class CCommentInline(admin.TabularInline):
    model = CComment
    exclude = ("deleted_at",)
    show_change_link = True


@admin.register(Comment)
class CommentAdmin(CommonAdmin):
    inlines = [CCommentInline]
    fieldsets = CommonAdmin.fieldsets + [
        ("Relations", {"fields": ("created_by", "post")})
    ]
    list_display = (
        ("id",) + CommonAdmin.list_display + ("get_ccomment_count", "created_at")
    )

    def get_ccomment_count(self, obj):
        return obj.ccomment.count()

    get_ccomment_count.short_description = "ccomment count"


@admin.register(CComment)
class CCommentAdmin(CommonAdmin):
    fieldsets = (
        [("parent", {"fields": ("parent",)})]
        + CommonAdmin.fieldsets
        + [("Relations", {"fields": ("created_by",)})]
    )
    list_display = ("id", "parent_link") + CommonAdmin.list_display + ("created_at",)
    list_filter = ("parent",) + CommonAdmin.list_filter

    def parent_link(self, obj):
        # meta = obj._meta
        # meta.app_label # comment
        # meta.model_name # ccomment
        return mark_safe(
            '<a href="{}"><b>{}<b/></>'.format(
                resolve_url("admin:comment_comment_change", obj.parent_id),
                obj.parent,
            )
        )

    parent_link.short_description = "parent"
    parent_link.allow_tags = True
