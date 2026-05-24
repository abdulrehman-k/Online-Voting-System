import json
import os

DATA_FILE = "voting_data.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        data = {
            "users": {},
            "votes": {},
            "candidates": ["Alice", "Bob", "Charlie"]
        }
        save_data(data)
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


# You can edit voting system on your choice
class VotingSystem:
    def __init__(self):
        self.data = load_data()
        self.current_user = None

    # Main menu can be edited for sure
    def main_menu(self):
        while True:
            print("\n===== ONLINE VOTING SYSTEM =====")
            print("1. Register")
            print("2. Login")
            print("3. Admin Panel")
            print("4. Exit")

            choice = input("Enter choice: ")

            if choice == "1":
                self.register()
            elif choice == "2":
                self.login()
            elif choice == "3":
                self.admin_panel()
            elif choice == "4":
                print("Exiting system...")
                break
            else:
                print("Invalid choice!")

    # Registration
    def register(self):
        print("\n--- REGISTER ---")
        username = input("Enter username: ")
        password = input("Enter password: ")

        if username in self.data["users"]:
            print("User already exists!")
            return

        self.data["users"][username] = password
        save_data(self.data)
        print("Registration successful!")

    # Login INFO
    def login(self):
        print("\n--- LOGIN ---")
        username = input("Username: ")
        password = input("Password: ")

        if username in self.data["users"] and self.data["users"][username] == password:
            self.current_user = username
            print(f"\nWelcome {username}!")
            self.vote_menu()
        else:
            print("Invalid credentials!")

    # Voting menu can be edited if u want like 4-5 votes
    def vote_menu(self):
        if self.current_user in self.data["votes"]:
            print("You have already voted!")
            return

        print("\n--- VOTING PANEL ---")
        print("Candidates:")

        for i, c in enumerate(self.data["candidates"], start=1):
            print(f"{i}. {c}")

        try:
            choice = int(input("Select candidate number: "))
            if 1 <= choice <= len(self.data["candidates"]):
                selected = self.data["candidates"][choice - 1]

                self.data["votes"][self.current_user] = selected
                save_data(self.data)

                print("Vote submitted successfully!")
            else:
                print("Invalid choice!")
        except ValueError:
            print("Please enter a number!")

    # Admin Panel is the one after a successfull registration of a voter
    def admin_panel(self):
        print("\n--- ADMIN LOGIN ---")
        user = input("Admin username: ")
        pwd = input("Admin password: ")

        if user == "admin" and pwd == "1234":
            self.show_results()
        else:
            print("Wrong admin credentials!")

    # Voters Results
    def show_results(self):
        print("\n===== VOTING RESULTS =====")

        results = {c: 0 for c in self.data["candidates"]}

        for vote in self.data["votes"].values():
            if vote in results:
                results[vote] += 1

        for candidate, count in results.items():
            print(f"{candidate}: {count} votes")
# Running Application....
if __name__ == "__main__":
    system = VotingSystem()
    system.main_menu()