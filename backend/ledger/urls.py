from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import AccountAPIViewset, TransactionAPIViewset, UserAPIViewset

router = SimpleRouter()
router.register('users', UserAPIViewset)
router.register('accounts', AccountAPIViewset)
router.register('transactions', TransactionAPIViewset)


urlpatterns = router.urls
