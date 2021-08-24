from django.contrib import admin

from .models import Movie


@admin.action(description='Make selected as not enabled')
def make_not_enabled(modeladmin, request, queryset):
    queryset.update(is_enabled=False)


class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'is_enabled')
    search_fields = ('title', )
    ordering = ('title', )
    actions = (make_not_enabled, )


admin.site.register(Movie, MovieAdmin)
