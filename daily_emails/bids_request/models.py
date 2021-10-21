from django.db import models

# Create your models here.
class Supplier(models.Model):
    trade=models.CharField(max_length=50)
    name=models.CharField(max_length=255)
    email=models.EmailField(max_length=254)
    active=models.BooleanField(default=True)
def __str__(self):
    return self.trade

class Missing(models.Model):
    job_code=models.CharField(max_length=10)
    complete=models.BooleanField(default=False)
    concrete=models.ForeignKey(Supplier,on_delete=models.CASCADE,null=True)
    framing=models.ForeignKey(Supplier,on_delete=models.CASCADE,null=True)
    waterproofing=models.ForeignKey(Supplier,on_delete=models.CASCADE,null=True)
    roofing_siding=models.ForeignKey(Supplier,on_delete=models.CASCADE,null=True)
    insulation_gutters=models.ForeignKey(Supplier,on_delete=models.CASCADE,null=True)
    electrical=models.ForeignKey(Supplier,on_delete=models.CASCADE,null=True)
    hvac=models.ForeignKey(Supplier,on_delete=models.CASCADE,null=True)
    plumbing_fixt=models.ForeignKey(Supplier,on_delete=models.CASCADE,null=True)
    electrical_fixt=models.ForeignKey(Supplier,on_delete=models.CASCADE,null=True)
    low_voltage=models.ForeignKey(Supplier,on_delete=models.CASCADE,null=True)
    drywall=models.ForeignKey(Supplier,on_delete=models.CASCADE,null=True)
    specialties=models.ForeignKey(Supplier,on_delete=models.CASCADE,null=True)
    tile=models.ForeignKey(Supplier,on_delete=models.CASCADE,null=True)
    flooring=models.ForeignKey(Supplier,on_delete=models.CASCADE,null=True)

def __str__(self):
    return self.job_code