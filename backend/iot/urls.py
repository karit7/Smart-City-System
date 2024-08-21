from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import CityAPIViewset, InformationKioskAPIViewset, ParkingSpaceAPIViewset, StreetSignAPIViewset, StreetLightAPIViewset, VehicleAPIViewset, RobotAPIViewset

router = SimpleRouter()
router.register('cities', CityAPIViewset)
router.register('informationkiosks', InformationKioskAPIViewset)
router.register('parkingspaces', ParkingSpaceAPIViewset)
router.register('streetsigns', StreetSignAPIViewset)
router.register('streetlights', StreetLightAPIViewset)
router.register('vehicles', VehicleAPIViewset)
router.register('robots', RobotAPIViewset)


urlpatterns = router.urls

