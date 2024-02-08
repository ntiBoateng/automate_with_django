from typing import Any
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Sends a greeting message to everyone"

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help="Specifies user's name")


    def handle(self, *args: Any, **kwargs: Any) -> str | None:
        name = kwargs['name']
        greeting = f'Hello {name}, good morning to you'
        self.stdout.write(greeting)