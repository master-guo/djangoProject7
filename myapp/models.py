from django.db import models

# Create your models here.

class Stu(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    age = models.SmallIntegerField()
    sex = models.CharField(max_length=1)
    classid = models.CharField(max_length=8)

    def __str__(self):
        return "%d:%s:%d:%s:%s"%(self.id,self.name,self.age,self.sex,self.classid)

    class Meta:
        db_table = "stu"