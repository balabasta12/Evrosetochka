from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about', about, name='about'),
    path('login', LoginAccount.as_view(), name='login'),
    path('register', RegisterAccount.as_view(), name='register'),
    path('add_supp', add_supplier, name='add_supplier'),
    path('user/register/confirm', ConfirmAccount.as_view(), name='user-register-confirm'),
    path('user/details', AccountDetails.as_view(), name='user-details'),
    path('user/contact', ContactView.as_view(), name='user-contact'),
    path('categories', CategoryView.as_view(), name='categories'),
    path('shops', ShopView.as_view(), name='shops'),
    path('products', ProductInfoView.as_view(), name='shops'),
    path('basket', BasketView.as_view(), name='basket'),
    path('partner/update', PartnerUpdate.as_view(), name='partner-update'),
    path('partner/state', PartnerState.as_view(), name='partner-state'),
    path('partner/orders', PartnerOrders.as_view(), name='partner-orders'),
    path('order', OrderView.as_view(), name='order'),
]
