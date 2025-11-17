from django.db import models

class CSPViolationReport(models.Model):
    blocked_uri = models.CharField(max_length=512, blank=True, null=True)
    document_uri = models.CharField(max_length=512)
    violated_directive = models.CharField(max_length=256)
    report_time = models.DateTimeField(auto_now_add=True)
    full_report = models.JSONField() 

    class Meta:
        ordering = ['-report_time']

    def __str__(self):
        return f"تخطی {self.violated_directive} در {self.document_uri}"