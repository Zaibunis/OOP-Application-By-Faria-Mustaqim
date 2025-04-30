# Contact Manager with OOP in Python

A CLI-based **Contact Manager** built using **Object-Oriented Programming (OOP)** concepts in **Python** by **Faria Mustaqim**.  
This application allows you to manage **Friend** and **Business** contacts efficiently from the command line.

---

## Features

- ➕ Add **Friend** contacts with Name, Phone, and Birthday 🎂  
- ➕ Add **Business** contacts with Name, Phone, Company, and Job Title 💼  
- 📋 List all saved contacts in a structured format  
- 🔍 Search for a contact by name  
- ❌ Delete contacts you no longer need  
- ✅ Validates phone number format (7–15 digits, optional `+`)  

---

## OOP Concepts Used

- ✅ **Classes and Inheritance** (`Contact`, `FriendContact`, `BusinessContact`)
- 🔁 **Method Overriding** (custom `display()` in child classes)
- 🧪 **Encapsulation** with private attributes
- ⚠️ **Input Validation** using Regex
- 📌 **Static Methods** for utility logic
- 🧠 **Polymorphism** for displaying different contact types

---

## File Structure

contact_manager.py  # Main application code with OOP structure

---

## How to Run

1. Install **Python 3** if not already installed.
2. Save the code as `contact_manager.py`.
3. Run the application in the terminal:

```bash
python contact_manager.py

📒 Contact Manager Menu With OOP by Faria Mustaqim
1️⃣  Add friend contact 🧑
2️⃣  Add business contact 🧑‍💼
3️⃣  Search contact 🔍
4️⃣  Delete contact ❌
5️⃣  List all contacts 📋
6️⃣  Exit 🚪

```

Phone Format Rule

Phone numbers must:

Be 7 to 15 digits

Optionally start with a +

✅ Valid:

+923001234567

03001234567

❌ Invalid:

123abc

001

Author:
Faria Mustaqim🙌
🌐 GIAIC Student | 💻 Full Stack & Python Developer








