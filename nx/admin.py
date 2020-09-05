from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from django.utils.translation import gettext as _
from django.db import models
from django.utils.safestring import mark_safe
import time
from nx.forms import *
from nx.models import *
from django.contrib import admin

import datetime

epoch = datetime.datetime.utcfromtimestamp(0)


def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0

admin.site.unregister(Group)

@admin.register(Users)
class MyUserAdmin(admin.ModelAdmin):
    # form = UsersForm
    form = UserChangeForm
    # add_form = UserCreationForm
    list_display = ('id', 'first_name', 'Last_name', 'login', 'email', 'balance')
    list_display_links = list_display
    list_filter = ('status', 'is_superuser')
    search_fields = ('email', 'first_name', 'last_name', 'login')
    ordering = ('-id',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'first_name', 'last_name', 'login', 'phone',
                           'photo', 'u_group', 'u_verify', 'status')}),

    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'date_of_birth', 'password1', 'password2')}
         ),
    )
    def Last_name(self, obj):
        return obj.last_name

    def balance(self, obj):
        try:
            balance = Balance.objects.get(login=obj.login)
        except Balance.DoesNotExist:
            balance = 0
        return balance

    def date_update1(self, obj):
        try:
            float_date = float(obj.date_update)
            return time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(float_date))

        except ValueError:
            float_date = unix_time_millis(obj.date_update)
            return time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(float_date))

    def date_creation(self, obj):
        float_date = float(obj.date_creation)
        return time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(float_date))





@admin.register(Finance)
class FinanceAdmin(admin.ModelAdmin):
    list_display = ['id', 'status', 'type', 'name', 'currency']
    list_display_links = list_display
    list_filter = ['status', 'type', 'currency']
    search_fields = ['name']
    exclude = ('processing', 'type')
    form = FinanceForm

    # readonly_fields = ['image_tag_normal','id']
    # fieldsets = (
    #     (None, {'fields': ('name','logo' )}),
    #
    # )
    prepopulated_fields = {'alias': ('name',)}

    def get_changelist(self, request, **kwargs):
        """Improve changelist query speed by disabling deterministic ordering.

        Please be aware that this might disturb pagination.
        """
        from django.contrib.admin.views.main import ChangeList

        class NoDeterministicOrderChangeList(ChangeList):
            def _get_deterministic_ordering(self, ordering):
                return ordering

        return NoDeterministicOrderChangeList


@admin.register(Balance)
class BalanceAdmin(admin.ModelAdmin):
    list_display = ['id','balance']


@admin.register(Finance_rates)
class FinanceRatesAdmin(admin.ModelAdmin):
    form = FinanceRatesForm
    # fields = ('date_update',)
    exclude = ('processing', 'date_update')
    list_display = ['id', 'rate', 'date_update1', 'currency']
    list_display_links = list_display
    list_filter = ['currency']
    search_fields = ['rate']

    def date_update1(self, obj):
        float_date = float(obj.date_update)
        return time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(float_date))


@admin.register(Requests)
class RequestsAdmin(admin.ModelAdmin):
    list_display = ['id', 'Sum', 'Batch_Wallet', 'status', 'login', 'currency']
    list_display_links = list_display
    list_filter = ['currency', 'status']
    search_fields = ['login', 'batch', 'wallet_num']

    def Batch_Wallet(self, obj):
        return mark_safe('<div>'
                         '{}<br>{}'
                         '</div>'.format(obj.batch, obj.wallet_num))

    def Sum(self, obj):
        users = Users.objects.all().count()
        return mark_safe('<div  style="'
                         'height:40px;width:150px;border-radius: 5px;'
                         'text-align: center;">'
                         '{}<br>{}'
                         '</div>'.format(obj.sum, obj.credit))

    def has_add_permission(self, request, obj=None):
        return False
