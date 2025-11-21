from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns =[
    path('index/',views.index,name='index'),
    path('result/',views.result,name='result'),
    path('submit-form/', views.submit_form, name='submit_form'),
    path('verify-otp/', views.verify_otp, name='verify_otp'),
    path('resend',views.resend,name='resend'),
    path('delete/<int:id>',views.delete_id,name='delete'),
    path('update/<int:id>',views.update_id,name='update'),
    path('register/',views.register_page,name='register'),
    path('',views.login_page,name='login'),
    path('logout/',views.logout_page,name='logout')
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)