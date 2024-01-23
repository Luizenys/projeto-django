from django.contrib import admin
from .models import Shows

class ShowsAdmin(admin.ModelAdmin):
    list_display = ('local', 'endereco', 'data',)
    search_fields = ('local', 'endereco', 'data',)
    list_filter = ('local',)
    fields = ('local', 'endereco', 'data',)

admin.site.register(Shows, ShowsAdmin)
