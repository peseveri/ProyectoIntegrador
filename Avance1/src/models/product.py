class Product:
    def __init__(self, ProductID, ProductName, Price, CategoryID, Class, ModifyDate, Resistant, IsAllergic, VitalityDays):
        self._ProductID = ProductID
        self._ProductName = ProductName
        self._Price = Price
        self._CategoryID = CategoryID
        self._Class = Class
        self._ModifyDate = ModifyDate
        self._Resistant = Resistant
        self._IsAllergic = IsAllergic
        self._VitalityDays = VitalityDays

    def __str__(self):
        return f"{self._ProductName} - ${self._Price:.2f}"

    def is_expensive(self, threshold=100):
        return self._Price > threshold
