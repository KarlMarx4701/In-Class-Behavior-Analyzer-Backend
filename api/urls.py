from django.urls import path

from .views import *
from .auth_views import *

urlpatterns = [
    path('', index),

    # Authentication
    path('login', login),
    path('register', register),
    path('logout', logout),
    path('reset_password/<str:reset_code>', reset_password),
    path('request_password_reset/<str:username>', request_password_reset),
    path('user/group', user_group),

    # Demographic Requests
    path('demographic/create', demographic_create),
    path('demographic/update', demographic_update),
    path('demographic/delete', demographic_delete),
    path('demographic/select', demographic_select),

    # Position Requests
    path('position/create', position_create),
    path('position/select/all', position_select_all),
    path('position/select', position_select_id),
    path('position/summary', position_summary)

    # Classes Requests
]
