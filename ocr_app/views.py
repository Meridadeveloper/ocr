# from django.shortcuts import render
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import File
# from .serializers import FileSerializer
# from google.cloud import translate_v3beta1 as translate


# #for credentials
# from django.conf import settings


# class TranslatePDFAPIView(APIView):
#     def get(self, request):
#         # Handle GET request logic here
#         # For example, you might want to return some information or instructions about using this API
#         return Response("This is the TranslatePDFAPIView. Use POST method to translate PDFs.", status=status.HTTP_200_OK)

#     def post(self, request):
#         if request.method == 'POST' and 'file' in request.FILES:
#             file_pdf = request.FILES['file']
#             serializer = FileSerializer(data={'file': file_pdf})
            
#             if serializer.is_valid():
#                 serializer.save()
#                 print(serializer.instance)
#                 print('file_instance')
#                 file_instance = serializer.instance
#                 # file_path = file_instance.file.path
#                 print(file_instance)


#                 def translate_document(
#                     project_id: str,
#                      file_path:str,
#                      ) ->translate.TranslationServiceClient: 

                 
#                     print("translate_document function started")

#                     print("try block executing")
#                     client = translate.TranslationServiceClient.from_service_account_json(
#                     settings.GOOGLE_APPLICATION_CREDENTIALS)
        
#                     location = "us-central1"
#                     parent = f"projects/{project_id}/locations/{location}"
                    
#                     with open(file_path, "rb") as document:
#                         document_content = document.read()
                    
#                     document_input_config = {
#                         "content": document_content,
#                         "mime_type": "application/pdf",
#                     }
#                     print("documented data ")
#                     response = client.translate_document(
#                         request={
#                             "parent": parent,
#                             "target_language_code": "te",
#                             "document_input_config": document_input_config,
#                         }
#                     )
#                     translated_filename = 'media/output.pdf'
#                     f = open(translated_filename, 'wb')
#                     f.write(response.document_translation.byte_stream_outputs[0])
#                     f.close()
                
                    
#                     print("translated_file name",f)
#                     return Response(f"{translated_filename}")
                   
    
#                 file_path = file_instance.file.path
#                 return translate_document("translateapi-409417",file_path)
            


from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import File
from .serializers import FileSerializer
from google.cloud import translate_v3beta1 as translate
from django.http import FileResponse
from django.conf import settings
import io
import base64
import google.generativeai as genai
from google.generativeai import configure, GenerativeModel


class TranslatePDFAPIView(APIView):
    def get(self, request):
        # Handle GET request logic here
        # For example, you might want to return some information or instructions about using this API
        return Response("This is the TranslatePDFAPIView. Use POST method to translate PDFs.", status=status.HTTP_200_OK)

    def post(self, request):
        if request.method == 'POST' and 'file' in request.FILES:
            file_pdf = request.FILES['file']
            serializer = FileSerializer(data={'file': file_pdf})
            
            if serializer.is_valid():
                serializer.save()
                file_instance = serializer.instance
                file_path = file_instance.file.path

                client = translate.TranslationServiceClient.from_service_account_json(
                    settings.GOOGLE_APPLICATION_CREDENTIALS)
                location = "us-central1"
                parent = f"projects/translateapi-409417/locations/{location}"
                    
                with open(file_path, "rb") as document:
                    document_content = document.read()
                    
                document_input_config = {
                    "content": document_content,
                    "mime_type": "application/pdf",
                }
                response = client.translate_document(
                    request={
                        "parent": parent,
                        "target_language_code": "de",
                        "document_input_config": document_input_config,
                    }
                )

                translated_filename = 'media/output.pdf'
                f = open(translated_filename, 'wb')
                f.write(response.document_translation.byte_stream_outputs[0])
                f.close()

                translated_pdf_content = response.document_translation.byte_stream_outputs[0]

                # Corrected base64 encoding
                translated_pdf_base64 = base64.b64encode(translated_pdf_content).decode('utf-8')
                return Response(translated_pdf_base64)
        return Response("Invalid request", status=status.HTTP_400_BAD_REQUEST)


from rest_framework.decorators import api_view

# def generate_content(request):

#     api_key = 'AIzaSyBlrcjFCOerZSDkC7YvaHoJ4elXDjaYWg8'
#     genai.configure(api_key=api_key)
#     model = genai.GenerativeModel('gemini-pro')
#     question = request.GET.get('question','')
#     s= "1 line definition of "+ question
#     response =model.generate_content(s)
#     generated_text = response.text

#     return JsonResponse({'generated_text':generated_text})

# @api_view(['GET','POST'])
# def generate_content(request):
#     api_key = 'AIzaSyBlrcjFCOerZSDkC7YvaHoJ4elXDjaYWg8'
#     configure(api_key=api_key)
#     model = GenerativeModel('gemini-pro')
#     question = request.data.get('question','')
#     print(len(question))

#     s = "3 half lines answer for the " + question
#     print(s)
#     try:
#         print("try block executed")
#         response = model.generate_content(s)
#         generated_text = response.text
#         print(generated_text)
#         if generated_text == 'undefined':
#             return Response({'message':"Please enter the correct word"})
#         else:
#             print(generated_text)

#             return Response({'generated_text': generated_text})
#     except Exception as e:
#         print("except block",e)

#         return Response({'error': str(e)}, status=500)


class GenerateContentView(APIView):
    def post(self, request):
        api_key = 'AIzaSyBlrcjFCOerZSDkC7YvaHoJ4elXDjaYWg8'
        configure(api_key=api_key)
        model = GenerativeModel('gemini-pro')
        question = request.data.get('question', '')
        print(len(question))

        s = "1 line definition of " + question
        print(s)
        try:
            print("try block executed")
            response = model.generate_content(s)
            generated_text = response.text
            print(generated_text)

            return Response({'generated_text': generated_text})
        except Exception as e:
            print("except block", e)
            return Response({'error': str(e)}, status=500)
