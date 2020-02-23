from django.contrib.auth.models import PermissionsMixin, UserManager
from django.core.mail import send_mail
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext as _
from django.utils import timezone
from django.db import models


from uuid import uuid4


class CustomUserManager(UserManager):
    """Define a model manager for User model with username field"""

    user_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create abd save a User with the given email and password"""
        if not email:
            raise ValueError('The given must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')

        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """拡張ユーザーモデル"""

    uuid = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)

    is_staff = models.BooleanField(
        _('is staff'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.')
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_('Designates whether the user should be treated as active.\nUnselect this instead of deleting accounts.')
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = CustomUserManager()

    EMAIl_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        full_name = '{} {}'.format(self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

    @property
    def username(self):
        """
        username属性のゲッター
        他のアプリケーションが、username属性にアクセスしたバアに備えて定義メールアドレスを返す
        """
        return self.email
