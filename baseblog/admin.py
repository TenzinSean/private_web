from django.contrib import admin
from .models import (
                Blog,
                Travel,
                PhotoCollection,
                StoryModel,
                Portofilo,
                Projects,
                Pola,
                Family,
                Comment
                )

# Register your models here.

admin.site.register(Blog)
admin.site.register(Travel)
admin.site.register(PhotoCollection)
admin.site.register(StoryModel)
admin.site.register(Portofilo)
admin.site.register(Projects)
admin.site.register(Pola)
admin.site.register(Family)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')
