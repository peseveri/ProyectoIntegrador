class City:
    def __init__(self, CityID, CityName, Zipcode, CountryID):
        self._CityID = CityID
        self._CityName = CityName
        self._Zipcode = Zipcode
        self._CountryID = CountryID

    def __str__(self):
        return f"{self._CityName} ({self._Zipcode})"

    def belongs_to_country(self, country_id):
        return self._CountryID == country_id
