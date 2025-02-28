company_employees = {
    "Engineering": {
        "Alice": {"age": 30, "role": "Software Engineer"},
        "Bob": {"age": 28, "role": "DevOps Engineer"}
    },
    "HR": {
        "Charlie": {"age": 35, "role": "HR Manager"}
    }
}
#print company employees
print("Company Employees: ", company_employees)

#add new employee
company_employees["Engineering"]["David"] = {"age": 27, "role": "Data Scientist"}
print("Company Employees after adding David: ", company_employees)

#print total number of employees
total_employees = sum(len(dept) for dept in company_employees.values())
print("Total Employees:", total_employees)
