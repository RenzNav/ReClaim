from decimal import Decimal
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.db import transaction
from core.models import Listing


class Command(BaseCommand):
    help = "Populate ReClaim with demo accounts and listings"

    @transaction.atomic
    def handle(self, *args, **options):

        # Fictional users for the prototype demonstration
        names = [
            ("Sarah", "Murphy"),
            ("James", "Kelly"),
            ("Emma", "Byrne"),
            ("Daniel", "Ryan"),
            ("Rachel", "Walsh"),
            ("Jack", "Doyle"),
            ("Aoife", "Brennan"),
            ("Conor", "Smith"),
            ("Sophie", "Nolan"),
            ("Sean", "Clarke"),
            ("Emily", "Wilson"),
            ("Adam", "Moore"),
            ("Ciara", "Quinn"),
            ("Luke", "Martin"),
            ("Niamh", "Dunne"),
            ("Ryan", "Reilly"),
            ("Katie", "Murray"),
            ("David", "Lynch"),
            ("Laura", "Taylor"),
            ("Patrick", "Kennedy"),
        ]

        users = []
        users_created = 0
        listings_created = 0

        # Create demo accounts without duplicating existing users
        for first_name, last_name in names:
            username = f"demo_{first_name.lower()}_{last_name.lower()}"

            user, created = User.objects.get_or_create(
                username=username,
                defaults={
                    "first_name": first_name,
                    "last_name": last_name,
                    "email": f"{username}@example.com",
                }
            )

            # Store the password securely using Django's password hashing
            if created:
                user.set_password("ReclaimDemo2026!")
                user.save()
                users_created += 1

            users.append(user)

        # Listing title, quantity, estimated value and description
        listings = [
            ("Plastic Water Bottles", 15, "2.25",
             "Empty water bottles collected over the past week."),

            ("Mixed Cans and Bottles", 30, "4.50",
             "A bag of mixed recyclable drinks containers."),

            ("Soft Drink Cans", 12, "1.80",
             "Empty Coke and Fanta cans, ready for collection."),

            ("Large Plastic Bottles", 20, "5.00",
             "Empty two-litre drinks bottles."),

            ("Weekend Recycling", 45, "6.75",
             "Containers left over from a weekend gathering."),

            ("Energy Drink Cans", 18, "2.70",
             "Empty energy drink cans collected throughout the week."),

            ("Small Water Bottles", 10, "1.50",
             "Empty 500ml water bottles."),

            ("Household Recycling", 60, "9.00",
             "Several bags of empty drinks containers."),

            ("Sparkling Water Bottles", 16, "2.40",
             "Clean and empty sparkling water bottles."),

            ("Aluminium Cans", 35, "5.25",
             "Mixed aluminium drinks cans."),

            ("Office Recycling", 80, "12.00",
             "Empty drinks containers collected from our office."),

            ("Large Water Bottles", 12, "3.00",
             "Empty two-litre water bottles."),

            ("Mixed Plastic Bottles", 25, "3.75",
             "A mixture of small plastic drinks bottles."),

            ("Student House Recycling", 50, "7.50",
             "Empty cans and bottles from a shared student house."),

            ("Orange Juice Bottles", 14, "2.10",
             "Eligible plastic juice bottles ready for collection."),

            ("Party Leftovers", 100, "15.00",
             "Several bags of empty drinks cans from a party."),

            ("Sports Drink Bottles", 22, "3.30",
             "Empty sports and energy drink bottles."),

            ("Weekly Can Collection", 28, "4.20",
             "A week's worth of empty soft drink cans."),

            ("Family Recycling Bag", 40, "6.00",
             "Mixed small drinks containers from our household."),

            ("Small Can Collection", 8, "1.20",
             "A small bag of empty aluminium cans."),

            ("Two-Litre Soft Drink Bottles", 18, "4.50",
             "Empty large soft drink bottles."),

            ("Cafe Recycling", 120, "18.00",
             "Empty eligible drinks containers collected from a cafe."),

            ("Gym Water Bottles", 32, "4.80",
             "Empty water bottles collected after training."),

            ("Monthly Recycling Collection", 75, "11.25",
             "A month's worth of recyclable drinks containers."),

            ("Bag of Mixed Containers", 24, "3.60",
             "Mixed small cans and bottles available for collection."),
        ]

        # Distribute listings across 15 of the demo accounts
        for index, (title, quantity, value, description) in enumerate(listings):
            listing, created = Listing.objects.get_or_create(
                donor=users[index % 15],
                title=title,
                defaults={
                    "quantity": quantity,
                    "estimated_value": Decimal(value),
                    "description": description,
                    "is_available": True,
                }
            )

            if created:
                listings_created += 1

        # Display the results in the terminal
        self.stdout.write(self.style.SUCCESS(
            f"Created {users_created} demo accounts "
            f"and {listings_created} demo listings."
        ))