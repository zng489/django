from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from .views import DataListCreateAPIView

urlpatterns = [
    path('blogposts/', views.BlogPostListCreate.as_view(), name='blogpost-view-create'),
    path('blogposts/<int:pk>/', views.BlogPostRetrieveUpdateDestroy.as_view(), name='update'),
    path('api_home/', views.api_home),
    path('api_home/<int:pk>/', views.product_detail_view),
    path('csv-handler/', views.handle_csv_view, name='handle_csv_view'),
 
    path('dlca_view/', DataListCreateAPIView.as_view(), name='data-list-create'),
    path('dlrud_view/<int:pk>/', views.DataListRetrieveUpdateDestroy.as_view(), name='update'),

    path('obtain_csv_from_file/', views.obtain_direct_data_from_csv_file, name='csv_data'),

    path('DataRecord/', views.list_data_records, name='list_data_records'),          # List all records
    path('DataRecord/create/', views.create_data_record, name='create_data_record'), # Create a new record
    path('DataRecord/<int:pk>/', views.retrieve_data_record, name='retrieve_data_record'), # Retrieve a single record
    path('DataRecord/<int:pk>/update/', views.update_data_record, name='update_data_record'), # Update a record
    path('DataRecord/<int:pk>/delete/', views.delete_data_record, name='delete_data_record'), # Delete a record
    path('get_api_from_api/', views.get_api_from_api, name='delete_data_record'),

    path('product_r_u_d_v/', views.product_r_u_d_v, name='product-list-create'),
    path('product_r_u_d_v/<int:pk>/', views.product_r_u_d_v, name='product-detail'),

    path('auth/', obtain_auth_token),    
]


