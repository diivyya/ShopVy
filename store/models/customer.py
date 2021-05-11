from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=40)
    password = models.CharField(max_length=100)


    def register(self):
        self.save()

    @staticmethod
    def get_customer_by_email(eid):
        try:
            return Customer.objects.get(email=eid)
        except:
            return False

    def userExists(self):
        if Customer.objects.filter(email=self.email):
            return True
        else:
            return False
