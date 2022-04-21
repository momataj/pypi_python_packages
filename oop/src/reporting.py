
# decoupling the reports  : Dependency injection 

class Report:
    def __init__(self, emp_list):
        self._emp_list=emp_list
        #self._shift=shift
    

class AccountReport(Report):
    def print_report(self):   #Polymorphism using the same function name 
        print("Accounting")
        for e in self._emp_list:
            print(f'{e.get_fullname()},${e.salary}')   # call the class function with parenthesis

class StaffingReport(Report):

    def print_report(self):
        print("Staffing")
        for e in self._emp_list:
            print(f'{e.get_fullname()},{e.job_title}')


class ScheduleReport(Report):

    def print_report(self):
        print("Schedule")
        for e in self._emp_list:
            print(f'{e.get_fullname()},{e.shift.get_shift_info()}')


