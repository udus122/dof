from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class mypageView(LoginRequiredMixin, TemplateView):
    """mypage View"""
    template_name = 'mypage.html'


mypage_view = mypageView.as_view()


class diagnosisView(TemplateView):
    """diagnosis view"""
    template_name = 'diagnosis.html'


diagnosis_view = diagnosisView.as_view()
