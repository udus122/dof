from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, RedirectView
from django.shortcuts import redirect
from django.contrib.auth import get_user_model

from .models import Diagnosis
from .forms import DiagnosisForm


class MypageView(LoginRequiredMixin, TemplateView):
    """mypage View"""
    template_name = 'mypage.html'


mypage_view = MypageView.as_view()


class DiagnosisRedirectView(LoginRequiredMixin, RedirectView):
    url = '/diagnosis/1/'


diagnosis_redirect_view = DiagnosisRedirectView.as_view()


class DiagnosisView(LoginRequiredMixin, TemplateView):
    """diagnosis view"""
    template_name = 'diagnosis.html'
    form_class = DiagnosisForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = self.get_object()
        context['next_qn'] = int(self.kwargs.get('qn')) + 1
        return context

    def get_object(self):
        qn = self.kwargs.get('qn')
        obj = Diagnosis.objects.get(qn=qn)
        return obj

    def get_form(self):
        return self.form_class

    def save_result_redirect(self, request, form):
        """
        診断結果をユーザーモデルへ保存し、マイページへリダイレクトする
        """
        if form.is_valid():
            uuid = request.user.uuid
            login_user = get_user_model().objects.get(uuid=uuid)
            login_user.a_factor = form.cleaned_data['A']
            login_user.b_factor = form.cleaned_data['B']
            login_user.c_factor = form.cleaned_data['C']
            login_user.d_factor = form.cleaned_data['D']
            login_user.e_factor = form.cleaned_data['E']
            print(
                login_user.a_factor,
                login_user.b_factor,
                login_user.c_factor,
                login_user.d_factor,
                login_user.e_factor
            )
            login_user.save()
            # ffs_type(91type)の分類
            login_user.ffs_type = login_user.get_ffs_type()
            login_user.save()

            return redirect('mypage', permanent=True)

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        form = self.get_form()
        context['form'] = form()
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        form = self.get_form()
        form = form(request.POST)
        if form.is_valid():
            context['form'] = form

        if self.kwargs.get('qn') == 51:
            return self.save_result_redirect(request, form)

        return self.render_to_response(context)


diagnosis_view = DiagnosisView.as_view()
