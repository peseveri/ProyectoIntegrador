class Customer:
    def __init__(self, CustomerID, FirstName, MiddleInital, LastName, CityID, Address):
        self._CustomerID = CustomerID
        self._FirstName = FirstName
        self._MiddleInital = MiddleInital
        self._LastName = LastName
        self._CityID = CityID
        self._Address = Address

    def __str__(self):
        return f"Customer({self._CustomerID}: {self._FirstName} {self._MiddleInital}. {self._LastName})"

    def full_name(self):
        return f"{self._FirstName} {self._MiddleInital}. {self._LastName}"
