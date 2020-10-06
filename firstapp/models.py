from django.db import models

class Emp(models.Model):
    ename = models.CharField(max_length = 32)
    epass = models.CharField(max_length = 32)
    eemail = models.CharField(max_length = 32)
    eage = models.IntegerField()

    def __str__(self):
        a = self.ename+"\n"+self.epass+"\n"+self.eemail+"\n"+str(self.eage)
        return a
