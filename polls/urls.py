from django.urls import path
from .views import PublisherList,PublisherDetail
from django.contrib.auth import views as auth_views


app_name = 'polls'
urlpatterns = [
    path('', PublisherList.as_view(),name='index'),

    path('<int:pk>/',PublisherDetail.as_view(),name = 'detail'),


    path('password_reset/', auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('password_reset_complete', auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),



]





