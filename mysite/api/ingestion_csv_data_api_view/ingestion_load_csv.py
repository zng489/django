import csv
from api.models import DataRecord

file_path = r'C:\Users\PC\Desktop\django_api_v1\mysite\api\ingestion_csv_data_api_view\lnd_org_raw.csv'

with open(file_path, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        DataRecord.objects.create(
            PIPELINE = row['NAME_PIPELINE'],
            FOLDER = row['FOLDER'],
            SCRIPT = row['BOT_SCRIPT_NAME'],
            # Map other fields
        )
# (great_expectations) C:\Users\PC\Desktop\django_api_v1\mysite>python manage.py load_csv C:\Users\PC\Desktop\django_api_v1\mysite\api\management\commands\lnd_org_raw.csv