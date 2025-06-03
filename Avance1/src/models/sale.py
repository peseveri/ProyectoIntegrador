class Sale:
    def __init__(self, SalesID, SalesPersonID, CustomerId, ProducID, Quantity, Discount, TotalPrice, SalesDate, TransactionNumber):
        self._SalesID = SalesID
        self._SalesPersonID = SalesPersonID
        self._CustomerId = CustomerId
        self._ProducID = ProducID
        self._Quantity = Quantity
        self._Discount = Discount
        self._TotalPrice = TotalPrice
        self._SalesDate = SalesDate
        self._TransactionNumber = TransactionNumber

    def __str__(self):
        return f"Sale({self._SalesID}): ${self._TotalPrice} on {self._SalesDate}"

    def final_price_per_unit(self):
        return float(self._TotalPrice) / float(self._Quantity) if float(self._Quantity) != 0 else 0
