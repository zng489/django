from django.shortcuts import render
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from .models import BlogPost
from .serializers import BlogPostSerializer
from api.serializers import ProductSerializer
from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from django.http import JsonResponse, HttpResponse
import json
import csv
from api.models import Product
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework import permissions, authentication
from rest_framework import generics
from .models import Data
from .serializers import DataSerializer


from api.authentication import TokenAuthentication


# Create your views here.
# e31560f6dff7d486db8484329af13e28ef4713a1
class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    authentication_classes = [
        authentication.SessionAuthentication,
        TokenAuthentication
        #authentication.TokenAuthentication
        ]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]

    def delete(self, request, *args, **kwargs):
        BlogPost.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BlogPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    Lookup_field = "pk"

@api_view(["POST"])
def api_home(request, *args, **kwargs):
    """
    DRF API View
    """
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        print(serializer.data)
        data = serializer.data
        return Response(data)
    #return Response(data)
    ##model_data = Product.objects.all().order_by("?").first()
    ##data = {}
    ##if model_data:
        ##data = model_to_dict(model_data, fields=['id', 'title'])
        ##data = dict(data)
        ##json_data_str = json.dumps(data)

        # data['id'] = model_data.id
        # data['title'] = model_data.title
        # data['content'] = model_data.content
        # data['price'] = model_data.price
        # model instance (model_data)
        # turn a Python dict
        # return JSON to my client
    #return JsonResponse(json_data_str, headers = {"content-type":"application/json"}) 
    ##return HttpResponse(json_data_str, headers = {"content-type":"application/json"}) 

def api_home_test(request, *args, **kwargs):
#def api_home(request):    
    body = request.body # byte string of JSON data
    data = {}
    try:
        data = json.loads(body) # string of JSON data -> Python Dict
    except:
        pass
    # print(body)
    # print(data)
    # data['headers'] = request.headers # request.META
    # return JsonResponse({"message":"Hi There, this is yout Django API response"})
    return JsonResponse(data) 

#39:09
#39:09
# 56

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk' ??

product_detail_view = ProductDetailAPIView.as_view()

'''
# Function-Based View with @api_view 
# get, post, put, delete, update with csv file

@api_view(['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
def my_view(request):
    if request.method == 'GET':
        # Handle GET request
        data = {"message": "This is a GET request"}
        return Response(data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        # Handle POST request
        received_data = request.data  # Access the incoming data
        data = {"message": "This is a POST request", "received_data": received_data}
        return Response(data, status=status.HTTP_201_CREATED)
    
    elif request.method == 'PUT':
        # Handle PUT request
        received_data = request.data  # Access the incoming data
        data = {"message": "This is a PUT request", "updated_data": received_data}
        return Response(data, status=status.HTTP_200_OK)
    
    elif request.method == 'DELETE':
        # Handle DELETE request
        data = {"message": "This is a DELETE request"}
        return Response(data, status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PATCH':
        # Handle PATCH request
        received_data = request.data  # Access the incoming data
        data = {"message": "This is a PATCH request", "patched_data": received_data}
        return Response(data, status=status.HTTP_200_OK)
'''

import csv
from io import StringIO

@api_view(['POST'])
def upload_csv_view(request):
    if request.method == 'POST':
        csv_file = request.FILES.get('file')
        if not csv_file.name.endswith('.csv'):
            return Response({"error": "File is not CSV format"}, status=status.HTTP_400_BAD_REQUEST)

        file_data = csv_file.read().decode('utf-8')
        io_string = StringIO(file_data)
        reader = csv.reader(io_string)
        # Process the CSV data
        for row in reader:
            # Do something with the data
            pass
        
        return Response({"message": "CSV file processed successfully"}, status=status.HTTP_201_CREATED)
    




