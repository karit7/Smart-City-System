from django.contrib.auth import get_user_model

from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import City
from .models import InformationKiosk, ParkingSpace, Robot, StreetSign, StreetLight, Vehicle

from .serializers import StreetLightSerializer, StreetSignSerializer, CitySerializer, InformationKioskSerializer, ParkingSpaceSerializer, VehicleSerializer, RobotSerializer
from .permissions import IsSuperUserOrReadOnly, IsSuperUser

from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class CityAPIViewset(viewsets.ModelViewSet):
    permission_classes = (IsSuperUserOrReadOnly,) # new
    queryset = City.objects.all()
    serializer_class = CitySerializer

class InformationKioskAPIViewset(viewsets.ModelViewSet):
    permission_classes = (IsSuperUserOrReadOnly,) # new
    queryset = InformationKiosk.objects.all()
    serializer_class = InformationKioskSerializer

    @action(detail=True)
    def purchase_ticket(self, request, pk=None):
        print(request)
        print('pk = ', pk)
        information_kiosk = self.get_object()
        if information_kiosk.purchase_ticket(request['person'], ['event']):
            return Response({'status': 'transaction processed'})
        else:
            return Response({'status': 'transaction NOT processed'})

class ParkingSpaceAPIViewset(viewsets.ModelViewSet):
    permission_classes = (IsSuperUserOrReadOnly,) # new
    queryset = ParkingSpace.objects.all()
    serializer_class = ParkingSpaceSerializer

    @action(detail=True)
    def charge(self, request, pk=None):
        parking_space = self.get_object()
        if parking_space.charge(self, request['vehicle'], request['hours']):
            return Response({'status': 'transaction processed'})
        else:
            return Response({'status': 'transaction NOT processed'})

class RobotAPIViewset(viewsets.ModelViewSet):
    permission_classes = (IsSuperUserOrReadOnly,) # new
    queryset = Robot.objects.all()
    serializer_class = RobotSerializer

class StreetSignAPIViewset(viewsets.ModelViewSet):
    permission_classes = (IsSuperUserOrReadOnly,) # new
    queryset = StreetSign.objects.all()
    serializer_class = StreetSignSerializer

class StreetLightAPIViewset(viewsets.ModelViewSet):
    permission_classes = (IsSuperUserOrReadOnly,) # new
    queryset = StreetLight.objects.all()
    serializer_class = StreetLightSerializer

class VehicleAPIViewset(viewsets.ModelViewSet):
    permission_classes = (IsSuperUserOrReadOnly,) # new
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

    @action(detail=True)
    def charge(self, request, pk=None):
        vehicle = self.get_object()
        if vehicle.charge(self, request['person']):
            return Response({'status': 'transaction processed'})
        else:
            return Response({'status': 'transaction NOT processed'})



