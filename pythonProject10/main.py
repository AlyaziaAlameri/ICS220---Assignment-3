import tkinter as tk



class Employee:

    def __init__(self, id, name, position):

        self.id = id

        self.name = name

        self.position = position



class Event:

    def __init__(self, id, name, date):

        self.id = id

        self.name = name

        self.date = date



class Guest:

    def __init__(self, id, name, affiliation):

        self.id = id

        self.name = name

        self.affiliation = affiliation



class Supplier:

    def __init__(self, id, name, service):

        self.id = id

        self.name = name

        self.service = service



# Sample data

employees = []

events = []

guests = []

suppliers = []



# Create a tkinter window

window = tk.Tk()

window.title("Management System")



# Function to add an employee

def add_employee():

    id = emp_id_entry.get()

    name = emp_name_entry.get()

    position = emp_position_entry.get()

    employees.append(Employee(id, name, position))

    update_status("Employee added successfully.")



# Function to delete an employee

def delete_employee():

    id = emp_id_entry.get()

    for employee in employees:

        if employee.id == id:

            employees.remove(employee)

            update_status("Employee deleted successfully.")

            return

    update_status("Employee not found.")



# Function to modify an employee

def modify_employee():

    id = emp_id_entry.get()

    for employee in employees:

        if employee.id == id:

            employee.name = emp_name_entry.get()

            employee.position = emp_position_entry.get()

            update_status("Employee modified successfully.")

            return

    update_status("Employee not found.")



# Function to display employee details by ID

def display_employee():

    id = emp_id_entry.get()

    for employee in employees:

        if employee.id == id:

            update_status(f"Employee ID: {employee.id}\nName: {employee.name}\nPosition: {employee.position}")

            return

    update_status("Employee not found.")



# Function to add an event

def add_event():

    id = event_id_entry.get()

    name = event_name_entry.get()

    date = event_date_entry.get()

    events.append(Event(id, name, date))

    update_status("Event added successfully.")



# Function to delete an event

def delete_event():

    id = event_id_entry.get()

    for event in events:

        if event.id == id:

            events.remove(event)

            update_status("Event deleted successfully.")

            return

    update_status("Event not found.")



# Function to modify an event

def modify_event():

    id = event_id_entry.get()

    for event in events:

        if event.id == id:

            event.name = event_name_entry.get()

            event.date = event_date_entry.get()

            update_status("Event modified successfully.")

            return

    update_status("Event not found.")



# Function to display event details by ID

def display_event():

    id = event_id_entry.get()

    for event in events:

        if event.id == id:

            update_status(f"Event ID: {event.id}\nName: {event.name}\nDate: {event.date}")

            return

    update_status("Event not found.")



# Function to add a guest

def add_guest():

    id = guest_id_entry.get()

    name = guest_name_entry.get()

    affiliation = guest_affiliation_entry.get()

    guests.append(Guest(id, name, affiliation))

    update_status("Guest added successfully.")



# Function to delete a guest

def delete_guest():

    id = guest_id_entry.get()

    for guest in guests:

        if guest.id == id:

            guests.remove(guest)

            update_status("Guest deleted successfully.")

            return

    update_status("Guest not found.")



# Function to modify a guest

def modify_guest():

    id = guest_id_entry.get()

    for guest in guests:

        if guest.id == id:

            guest.name = guest_name_entry.get()

            guest.affiliation = guest_affiliation_entry.get()

            update_status("Guest modified successfully.")

            return

    update_status("Guest not found.")



# Function to display guest details by ID

def display_guest():

    id = guest_id_entry.get()

    for guest in guests:

        if guest.id == id:

            update_status(f"Guest ID: {guest.id}\nName: {guest.name}\nAffiliation: {guest.affiliation}")

            return

    update_status("Guest not found.")



# Function to add a supplier

def add_supplier():

    id = supplier_id_entry.get()

    name = supplier_name_entry.get()

    service = supplier_service_entry.get()

    suppliers.append(Supplier(id, name, service))

    update_status("Supplier added successfully.")



# Function to delete a supplier

def delete_supplier():

    id = supplier_id_entry.get()

    for supplier in suppliers:

        if supplier.id == id:

            suppliers.remove(supplier)

            update_status("Supplier deleted successfully.")

            return

    update_status("Supplier not found.")



