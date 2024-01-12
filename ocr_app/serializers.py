from rest_framework import serializers
from ocr_app.models import *
class FileSerializer(serializers.ModelSerializer):
    file_path = serializers.SerializerMethodField()  # Define a SerializerMethodField

    class Meta:
        model = File
        fields = ('id', 'file', 'file_path')  # Include 'file_path' in fields

    def get_file_path(self, obj):
        # Method to retrieve the file path
        return obj.file.path  # Assuming 'file' is the FileField in your model


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = userprofile
        fields = '__all__'

class StudiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = studies
        fields = '__all__'
    def to_representation(self, instance):
        self.fields['user'] =  UserSerializer(read_only=True)
        return super(StudiesSerializer, self).to_representation(instance)