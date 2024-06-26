from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import MailingMessageListView, MailingMessageDetailView, \
    MailingMessageUpdateView, MailingMessageDeleteView, MailingSettingsCreateView, MailingSettingsUpdateView, \
    MailingSettingsListView, MailingSettingsDetailView, MailingSettingsDeleteView, MailingStatusListView, \
    MailingStatusDeleteView, MailingMessageCreateView

app_name = MailingConfig.name

urlpatterns = [
    path('', MailingMessageListView.as_view(), name='list'),
    path('create/', MailingMessageCreateView.as_view(), name='create'),
    path('view/<int:pk>/', MailingMessageDetailView.as_view(), name='view'),
    path('update/<int:pk>/', MailingMessageUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', MailingMessageDeleteView.as_view(), name='delete'),
    path('settings/', MailingSettingsListView.as_view(), name='settings_list'),
    path('settings/create/', MailingSettingsCreateView.as_view(), name='settings_create'),
    path('settings/<int:pk>/', MailingSettingsDetailView.as_view(), name='settings_view'),
    path('settings/<int:pk>/update/', MailingSettingsUpdateView.as_view(), name='settings_edit'),
    path('settings/<int:pk>/delete/', MailingSettingsDeleteView.as_view(), name='settings_delete'),
    path('status/', MailingStatusListView.as_view(), name='status_list'),
    path('status/<int:pk>/delete/', MailingStatusDeleteView.as_view(), name='status_delete'),
]
