from typing import List


class InMemoryDB:
    # Level 1 Functions
    def Set(self, key, field, value: str):
        """
        Should insert a field-value pair to the record associated with key. If the field in the record already
        exists, replace the existing value with the specified value. If record doesn't exist, create a new one.
        """
        pass

    def Get(self, key, field: str) -> str:
        """
        Should return the value contained within field of record associated with key. If record or field doesn't exist, should return null
        """
        pass

    def Delete(self, key, field: str) -> bool:
        """
        Should remove the field from the record associated with key. Returns true if the field was successfully deleted,
        and false if the key or the field do not exist in the database
        """
        pass

    # Level 2 functions
    def Scan(self, key: str) -> List[str]:
        """
        Should return a list of strings representing the fields of a record associated with the key.
        The returned list should be in the following format ["<field1>(<value1>)" , "<field2>(<value2>)", ...]
        where the fields are lexicographically sorted. If specified record doesn't exist, return empty list.
        """
        pass

    def ScanByPrefix(self, key, prefix: str) -> List[str]:
        """
        Should return a list of strings representing some fields of a records associated with the key.
        Specifically, only fields that starts with the prefix should be included.
        The returned list should be the same format as the Scan operation with the fields sorted in lexicographical order.
        """
        pass

    # Level 3 functions

    def SetAt(self, key, field, value: str, timestamp: int) -> List[str]:
        """
        Should insert a field-value pair or update the value of the field in the record associated with key
        """
        pass

    def SetAtWithTtl(self, key, field, value: str, timestamp, ttl: int) -> List[str]:
        """
        Should insert a field-value pair or update the value of the field in the record associated with key.
        Also sets its Time-to-Live starting at timestamp to be ttl. The ttl is the amount of time that this
        field-value pair should exist in the database, meaning it will be available during the interval: [timestamp, timestamp + ttl]
        """
        pass

    def DeleteAt(self, key, field: str, timestamp: int) -> bool:
        """
        The same as Delete, but with timestamp of the operation specified. Should return true if the field existed and was
        successfully deleted and false if the key didn't exist.
        """
        pass

    def GetAt(self, key, field: str, timestamp: int) -> str:
        """
        The same as Get, but with timestamp of the operation specified
        """
        pass

    def ScanAt(self, key: str, timestamp: int) -> List[str]:
        """
        The same Scan but with the timestamp of the operation specified
        """
        pass

    def ScanPrefixAt(self, key, prefix: str, timestamp: int) -> List[str]:
        """
        The same as ScanPrefix but with the timestamp of the operation specified.
        """
        pass
