from django.db import models

# Create your models here.
class Phase(models.Model):
    phase=models.IntegerField()

    def __str__(self) -> str:
        return f'{self.phase}'
    
class Movies(models.Model):
    mname=models.CharField( max_length=50)
    year=models.CharField(max_length=50)
    link=models.CharField(max_length=100)
    image=models.ImageField(upload_to='img_files')
    phase=models.ForeignKey("Phase", on_delete=models.CASCADE,null=True)
    fav=models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.mname} {self.year} {self.link} {self.image} {self.phase}'
