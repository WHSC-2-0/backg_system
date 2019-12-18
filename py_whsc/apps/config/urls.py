from rest_framework.routers import SimpleRouter

from apps.config.views import WhBannerViewSet

Banner_router = SimpleRouter()
Banner_router.register(r'banner', WhBannerViewSet)

