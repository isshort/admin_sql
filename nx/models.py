from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.utils.safestring import mark_safe
from django.utils.translation import gettext as _


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
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
        extra_fields.setdefault('date_creation', timezone.now())
        extra_fields.setdefault('date_update', timezone.now())
        extra_fields.setdefault('status', 1)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class Users(AbstractUser):
    guid = models.CharField(max_length=280)
    login = models.CharField(max_length=240, unique=True)
    username = models.CharField(max_length=240, blank=True, db_column="username")
    USERNAME_FIELD = 'login'
    first_name = models.CharField(_('first name'), max_length=100, db_column='firstname', blank=True)
    last_name = models.CharField(_('first name'), max_length=100, db_column='lastname', blank=True)
    email = models.EmailField(_('email address'), blank=True)
    phone = models.CharField(max_length=20, blank=True)
    photo = models.ImageField(upload_to=_("AdminPhoto"))
    u_group = models.CharField(max_length=280)
    u_verify = models.CharField(max_length=280)
    date_creation = models.CharField(max_length=280)
    date_update = models.CharField(max_length=280)
    status = models.IntegerField()

    objects = UserManager()




ROLE_CHOICES = (
    (1, "Выключено"),
    (2, "Включено"),
)
ROLE_CHOICES1 = (
    (1, "Показаты"),
    (2, "Скрыть"),
)

ROLE_CHOICES2 = (
    (1, "Fiat"),
    (2, "Crypto"),
)

ROLE_CHOICES3 = (
    (1, "Покупка"),
    (2, "Пополниние"),
)

ROLE_CHOICES4 = (
    (1, "В ожидании"),
    (2, "Обработано"),
)


class Finance(models.Model):
    name = models.CharField(max_length=280)
    logo = models.ImageField(upload_to="Finance")
    description = models.TextField()
    alias = models.SlugField()
    # type = models.IntegerField()

    wallet_type = models.PositiveSmallIntegerField(choices=ROLE_CHOICES2, blank=True,
                                                   null=True)
    type = models.PositiveSmallIntegerField(choices=ROLE_CHOICES3, blank=True,
                                            null=True)
    currency = models.CharField(max_length=280)
    commission = models.CharField(max_length=280)
    gateway_fees = models.CharField(max_length=280)
    extra_fees = models.CharField(max_length=280)
    min = models.CharField(max_length=16)
    max = models.CharField(max_length=16)
    status = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True,
                                              null=True)
    display = models.PositiveSmallIntegerField(choices=ROLE_CHOICES1, blank=True,
                                               null=True)

    processing = models.CharField(max_length=16)

    class Meta:
        ordering = ['type']

    def image_tag(self):
        return mark_safe('<img src={} width="50" />'.format(self.logo.url))

    image_tag.short_description = 'Изображение'
    image_tag.allow_tags = True

    def image_tag_normal(self):
        return mark_safe('<img src={} width="300" />'.format(self.logo.url))

    image_tag_normal.short_description = 'Изображение'


class Finance_rates(models.Model):
    currency = models.CharField(max_length=280)
    rate = models.CharField(max_length=280)
    date_update = models.CharField(max_length=280)


class Requests(models.Model):
    guid = models.CharField(max_length=280)
    suid = models.CharField(max_length=280)
    login = models.CharField(max_length=280)
    sum = models.CharField(max_length=280)
    credit = models.CharField(max_length=280)
    method = models.CharField(max_length=280)
    currency = models.CharField(max_length=280)
    wallet_num = models.CharField(max_length=280)
    wallet_type = models.CharField(max_length=16)
    date_creation = models.CharField(max_length=280)
    date_update = models.CharField(max_length=280)
    batch = models.CharField(max_length=280)

    status = models.PositiveSmallIntegerField(choices=ROLE_CHOICES4, blank=True,
                                              null=True)


class Balance(models.Model):
    login = models.CharField(max_length=280)
    alias = models.SlugField()
    balance = models.CharField(max_length=280)
    limit_refill = models.CharField(max_length=280)
    limit_buy = models.CharField(max_length=280)
    limit_sell = models.CharField(max_length=280)
    date_update = models.CharField(max_length=280)

    def __str__(self):
        return self.balance
