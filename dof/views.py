from django.views.generic.base import TemplateView


class mypageView(TemplateView):
    """mypage View"""
    template_name = 'mypage.html'


mypage_view = mypageView.as_view()


class diagnosisView(TemplateView):
    """diagnosis view"""
    template_name = 'diagnosis.html'


diagnosis_view = diagnosisView.as_view()
