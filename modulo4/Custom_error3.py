class CustomHttpsException():
    def __init__(self _code500, _message="internal Server Error"):
        self.code = _code
        self.message = _message

try:
    raise CustomHttpsException
except Exception as error:
    print(error.code)
    print(error.message)

try:
    raise  CustomHttpsException(400, "bad Resquest")¨[]

      