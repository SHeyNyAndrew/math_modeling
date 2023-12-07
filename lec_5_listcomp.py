symbols = 'Python'
symbols_codes = [ord(symbols) for symbols in symbols]
print(symbols_codes)

symbols = 'Snake'
symbols_codes = (ord(symbols) for symbols in symbols)
print(symbols_codes)

for object in symbols_codes:
    print(object)