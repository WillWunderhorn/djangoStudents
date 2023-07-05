from django.contrib import admin
from django.utils.safestring import mark_safe

from students.entity.students import Students


class Admin(admin.ModelAdmin):
    readonly_fields = ['preview']
    list_display = ['id', 'name', 'age', 'preview']

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.profile_image.url}" width="200" height="112">')

    preview.short_description = 'Profile Image'


admin.site.register(Students, Admin)
