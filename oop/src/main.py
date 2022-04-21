from employee import *
from reporting import *
from shift import *

# Call the classses 
# Create data:Create a list with employee and salary inside the Employee Class 
employee=[
    Manager("vera","V",2000,MorningShift()),
    Attdendant("tine","T",4000,MorningShift()),
    Attdendant("james","J",8000,AfternoonShift()),
    Cook("tim","Ti",5000,AfternoonShift()),
    Mechanic("ela","E",1500,AfternoonShift()),
    Mechanic("sayla","S",3000,MorningShift()),
    Mechanic("era","EA",2020,AfternoonShift()),
    Mechanic("cheuk","C",3400,NightShift()),
]

# dependency ingestion a tool to removing decoupling

# Polymorphism help to removed if/else blocked
reports=[
    AccountReport(employee),
    StaffingReport(employee),
    ScheduleReport(employee),
]


def main():
# # decoupling the reports  : Dependency injection 
#     account_report=AccountReport(employee)
#     account_report.print_accounting_report()  # call print_accounting_report method
#     print()
#     staffing_report=StaffingReport(employee)
#     staffing_report.print_staffing_report()

    for r in reports:
        print()
        r.print_report()  # call print_report()

if __name__ == '__main__':
    main()



