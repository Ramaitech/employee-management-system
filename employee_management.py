# ---------------------------------------------------------
# Employee Management System (Python OOP)
# ---------------------------------------------------------

class Employee:
    """
    Represents an employee in the organization.
    Attributes:
        employee_id : int
        name        : str
        department  : str
        salary      : float (monthly salary)
        designation : str
    """

    def __init__(self, employee_id, name, department, salary, designation):
        self.employee_id = employee_id
        self.name = name
        self.department = department
        self.salary = salary          # monthly salary
        self.designation = designation

    def display_info(self):
        """Display all details of the employee."""
        print("--------------------------------------------------")
        print(f"Employee ID : {self.employee_id}")
        print(f"Name        : {self.name}")
        print(f"Department  : {self.department}")
        print(f"Designation : {self.designation}")
        print(f"Monthly Pay : ${self.salary:.2f}")
        print("--------------------------------------------------")

    def update_salary(self, new_salary):
        """
        Update the employee's monthly salary.
        """
        print(f"[Update] Changing salary for {self.name} "
              f"from ${self.salary:.2f} to ${new_salary:.2f}")
        self.salary = new_salary

    def calculate_annual_salary(self):
        """
        Calculate and return the annual salary.
        """
        annual = self.salary * 12
        print(f"[Annual Salary] {self.name}'s annual salary is: ${annual:.2f}")
        return annual


# ---------------------------------------------------------
# Helper function to show all employees
# ---------------------------------------------------------
def show_all_employees(employees):
    """
    Display information for all employees in the list.
    """
    print("\n=== EMPLOYEE LIST ===")
    for emp in employees:
        emp.display_info()


# ---------------------------------------------------------
# Main Execution Block
# ---------------------------------------------------------
def main():
    # Create at least 5 employee objects
    emp1 = Employee(101, "Alice Johnson", "Engineering", 5000, "Software Engineer")
    emp2 = Employee(102, "Bob Smith", "Engineering", 6500, "Senior Developer")
    emp3 = Employee(103, "Carol Davis", "HR", 4000, "HR Specialist")
    emp4 = Employee(104, "David Wilson", "Finance", 5500, "Accountant")
    emp5 = Employee(105, "Eve Brown", "Marketing", 4500, "Marketing Executive")

    # Store them in a list
    employees = [emp1, emp2, emp3, emp4, emp5]

    # 1. Display all employees
    show_all_employees(employees)

    # 2. Update salary for one employee (example)
    print("\n=== SALARY UPDATE EXAMPLE ===")
    emp1.update_salary(5200)  # Alice gets a raise
    emp1.display_info()

    # 3. Calculate annual salary for a few employees
    print("\n=== ANNUAL SALARY CALCULATIONS ===")
    emp1.calculate_annual_salary()
    emp2.calculate_annual_salary()
    emp3.calculate_annual_salary()

    print("\n=== END OF EMPLOYEE MANAGEMENT DEMO ===")


if __name__ == "__main__":
    main()
