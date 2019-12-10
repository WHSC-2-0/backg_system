from rest_framework.routers import SimpleRouter

from apps.admins.views import WhAdminViewSet

Admin_router = SimpleRouter()
Admin_router.register(r'auth', WhAdminViewSet)
