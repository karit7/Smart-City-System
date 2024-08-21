from django.test import TestCase
from .models import Account, Transaction

# Create your tests here.
class AccountModelTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        Account.objects.create(balance=1000.0)
        Account.objects.create(balance=0.0)

    def check_initial_balance(self):
        account1 = Account.objects.get(id=1)
        account2 = Account.objects.get(id=2)
        self.assertEquals(account1.balance, 1000.0)
        self.assertEquals(account2.balance, 0.0)

    

