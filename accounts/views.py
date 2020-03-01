from allauth.account.views import LoginView, LogoutView, SignupView


class LoginView(LoginView):
    """
    ログインビュー
    """
    template_name = 'login.html'


login_view = LoginView.as_view()


class LogoutView(LogoutView):
    """
    ログアウトビュー
    """
    template_name = 'logout.html'


logout_view = LogoutView.as_view()


class SignupView(SignupView):
    """
    サインアップビュー
    """
    template_name = 'signup.html'


signup_view = SignupView.as_view()
