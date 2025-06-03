class Employee:
    def __init__(self, EmployeeID, FirstName, MiddleInital, LastName, BirthDate, Gender, CityID, HireDate):
        self._EmployeeID = EmployeeID
        self._FirstName = FirstName
        self._MiddleInital = MiddleInital
        self._LastName = LastName
        self._BirthDate = BirthDate
        self._Gender = Gender
        self._CityID = CityID
        self._HireDate = HireDate

    def __str__(self):
        return f"Employee({self._EmployeeID}: {self._FirstName} {self._LastName})"

    def years_worked(self, current_year):
        return current_year - self._HireDate.year
