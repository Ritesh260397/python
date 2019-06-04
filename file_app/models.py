from django.db import models
from django_mysql.models import JSONField
from jsonfield import JSONField
from django.core.files.storage import FileSystemStorage
import os
class OverwriteStorage(FileSystemStorage):
  def get_available_name(self, name, max_length=None):
    if self.exists(name):
      # self.delete('media2/')
      os.remove(os.path.join('media2/'+name))
    return name
fs = OverwriteStorage(location='media2')


class  File(models.Model):
  file = models.FileField(blank=False, null=False,storage=fs)


class Detail(models.Model):
  SHEET_NAME = models.CharField(max_length=20)
  ROW_NO = models.IntegerField()
  COMPANY_NAME = models.CharField(max_length=20)
  STATUS = models.CharField(max_length=20)

class Template(models.Model):
    column_header=JSONField()
    Template_Name =models.CharField(max_length=80)
    Company_Name =models.CharField(max_length=100)
    Status=models.CharField(max_length=20)
    on_off=models.BooleanField(default=True)
    SHEET_NAME = models.CharField(max_length=20)
# class active(models.Model):
