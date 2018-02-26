#_*_ coding:utf-8 _*_
# Author: Qiu

class Department():

    ALL = 0
    def __init__(self,name):
        dpms = []
        self.name = name
        self.dpms = dpms
    @classmethod
    def get_all(cls):
        return Department.ALL

    def get_count(self):
        return len(self.dpms)

    def get_employees(self):
        for i in self.dpms:
            info = 'id-{employee_id},name-{name},phone-{phone},salary-{salary},department-{department_name}'.format(
                employee_id=i.employee_id,name=i.name,phone=i.phone,salary=i.get_salary(),department_name=i.department_name
            )
            print info

class Employee():

    employee_id = 0

    def __init__(self,name,phone,salary,department):
        Employee.employee_id += 1
        Department.ALL += 1
        self.name = name
        self.phone = phone
        self.__salary = salary
        self.employee_id = Employee.employee_id
        self.department_name = department.name
        department.dpms.append(self)


    def get_salary(self):
        return self.__salary

    def get_info(self):
        info = {}
        info['name'] = self.name
        info['id'] = self.employee_id
        info['phone'] = self.phone
        info['salary'] = self.__salary
        info['dapartment_name'] = self.department_name
        return info

if __name__ == '__main__':
    hr = Department('hr')
    it = Department('it')

    e1 = Employee('hong','123456','5000',hr)
    e2 = Employee('tian','111111','6666',it)
    e3 = Employee('liu','222222','7777',it)
    print e1.get_info(),e1.get_salary()
    print e2.get_info(),e2.get_salary()
    print e3.get_info(),e3.get_salary()
    print hr.get_count()
    print it.get_count()
    print Department.get_all()
    hr.get_employees()
    it.get_employees()
