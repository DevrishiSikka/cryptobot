from django.urls import path
from .views import CreateAlertView, ListAlertView, DeleteAlertView

urlpatterns = [
    path('create/', CreateAlertView.as_view(), name='create_alert'),
    path('delete/', DeleteAlertView.as_view(), name='delete_alert'),
    path('', ListAlertView.as_view(), name='list_alerts')
]
