# myapp/management/commands/load_csv.py
import csv
from django.core.management.base import BaseCommand
from api.models import Data

class Command(BaseCommand):
    help = 'Load data from CSV file into the database'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']
        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                Data.objects.create(
                    PIPELINE = row[0],
                    FOLDER = row[1],
                    SCRIPT = row[2],
                    # Map fields to your model fields
                )
        self.stdout.write(self.style.SUCCESS('Data loaded successfully'))
