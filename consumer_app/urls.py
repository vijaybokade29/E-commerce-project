from django.urls import path
from consumer_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name = 'index'),
    path('about/',views.about,name = 'about'),
    path('products/',views.products,name = 'products'),
    path('product_detail/<prod_id>',views.product_detail,name = 'product_detail'),
    path('contact/',views.contact,name = 'contact'),
    path('faq/',views.faq,name = 'faq'),
    path('signin/',views.signin,name = 'signin'),
    path('signout/',views.signout,name = 'signout'),
    path('signup/',views.signup,name = 'signup'),
    path('profile/',views.profile,name = 'profile'),
    path('otp_page/',views.otp_page,name = 'otp_page'),
    path('s_otp_page/',views.s_otp_page,name = 's_otp_page'),
    # path('otp/', views.otp_page, name='otp_page'),
    path('resend_otp/', views.resend_otp, name='resend_otp'),
    path('s_resend_otp/', views.s_resend_otp, name='s_resend_otp'),
    path('reset_password/', views.reset_password, name='reset_password'),
    path('new_password/', views.new_password, name='new_password'),
    path('cart_table/', views.cart_table, name='cart_table'),
    path('update_quauntity/<prod_id>', views.update_quauntity, name='update_quauntity'),
    path('cart/<prod_id>', views.cart, name='cart'),
    path('del_cart_row/<prod_id>', views.del_cart_row, name='del_cart_row'),
    path('success/',views.success, name='success'),
    path('track/',views.track, name='track'),
    path('cart_table/paymenthandler/', views.paymenthandler, name='paymenthandler'),



]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)