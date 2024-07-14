from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import MailingMessageListView, MailingMessageDetailView, MailingMessageUpdateView, \
    MailingMessageDeleteView, MailingSettingsCreateView, MailingSettingsUpdateView, \
    MailingSettingsListView, MailingSettingsDetailView, MailingSettingsDeleteView, MailingStatusListView, \
    MailingStatusDetailView, MailingMessageCreateView, MailingMessageTemplateView

app_name = MailingConfig.name

urlpatterns = [
    path('', MailingMessageTemplateView.as_view(), name='home'),
    path('list/', MailingMessageListView.as_view(), name='list'),
    path('create/', MailingMessageCreateView.as_view(), name='create'),
    path('view/<int:pk>/', MailingMessageDetailView.as_view(), name='view'),
    path('update/<int:pk>/', MailingMessageUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', MailingMessageDeleteView.as_view(), name='delete'),
    path('settings/', MailingSettingsListView.as_view(), name='settings_list'),
    path('settings/create/', MailingSettingsCreateView.as_view(), name='settings_create'),
    path('settings/<int:pk>/', MailingSettingsDetailView.as_view(), name='settings_view'),
    path('settings/<int:pk>/update/', MailingSettingsUpdateView.as_view(), name='settings_edit'),
    path('settings/<int:pk>/delete/', MailingSettingsDeleteView.as_view(), name='settings_delete'),
    path('status_list', MailingStatusListView.as_view(), name='mailing_status_list'),
    path('status_detail/<int:pk>', MailingStatusDetailView.as_view(), name='mailing_status_detail'),
]
