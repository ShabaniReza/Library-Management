from rest_framework.serializers import ModelSerializer
from .models import CSPViolationReport

class CspViolationReportSerializer(ModelSerializer):
    class Meta:
        model = CSPViolationReport
        fields = ['id', 'blocked_uri', 'document_uri', 'violated_directive', 'report_time', 'full_report']
