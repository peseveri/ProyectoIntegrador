class Country:
    def __init__(self, CountryID, CountryName, CountryCode):
        self._CountryID = CountryID
        self._CountryName = CountryName
        self._CountryCode = CountryCode

    def __str__(self):
        return f"{self._CountryName} ({self._CountryCode})"

    def is_code_valid(self):
        return len(self._CountryCode) <= 3
