from datetime import date, time


class Employee:
    def __init__(self, name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details):
        self._name = name
        self._employee_id = employee_id
        self._department = department
        self._job_title = job_title
        self._basic_salary = basic_salary
        self._age = age
        self._date_of_birth = date_of_birth
        self._passport_details = passport_details

    def get_name(self):
        return self._name

        # Similar getter and setter methods for other attributes

    def calculate_salary(self):
        # Implement salary calculation logic here (e.g., with benefits, deductions)
        pass


class Manager(Employee):
    def __init__(self, name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details,
                 manages=[]):
        super().__init__(name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details)
        self._manages = manages

    def add_managed_employee(self, employee):
        self._manages.append(employee)

    def get_managed_employees(self):
        return self._manages


class Client:
    def __init__(self, client_id, name, address, contact_details, budget):
        self._client_id = client_id
        self._name = name
        self._address = address
        self._contact_details = contact_details
        self._budget = budget

        # Getter and setter methods omitted for brevity


class Guest:
    def __init__(self, guest_id, name, address, contact_details):
        self._guest_id = guest_id
        self._name = name
        self._address = address
        self._contact_details = contact_details

        # Getter and setter methods omitted for brevity


class Event:
    def __init__(self, event_id, event_type, theme, date, event_time, duration, venue_address, client, guest_list):
        self._event_id = event_id
        self._event_type = event_type
        self._theme = theme
        self._date = date
        self._event_time = event_time
        self._duration = duration
        self._venue_address = venue_address
        self._client = client
        self._guest_list = guest_list
        self._invoice = None

    def set_invoice(self, invoice):
        self._invoice = invoice

    def get_invoice(self):
        return self._invoice

    def calculate_cost(self):
        # Implement cost calculation logic here (considering supplier costs)
        pass


class Invoice:
    def __init__(self, invoice_id, event, total_cost, line_items=[]):
        self._invoice_id = invoice_id
        self._event = event
        self._total_cost = total_cost
        self._line_items = line_items
        # Getter and setter methods omitted for brevity


class Supplier:
    def __init__(self, supplier_id, name, address, contact_details):
        self._supplier_id = supplier_id
        self._name = name
        self._address = address
        self._contact_details = contact_details


class CateringCompany(Supplier):
    def __init__(self, supplier_id, name, address, contact_details, menu, minimum_guests, maximum_guests):
        super().__init__(supplier_id, name, address, contact_details)
        self._menu = menu
        self._minimum_guests = minimum_guests
        self._maximum_guests = maximum_guests

    # Test Cases


employee1 = Employee("Mariam Alameri", "EMP001", "Sales", "Sales Manager", 5000.0, 35, date(2003, 7, 3),
                     "Passport details")
employee2 = Manager("Alyazia Alameri", "EMP002", "Marketing", "Marketing Manager", 4500.0, 40, date(2005, 9, 1),
                    "Passport Details")
