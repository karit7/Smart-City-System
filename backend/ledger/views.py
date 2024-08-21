from django.contrib.auth import get_user_model

from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Account, Transaction
from .serializers import AccountSerializer, TransactionSerializer, UserSerializer
from .permissions import IsSuperUserOrReadOnly, IsSuperUser

from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class AccountAPIViewset(viewsets.ModelViewSet):
    permission_classes = (IsSuperUser,) # new
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    

class TransactionAPIViewset(viewsets.ModelViewSet):
    permission_classes = (IsSuperUserOrReadOnly,) # new
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status', 'payer', 'receiver']

    @action(detail=True)
    def process(self, request, pk=None):
        transaction = self.get_object()
        if transaction.process():
            return Response({'status': 'transaction processed'})
        else:
            return Response({'status': 'transaction NOT processed'},
                            status=status.HTTP_400_BAD_REQUEST)
    
    # a transaction can not be deleted
    def destroy(self, request, pk=None):
        response = {'message': 'Delete function is not offered in this path.'}
        return Response(response, status=status.HTTP_403_FORBIDDEN)

class UserAPIViewset(viewsets.ModelViewSet):
    permission_classes = (IsSuperUser,) # new
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer



