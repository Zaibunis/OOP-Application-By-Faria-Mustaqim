import re

class Contact:
    """Base class for a contact."""
    def __init__(self, name: str, phone: str):
        if not self._validate_phone(phone):
            raise ValueError("Invalid phone number format.")
        self._name = name
        self._phone = phone

    def get_name(self) -> str:
        return self._name

    def display(self) -> None:
        print(f"📇 Name: {self._name}, 📞 Phone: {self._phone}")

    def update_phone(self, new_phone: str) -> None:
        if not self._validate_phone(new_phone):
            raise ValueError("Invalid phone number format.")
        self._phone = new_phone

    @staticmethod
    def _validate_phone(phone: str) -> bool:
        return bool(re.match(r"^\+?\d{7,15}$", phone))

class FriendContact(Contact):
    """Class for a friend contact."""
    def __init__(self, name: str, phone: str, birthday: str):
        super().__init__(name, phone)
        self.birthday = birthday

    def display(self) -> None:
        super().display()
        print(f"🎂 Birthday: {self.birthday}")

class BusinessContact(Contact):
    """Class for a business contact."""
    def __init__(self, name: str, phone: str, company: str, job_title: str):
        super().__init__(name, phone)
        self.company = company
        self.job_title = job_title

    def display(self) -> None:
        super().display()
        print(f"🏢 Company: {self.company}, 💼 Title: {self.job_title}")

class ContactManager:
    """Manager class to handle contacts."""
    def __init__(self):
        self._contacts = []

    def add_contact(self, contact: Contact) -> None:
        self._contacts.append(contact)

    def list_contacts(self) -> None:
        if not self._contacts:
            print("📭 No contacts available.")
        for contact in self._contacts:
            contact.display()
            print("--------")

    def find_contact(self, name: str) -> Contact | None:
        for contact in self._contacts:
            if contact.get_name().lower() == name.lower():
                return contact
        return None

    def remove_contact(self, name: str) -> bool:
        contact = self.find_contact(name)
        if contact:
            self._contacts.remove(contact)
            return True
        return False

def get_input(prompt: str, required: bool = True) -> str:
    """Helper function to get user input with validation."""
    while True:
        value = input(prompt).strip()
        if value or not required:
            return value
        print("⚠️ Input cannot be empty. Please try again.")

def main() -> None:
    """Main function to run the contact manager."""
    manager = ContactManager()
    while True:
        print("\n📒 Contact Manager Menu With OOP by Faria Mustaqim")
        print("1️⃣  Add friend contact 🧑")
        print("2️⃣  Add business contact 🧑‍💼")
        print("3️⃣  Search contact 🔍")
        print("4️⃣  Delete contact ❌")
        print("5️⃣  List all contacts 📋")
        print("6️⃣  Exit 🚪")
        choice = get_input("Enter option number: ")

        if choice == "1":
            name = get_input("👤 Name: ")
            phone = get_input("📞 Phone: ")
            birthday = get_input("🎂 Birthday: ")
            try:
                manager.add_contact(FriendContact(name, phone, birthday))
                print("✅ Friend contact added.")
            except ValueError as e:
                print(f"❌ Error: {e}")
        elif choice == "2":
            name = get_input("👤 Name: ")
            phone = get_input("📞 Phone: ")
            company = get_input("🏢 Company: ")
            title = get_input("💼 Job Title: ")
            try:
                manager.add_contact(BusinessContact(name, phone, company, title))
                print("✅ Business contact added.")
            except ValueError as e:
                print(f"❌ Error: {e}")
        elif choice == "3":
            name = get_input("🔍 Search Name: ")
            contact = manager.find_contact(name)
            if contact:
                print("🔎 Contact found:")
                contact.display()
            else:
                print("❗ Contact not found.")
        elif choice == "4":
            name = get_input("Name to delete: ")
            if manager.remove_contact(name):
                print("🧹 Contact deleted.")
            else:
                print("❗ Contact not found.")
        elif choice == "5":
            print("📋 All contacts:")
            manager.list_contacts()
        elif choice == "6":
            confirm = get_input("Are you sure you want to exit? (yes/no): ", required=False).lower()
            if confirm in ("yes", "y"):
                print("👋 Goodbye!")
                break
        else:
            print("⚠️ Invalid option. Please try again.")

if __name__ == "__main__":
    main()
