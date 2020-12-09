from rest_framework import serializers
from apps.dashboards.models import Dashboard


# User dashboard serializer

class DashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dashboard
        fields = "__all__"
