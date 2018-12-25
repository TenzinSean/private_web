from django.contrib import admin
from .models import (
                Blog,
                Travel,
                PhotoCollection,
                StoryModel,
                Portofilo,
                Projects,
                Pola,
                Family
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
