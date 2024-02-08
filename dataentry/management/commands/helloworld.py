from django.core.management.base import BaseCommand



class Command(BaseCommand):
    help = "Prints hello world" 

    def handle(self, *args, **kwargs):
        # we wrtie the logic here
        self.stdout.write("Hello world")