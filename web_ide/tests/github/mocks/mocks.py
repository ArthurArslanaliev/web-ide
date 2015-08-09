class MockResponse:
    def __init__(self, resp):
        self.__response = resp

    def json(self):
        return self.__response
