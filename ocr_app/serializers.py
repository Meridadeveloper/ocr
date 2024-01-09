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
