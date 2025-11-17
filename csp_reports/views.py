from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.viewsets import ModelViewSet
from .models import CSPViolationReport
from .serializers import CspViolationReportSerializer

class CspViewSet(ModelViewSet):
    queryset = CSPViolationReport.objects.all()
    serializer_class = CspViolationReportSerializer
    http_method_names = ['get', 'post']

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAdminUser()]
        return [AllowAny()]