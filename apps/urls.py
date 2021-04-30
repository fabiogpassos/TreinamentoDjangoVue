from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.contrib.auth import views

from .cart.webhook import webhook

from .cart.views import cart_detail, success
from .core.views import frontpage, contact, about
from .order.views import admin_order_pdf
from .store.views import product_detail, category_detail, search
from .userprofile.views import signup, myaccount

from .newsletter.api import api_add_subscriber
from .coupon.api import api_can_use
from .store.api import api_add_to_cart, api_remove_from_cart, api_create_checkout_session, api_validate_payment

from saulgadgets.sitemaps import StaticViewSitemap, CategorySitemap, ProductSitemap


sitemaps = {'static': StaticViewSitemap, 'product': ProductSitemap, 'category': CategorySitemap}


urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('search/', search, name='search'),
    path('cart/', cart_detail, name='cart_detail'),
    path('hooks/', webhook, name='webhook'),
    path('cart/success/', success, name='success'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('admin/admin_order_pdf/<int:order_id>/', admin_order_pdf, name='admin_order_pdf'),

    # Auth
    path('myaccount/', myaccount, name='myaccount'),
    path('signup/', signup, name='signup'),
    path('login/', views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),

    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

    # API
    path('api/can_use/', api_can_use, name='api_can_use'),
    path('api/create_checkout_session/', api_create_checkout_session, name='api_create_checkout_session'),
    path('api/validate_payment/', api_validate_payment, name='api_validate_payment'),
    path('api/add_to_cart/', api_add_to_cart, name='api_add_to_cart'),
    path('api/remove_from_cart/', api_remove_from_cart, name='api_remove_from_cart'),
    path('api/add_subscriber/', api_add_subscriber, name='api_add_subscriber'),

    # Store
    path('<slug:category_slug>/<slug:slug>/', product_detail, name='product_detail'),
    path('<slug:slug>/', category_detail, name='category_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
