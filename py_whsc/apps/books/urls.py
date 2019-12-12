from rest_framework.routers import SimpleRouter

from apps.books.views import WhBookViewSet

Book_router = SimpleRouter()
Book_router.register(r'book', WhBookViewSet)