# Function to modify a supplier

def modify_supplier():

    id = supplier_id_entry.get()

    for supplier in suppliers:

        if supplier.id == id:

            supplier.name = supplier_name_entry.get()

            supplier.service = supplier_service_entry.get()

            update_status("Supplier modified successfully.")

            return

    update_status("Supplier not found.")



# Function to display supplier details by ID

def display_supplier():

    id = supplier_id_entry.get()

    for supplier in suppliers:

        if supplier.id == id:

            update_status(f"Supplier ID: {supplier.id}\nName: {supplier.name}\nService: {supplier.service}")

            return

    update_status("Supplier not found.")



# Function to update status label

def update_status(message):

    status_label.config(text=message)



# Create employee input fields

emp_id_label = tk.Label(window, text="Employee ID:")

emp_id_label.grid(row=0, column=0)

emp_id_entry = tk.Entry(window)

emp_id_entry.grid(row=0, column=1)



emp_name_label = tk.Label(window, text="Name:")

emp_name_label.grid(row=1, column=0)

emp_name_entry = tk.Entry(window)

emp_name_entry.grid(row=1, column=1)



emp_position_label = tk.Label(window, text="Position:")

emp_position_label.grid(row=2, column=0)

emp_position_entry = tk.Entry(window)

emp_position_entry.grid(row=2, column=1)



# Create employee action buttons

add_emp_btn = tk.Button(window, text="Add Employee", command=add_employee)

add_emp_btn.grid(row=3, column=0)

delete_emp_btn = tk.Button(window, text="Delete Employee", command=delete_employee)

delete_emp_btn.grid(row=3, column=1)

modify_emp_btn = tk.Button(window, text="Modify Employee", command=modify_employee)

modify_emp_btn.grid(row=3, column=2)

display_emp_btn = tk.Button(window, text="Display Employee", command=display_employee)

display_emp_btn.grid(row=3, column=3)



# Create event input fields

event_id_label = tk.Label(window, text="Event ID:")

event_id_label.grid(row=4, column=0)

event_id_entry = tk.Entry(window)

event_id_entry.grid(row=4, column=1)



event_name_label = tk.Label(window, text="Name:")

event_name_label.grid(row=5, column=0)

event_name_entry = tk.Entry(window)

event_name_entry.grid(row=5, column=1)



event_date_label = tk.Label(window, text="Date:")

event_date_label.grid(row=6, column=0)

event_date_entry = tk.Entry(window)

event_date_entry.grid(row=6, column=1)



# Create event action buttons

add_event_btn = tk.Button(window, text="Add Event", command=add_event)

add_event_btn.grid(row=7, column=0)

delete_event_btn = tk.Button(window, text="Delete Event", command=delete_event)

delete_event_btn.grid(row=7, column=1)

modify_event_btn = tk.Button(window, text="Modify Event", command=modify_event)

modify_event_btn.grid(row=7, column=2)

display_event_btn = tk.Button(window, text="Display Event", command=display_event)

display_event_btn.grid(row=7, column=3)



# Create guest input fields

guest_id_label = tk.Label(window, text="Guest ID:")

guest_id_label.grid(row=8, column=0)

guest_id_entry = tk.Entry(window)

guest_id_entry.grid(row=8, column=1)



guest_name_label = tk.Label(window, text="Name:")

guest_name_label.grid(row=9, column=0)

guest_name_entry = tk.Entry(window)

guest_name_entry.grid(row=9, column=1)



guest_affiliation_label = tk.Label(window, text="Affiliation:")

guest_affiliation_label.grid(row=10, column=0)

guest_affiliation_entry = tk.Entry(window)

guest_affiliation_entry.grid(row=10, column=1)



# Create guest action buttons

add_guest_btn = tk.Button(window, text="Add Guest", command=add_guest)

add_guest_btn.grid(row=11, column=0)

delete_guest_btn = tk.Button(window, text="Delete Guest", command=delete_guest)

delete_guest_btn.grid(row=11, column=1)

modify_guest_btn = tk.Button(window, text="Modify Guest", command=modify_guest)

modify_guest_btn.grid(row=11, column=2)

display_guest_btn = tk.Button(window, text="Display Guest", command=display_guest)

display_guest_btn.grid(row=11, column=3)



# Create supplier input fields

