try:
    #raise 
    raise Exception("rut", "2111111-0", "invalidate rut format")
except Exception as error:
    print(type(error))
    print(error.args)
    print(error)

#haciendo un destructuring de los args
key, value, message = error.args

print(f'key -->{key}')
print(f'value -->{value}')
print(f'message -->{message}')