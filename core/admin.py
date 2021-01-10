from django.contrib import admin
from django.contrib.admin.filters import SimpleListFilter


class DeletedFilter(SimpleListFilter):
    title = "deleted"
    parameter_name = "deleted_at"

    def lookups(self, request, model_admin):
        return [("true", "true"), ("false", "false")]

    def queryset(self, request, queryset):
        if self.value() == "true":
            return queryset.filter(deleted_at__isnull=True)
        elif self.value() == "false":
            return queryset.filter(deleted_at__isnull=False)


class CommonAdmin(admin.ModelAdmin):
    list_filter = (DeletedFilter,)
