class QueryBuilder:
    def __init__(self):
        self._select = []
        self._from = ""
        self._joins = []
        self._where = []
        self._group_by = []
        self._order_by = []
        self._limit = None

    def select(self, *columns):
        self._select.extend(columns)
        return self

    def from_table(self, table_name):
        self._from = table_name
        return self

    def join(self, join_clause):
        self._joins.append(join_clause)
        return self

    def where(self, condition):
        self._where.append(condition)
        return self

    def group_by(self, *columns):
        self._group_by.extend(columns)
        return self

    def order_by(self, *columns):
        self._order_by.extend(columns)
        return self

    def limit(self, limit_num):
        self._limit = limit_num
        return self

    def build(self):
        query = "SELECT " + (", ".join(self._select) if self._select else "*")
        query += " FROM " + self._from
        if self._joins:
            query += " " + " ".join(self._joins)
        if self._where:
            query += " WHERE " + " AND ".join(self._where)
        if self._group_by:
            query += " GROUP BY " + ", ".join(self._group_by)
        if self._order_by:
            query += " ORDER BY " + ", ".join(self._order_by)
        if self._limit is not None:
            query += f" LIMIT {self._limit}"
        return query
