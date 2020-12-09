from django.contrib import admin
from apps.dashboards.models import Dashboard


class DashboardAdmin(admin.ModelAdmin):
    fields = ('name', 'email', 'message')
    list_display = ('id', 'name', 'email', 'message')


admin.site.register(Dashboard, DashboardAdmin)
