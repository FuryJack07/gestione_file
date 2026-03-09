import hashlib as h

print(h.md5(b'Dato originale').digest())

print(h.md5('Dato originale'.encode('utf-8')).digest())

print(h.md5(b'Dato originale').hexdigest())

print(h.md5(b'Dato orignale').hexdigest())

print(h.sha256(b'Dato originale').hexdigest())