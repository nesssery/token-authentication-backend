from rest_framework import viewsets, permissions
from apps.dashboards.serializers import DashboardSerializer
from apps.dashboards.models import Dashboard


# User dashboard viewset

class DashboardViewSet(viewsets.ModelViewSet):
    queryset = Dashboard.objects.all()

    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = DashboardSerializer

    def get_queryset(self):
        return self.request.user.leads.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

