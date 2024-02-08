import csv
from typing import Any
from django.core.management.base import BaseCommand, CommandParser, CommandError
from django.apps import apps

from dataentry.models import Student


class Command(BaseCommand):
    help = "This commands imports a csv file"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('file_path', type=str, help='Path to the csv file.')
        parser.add_argument('model_name', type=str, help="Choose a name for the model")

    def handle(self, *args: Any, **options: Any) -> str | None:
        # logic to import csv
        file_path = options['file_path']
        model_name = options['model_name'].capitalize()

        model = None
        # search for the models all installed apps
        for app_config in apps.get_app_configs():
            # find the model
            try:
                model = apps.get_model(app_config.label, model_name)
                break
            except LookupError:
                continue # when model not found, continue searching in other apps
        if not model:
            raise CommandError(f'Model "{model_name}" was not found in any app!')
        # print(file_path)
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                model.objects.create(**row) # can also use **row
            self.stdout.write(self.style.SUCCESS("Data imported successfully"))
        
     