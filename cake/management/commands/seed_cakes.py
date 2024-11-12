from django.core.management.base import BaseCommand
from cake.factories import CakeFactory

class Command(BaseCommand):
    # Help text that provides a description of what the command does.
    help = 'Seed the database with Cakes'

    # The handle method is called when the custom command is executed.
    def handle(self, *args, **kwargs):
        # Create a batch of 5 Cake instances using the CakeFactory.
        CakeFactory.create_batch(5)

        # Output a success message to the console once the Cakes are seeded.
        self.stdout.write(self.style.SUCCESS('Successfully seeded Cakes'))