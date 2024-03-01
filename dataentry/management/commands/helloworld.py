from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Prints Hello World"

    def handle(self, *args, **kwargs):
        # write the logic
        self.stdout.write('Hello World')
