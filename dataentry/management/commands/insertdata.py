from django.core.management.base import BaseCommand

from dataentry.models import Student

class Command(BaseCommand):
    help = "This command accelerate importing data to the database"

    def handle(self, *args, **kwargs):
        # drop logics here
        dataset = [
            {
                'roll_number': "2008Uyt34", 'name':"Yaw Manu Uranue", 'age': 32
            },
            {
                'roll_number': "98ouy8734", 'name':"Akosuah Uranue", 'age': 43
            }
         ]
        for data in dataset:
            existing_record = Student.objects.filter(roll_number = data['roll_number']).exists()
            if not existing_record:
                Student.objects.create(roll_number = data['roll_number'], name = data['name'], age = data['age'])
                self.stdout.write(self.style.SUCCESS("Data imported successfully"))
            else:
                self.stderr.write(f'Student with roll_number {data["roll_number"]} already exist!')
            
            
        # to add one data
        # Student.objects.create(roll_number="1000Yu78", name="Anues Rojar", age=45)

        