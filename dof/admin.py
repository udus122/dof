from django.contrib import admin

from dof.models import DiagnosisResult


class DiagnosisResultAdmin(admin.ModelAdmin):
    fields = [
        'ffs_type',
        'thinking_order',
        'strength',
        'stressor',
        'weakness',
        'advice',
    ]


admin.site.register(DiagnosisResult, DiagnosisResultAdmin)
