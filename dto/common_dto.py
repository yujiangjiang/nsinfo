

class RestResult:
    code = 0,
    message = '',
    data = '',

    def getCode(self):
        return self.code

    @staticmethod
    def success(data):
        self = RestResult()
        self.data = data
        self.code = 200
        self.message = 'success'
        return self