@api_view(['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
def handle_csv_view(request):
    if request.method == 'GET':
        # Handle GET request: Retrieve some data (e.g., list of processed items)
        data = {"message": "This is a GET request"}
        ### csv_file = request.FILES.get(r'C:\Users\PC\Desktop\django_api_v1\mysite\api\Cep_coordenadas.csv')
        ### file_data = csv_file.read().decode('utf-8')
        ### io_string = StringIO(file_data)
        ### reader = csv.DictReader(io_string)
        ### print(reader)
        return Response(data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        # Handle POST request: Upload and process a CSV file
        csv_file = request.FILES.get(r'C:\Users\PC\Desktop\django_api_v1\mysite\api\Cep_coordenadas.csv')
        if not csv_file or not csv_file.name.endswith('.csv'):
            return Response({"error": "Please upload a valid CSV file."}, status=status.HTTP_400_BAD_REQUEST)
        
        file_data = csv_file.read().decode('utf-8')
        io_string = StringIO(file_data)
        reader = csv.DictReader(io_string)

        # Process the CSV data
        processed_data = []
        for row in reader:
            # Example processing: Collect rows into a list
            processed_data.append(row)

        # Return processed data or save to database
        return Response({"message": "CSV file processed successfully", "data": processed_data}, status=status.HTTP_201_CREATED)
    
    elif request.method == 'PUT':
        # Handle PUT request: Typically for updating records
        received_data = request.data
        # Process the received data (e.g., update existing record)
        data = {"message": "This is a PUT request", "updated_data": received_data}
        return Response(data, status=status.HTTP_200_OK)
    
    elif request.method == 'DELETE':
        # Handle DELETE request: Typically for deleting records
        # Example: Delete all records or a specific record
        data = {"message": "This is a DELETE request"}
        return Response(data, status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PATCH':
        # Handle PATCH request: Partially update a record
        received_data = request.data
        # Process the received data (e.g., update specific fields)
        data = {"message": "This is a PATCH request", "patched_data": received_data}
        return Response(data, status=status.HTTP_200_OK)



#####################################################################################
# GENERICS.LISTCREATEAPIVIEW 
#####################################################################################

class DataListCreateAPIView(generics.ListCreateAPIView):
    queryset = Data.objects.all()
    serializer_class = DataSerializer
    #authentication_classes = [authentication.SessionAuthentication]
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class DataListRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Data.objects.all()
    serializer_class = DataSerializer
    lookup_field = "pk"
    #authentication_classes = [authentication.SessionAuthentication]
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]



#####################################################################################
# API_VIEW['POST', 'GET', 'DELETE', 'PUT']
#####################################################################################

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import DataRecord
from .serializers import DataRecordSerializer

# CREATE
@api_view(['POST'])
def create_data_record(request):
    serializer = DataRecordSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# READ (List all records)
@api_view(['GET'])
def list_data_records(request):
    records = DataRecord.objects.all()
    serializer = DataRecordSerializer(records, many=True)
    return Response(serializer.data)

# READ (Retrieve a single record)
@api_view(['GET'])
def retrieve_data_record(request, pk):
    try:
        record = DataRecord.objects.get(pk=pk)
    except DataRecord.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = DataRecordSerializer(record)
    return Response(serializer.data)

# UPDATE
@api_view(['PUT'])
def update_data_record(request, pk):
    try:
        record = DataRecord.objects.get(pk=pk)
    except DataRecord.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = DataRecordSerializer(record, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# DELETE
@api_view(['DELETE'])
def delete_data_record(request, pk):
    try:
        record = DataRecord.objects.get(pk=pk)
    except DataRecord.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    record.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)



#####################################################################################
# METHOD TO OBTAIN DIRECT DATA FROM CSV FILE
#####################################################################################

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
@authentication_classes([authentication.SessionAuthentication])
# Permissions: permissions.IsAuthenticatedOrReadOnly is applied correctly, 
# meaning authenticated users can make any type of request, 
# while unauthenticated users can only read (via GET, HEAD, OPTIONS).
def obtain_direct_data_from_csv_file(request):
    data = []
    file_path = r'C:\Users\PC\Desktop\django_api_v1\mysite\api\management\commands\lnd_org_raw.csv'
    
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    
    return Response(data)




#####################################################################################
# API GETTING ANOTHER API
#####################################################################################

import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def get_api_from_api(request):
    # Example URL of the external API you want to call
    external_api_url = 'https://jsonplaceholder.typicode.com/posts'

    try:
        # Make a GET request to the external API
        response = requests.get(external_api_url)
        response.raise_for_status()  # Check if the request was successful

        # Parse the JSON response from the external API
        data = response.json()

        # Return the data from the external API as the response of your API
        return Response(data)

    except requests.exceptions.RequestException as e:
        # Handle any errors that occurred during the request
        return Response({"error": str(e)}, status=500)



#####################################################################################
# COMES FROM "DATA"
#####################################################################################

from rest_framework import mixins, generics

class ProductRetrieveUpdateDestroyView(mixins.ListModelMixin,
                                       mixins.CreateModelMixin,
                                       mixins.RetrieveModelMixin,
                                       mixins.UpdateModelMixin,
                                       mixins.DestroyModelMixin,
                                       generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'  # Assuming 'pk' is the field you're using to look up objects

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

# Create a view instance
product_r_u_d_v = ProductRetrieveUpdateDestroyView.as_view()

# Mensageiros
# API getway
# https://www.youtube.com/watch?v=c708Nf0cHrs