from django.contrib import admin

from .models import Movie, Person


@admin.action(description='Make selected as not enabled')
def make_not_enabled(modeladmin, request, queryset):
    queryset.update(is_enabled=False)


class MovieCrewInline(admin.TabularInline):
    model = Movie.persons.through


class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'gender')
    search_fields = ('first_name', 'last_name')
    ordering = ('last_name', )
    inlines = (MovieCrewInline, )


class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'is_enabled')
    search_fields = ('title', )
    ordering = ('title', )
    actions = (make_not_enabled, )
    inlines = (MovieCrewInline, )


admin.site.register(Person, PersonAdmin)
admin.site.register(Movie, MovieAdmin)
