from django.urls import path
from .views import get_token,protected_view
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('get-token/', get_token, name='get_token'),
    path('protected/',protected_view),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
