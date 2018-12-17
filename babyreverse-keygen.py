import string

def xordemboys(dembytes, demstrings):
  return chr(ord(dembytes) ^ ord(demstrings))

buchstaben = string.ascii_lowercase

vergleichsarray = ['\x0a','\x0d','\x06','\x1c','\x22','\x38','\x18','\x26','\x36','\x0f','\x39','\x2b','\x1c','\x59','\x42','\x2c','\x36','\x1a','\x2c','\x26','\x1c','\x17','\x2d','\x39','\x57','\x43','\x01','\x07','\x2b','\x38','\x09','\x07','\x1a','\x01','\x17','\x13','\x13','\x17','\x2d','\x39','\x0a','\x0d','\x06','\x46','\x5c','\x7d']

for buchstabe in buchstaben:
  y = buchstabe
  ergebnis = []
  ergebnis.append(y)
  for x in vergleichsarray:
    y = (xordemboys(x, y))
    ergebnis.append(y)
  printer = ''.join(str(e) for e in ergebnis)
  print(printer)

