from allauth.account import views as auth_view


class LoginView(auth_view.LoginView):
    """
    ログインビュー
    """
    template_name = 'login.html'


login_view = LoginView.as_view()


class LogoutView(auth_view.LogoutView):
    """
    ログアウトビュー
    """
    template_name = 'logout.html'


logout_view = LogoutView.as_view()


class SignupView(auth_view.SignupView):
    """
    サインアップビュー
    """
    template_name = 'signup.html'


signup_view = SignupView.as_view()


class PasswordResetView(auth_view.PasswordResetView):
    """
    パスワードリセットビュー
    """
    template_name = 'password_reset.html'


password_reset_view = PasswordResetView.as_view()


class PasswordResetDoneView(auth_view.PasswordResetDoneView):
    """
    パスワードリセットビュー
    """
    template_name = 'password_reset_done.html'


password_reset_done_view = PasswordResetDoneView.as_view()


class PasswordResetFromKeyView(auth_view.PasswordResetFromKeyView):
    """
    パスワードリセットビュー
    """
    template_name = 'password_reset_from_key.html'


password_reset_from_key_view = PasswordResetFromKeyView.as_view()


class PasswordResetFromKeyDoneView(auth_view.PasswordResetFromKeyDoneView):
    """
    パスワードリセットビュー
    """
    template_name = 'password_reset_from_key_done.html'


password_reset_from_key_done_view = PasswordResetFromKeyDoneView.as_view()
