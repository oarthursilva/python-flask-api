class ApiDTO:
    def __init__(self, value: str) -> None:
        self.value = value

    def toJson(self):
        return {
            'hello': self.value
        }
