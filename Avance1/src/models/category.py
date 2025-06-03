class Category:
    def __init__(self, CategoryID, CategoryName):
        self._CategoryID = CategoryID
        self._CategoryName = CategoryName

    def __str__(self):
        return f"Category({self._CategoryID}: {self._CategoryName})"

    def get_id_name(self):
        return (self._CategoryID, self._CategoryName)
