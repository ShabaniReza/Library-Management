from django.urls import path
from . import views

urlpatterns = [
    path('csp-reports/', views.csp_report_view, name='csp_reports'),
]