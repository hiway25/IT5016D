# TicketingSystem.py
# Author: Helen Thomas
# Date: 24.08.2023

# This version did not allow me to use options 3, 4, 5, as I had applied "Pass"
# I will edit in Pycharm and then import a better working version

class Ticket:
    def __init__(self, ticket_number, creator_name, staff_id, email, description):
        self.ticket_number = ticket_number
        self.creator_name = creator_name
        self.staff_id = staff_id
        self.email = email
        self.description = description
        self.response = "Not Yet Provided"
        self.status = "Open"

    def generate_password(self):
        if "Password Change" in self.description:
            new_password = self.staff_id[:2] + self.creator_name[:3]
            self.response = f"New password generated: {new_password}"
            self.status = "Closed"

    def provide_response(self, response):
        self.response = response
        self.status = "Closed"

    def reopen_ticket(self):
        self.status = "Reopened"

    def __str__(self):
        return (
            f"Ticket Number: {self.ticket_number}\n"
            f"Ticket Creator: {self.creator_name}\n"
            f"Staff ID: {self.staff_id}\n"
            f"Email Address: {self.email}\n"
            f"Description: {self.description}\n"
            f"Response: {self.response}\n"
            f"Ticket Status: {self.status}\n"
        )

    @staticmethod
    def TicketStats(tickets):
        num_created = len(tickets)
        num_resolved = sum(1 for ticket in tickets if ticket.status == "Closed")
        num_open = num_created - num_resolved
        return num_created, num_resolved, num_open


class Main:
    def __init__(self):
        self.tickets = []

    def create_ticket(self):
        creator_name = input("Enter ticket creator's name: ")
        staff_id = input("Enter staff ID: ")
        email = input("Enter contact email: ")
        description = input("Enter description of the issue: ")

        ticket_number = len(self.tickets) + 2001
        new_ticket = Ticket(ticket_number, creator_name, staff_id, email, description)
        self.tickets.append(new_ticket)
        return new_ticket

    def resolve_ticket(self, ticket):
        ticket.generate_password()

    def provide_response(self, ticket):
        response = input("Enter response: ")
        ticket.provide_response(response)

    def reopen_ticket(self, ticket):
        ticket.reopen_ticket()

    def display_tickets(self):
        for ticket in self.tickets:
            print(ticket)
            print()

    def display_statistics(self):
        num_created, num_resolved, num_open = Ticket.TicketStats(self.tickets)
        print("Displaying Ticket Statistics\n")
        print(f"Tickets Created: {num_created}\nTickets Resolved: {num_resolved}\nTickets To Solve: {num_open}\n")


if __name__ == "__main__":
    main = Main()

    while True:
        print("\nHelp Desk Ticketing System")
        print("1. Create Ticket")
        print("2. Resolve Ticket")
        print("3. Provide Response")
        print("4. Reopen Ticket")
        print("5. Display Tickets")
        print("6. Display Statistics")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            ticket = main.create_ticket()
            print(f"Ticket {ticket.ticket_number} created successfully!")

        elif choice == "2":
            # Resolve Ticket
            pass

        elif choice == "3":
            # Provide Response
            pass

        elif choice == "4":
            # Reopen Ticket
            pass

        elif choice == "5":
            main.display_tickets()

        elif choice == "6":
            main.display_statistics()

        elif choice == "0":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please choose a valid option.")
