from django.db import models
from django.utils import timezone
import uuid

class Account(models.Model):
    balance = models.FloatField(default=0.0, editable=False)

    def __str__(self):
        return 'account id ' + str(self.id) + ' with balance ' + str(self.balance)

class TransactionStatus(models.TextChoices):
    DRAFT = 'draft', 'Draft'
    PROCESSED = 'processed', 'Processed'

class Transaction(models.Model):
    amount = models.FloatField(default=0.0)
    payer = models.ForeignKey(Account, on_delete = models.CASCADE, related_name='transaction_payer')
    receiver = models.ForeignKey(Account, on_delete= models.CASCADE, related_name='transaction_receiver')
    note = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=TransactionStatus.choices, default=TransactionStatus.DRAFT, editable=False)

    class Meta:
        ordering = ('-updated',)
    
    def process(self):
        print('self.payer.balance < self.amount = ', self.payer.balance < self.amount)
        
        if self.payer.balance >= self.amount and self.status == TransactionStatus.DRAFT:
            self.payer.balance -= self.amount
            self.receiver.balance += self.amount

            self.payer.save()
            self.receiver.save()

            self.status = TransactionStatus.PROCESSED
            self.updated = timezone.now()
            self.save()
            return True
        return False

    def __str__(self):
        return 'transaction ' + self.status + ' created at ' + str(self.created_at) + ' amount ' + str(self.amount) + ' from ' + str(self.payer.id) + ' to ' + str(self.receiver.id) + ' note ' + self.note

'''
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save)
def create_account(sender, instance, created, **kwargs):
    if isinstance(instance, AccountHolder) and created:
        print("here")
        Account.objects.create(holder=instance)
'''