supplier_id_label = tk.Label(window, text="Supplier ID:")

supplier_id_label.grid(row=12, column=0)

supplier_id_entry = tk.Entry(window)

supplier_id_entry.grid(row=12, column=1)



supplier_name_label = tk.Label(window, text="Name:")

supplier_name_label.grid(row=13, column=0)

supplier_name_entry = tk.Entry(window)

supplier_name_entry.grid(row=13, column=1)



supplier_service_label = tk.Label(window, text="Service:")

supplier_service_label.grid(row=14, column=0)

supplier_service_entry = tk.Entry(window)

supplier_service_entry.grid(row=14, column=1)



# Create supplier action buttons

add_supplier_btn = tk.Button(window, text="Add Supplier", command=add_supplier)

add_supplier_btn.grid(row=15, column=0)

delete_supplier_btn = tk.Button(window, text="Delete Supplier", command=delete_supplier)

delete_supplier_btn.grid(row=15, column=1)

modify_supplier_btn = tk.Button(window, text="Modify Supplier", command=modify_supplier)

modify_supplier_btn.grid(row=15, column=2)

display_supplier_btn = tk.Button(window, text="Display Supplier", command=display_supplier)

display_supplier_btn.grid(row=15, column=3)



# Status label

status_label = tk.Label(window, text="", fg="green")

status_label.grid(row=16, columnspan=4)

from tkinter import ttk

# Function to populate Treeview with details
def populate_tree(tree, data_list):
    tree.delete(*tree.get_children())  # Clear existing treeview content
    for item in data_list:
        if isinstance(item, Employee):
            tree.insert("", tk.END, values=(item.id, item.name, item.position))
        elif isinstance(item, Event):
            tree.insert("", tk.END, values=(item.id, item.name, item.date))
        elif isinstance(item, Guest):
            tree.insert("", tk.END, values=(item.id, item.name, item.affiliation))
        elif isinstance(item, Supplier):
            tree.insert("", tk.END, values=(item.id, item.name, item.service))

# Create a tkinter window
window = tk.Tk()
window.title("Management System")

# Create Treeview widget for Employees
employee_tree = ttk.Treeview(window, columns=("ID", "Name", "Position"), show="headings")
employee_tree.heading("ID", text="ID")
employee_tree.heading("Name", text="Name")
employee_tree.heading("Position", text="Position")
employee_tree.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

# Create Treeview widget for Events
event_tree = ttk.Treeview(window, columns=("ID", "Name", "Date"), show="headings")
event_tree.heading("ID", text="ID")
event_tree.heading("Name", text="Name")
event_tree.heading("Date", text="Date")
event_tree.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

# Create Treeview widget for Guests
guest_tree = ttk.Treeview(window, columns=("ID", "Name", "Affiliation"), show="headings")
guest_tree.heading("ID", text="ID")
guest_tree.heading("Name", text="Name")
guest_tree.heading("Affiliation", text="Affiliation")
guest_tree.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

# Create Treeview widget for Suppliers
supplier_tree = ttk.Treeview(window, columns=("ID", "Name", "Service"), show="headings")
supplier_tree.heading("ID", text="ID")
supplier_tree.heading("Name", text="Name")
supplier_tree.heading("Service", text="Service")
supplier_tree.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

# Function to update all Treeviews with current data
def update_treeviews():
    populate_tree(employee_tree, employees)
    populate_tree(event_tree, events)
    populate_tree(guest_tree, guests)
    populate_tree(supplier_tree, suppliers)

# Button to update Treeviews
update_btn = tk.Button(window, text="Update", command=update_treeviews)
update_btn.grid(row=2, column=0, columnspan=2, pady=10)

# Sample data initialization
employees = [Employee(1, "Alyazia Alameri", "Manager"), Employee(2, "Mahra Mubarak", "Coordinator")]
events = [Event(101, "Conference", "2024-06-17"), Event(102, "Seminar", "2024-03-20")]
guests = [Guest(1001, "Mouza Saeed", "Company A"), Guest(1002, "Hamad Alhammadi", "Company B")]
suppliers = [Supplier(2001, "Special Catering", "Catering Services"), Supplier(2002, "Party Decor", "Event Decoration")]

# Update Treeviews initially with sample data
update_treeviews()

# Run the GUI
window.mainloop()