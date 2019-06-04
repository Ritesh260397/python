from rest_framework import serializers

from .models import File,Detail,Template

class FileSerializer(serializers.ModelSerializer):
  class Meta():
    model = File
    fields = '__all__'

class DetailSerializer(serializers.ModelSerializer):
  class Meta():
    model = Detail
    fields = '__all__'

class TemplateSerializer(serializers.ModelSerializer):
  class Meta():
    model = Template
    fields = '__all__'
# class On_OffSerializer(serializers.ModelSerializer):
#   class Meta():
#     model = active
#     fields = '__all__'
