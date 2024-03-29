"""delivery_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home.jinja2, name='home.jinja2')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home.jinja2')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('api/v1/', include([
        # path('', include('api.auth_v1.routes')),
        path('shop/', include('api.shop.urls')),
        # path('cart/', include('api.cart.urls')),
        path('auth/', include([
            path('', include('api.auth_v2.urls')),
            path('token/', jwt_views.TokenObtainPairView.as_view(), name ='token_obtain_pair'),
            path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name ='token_refresh'),
        ])),
    ])),
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('apps.shop.urls')),
    path('account/', include('apps.account.urls')),
    path('cart/', include('apps.cart.urls')),
)

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        re_path(r'^rosetta/', include('rosetta.urls'))
    ]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [path('__debug__/', include(debug_toolbar.urls)), ] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
