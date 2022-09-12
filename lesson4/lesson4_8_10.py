# Given the salaries of three employees working at a department, find the
# amount of money by which the salary of the highest-paid employee differs
# from the salary of the lowest-paid employee. The input consists of three
# positive integers - the salaries of the employees. Output a single number,
# the difference between the top and the bottom salaries

high_employee = input("write the highest salary: ")

average_employee = input("write the average salary: ")

low_employee = input("write the lowest salary: ")

mode_salary = int(high_employee) - int(low_employee)

print(mode_salary)