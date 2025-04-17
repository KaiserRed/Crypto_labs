import _pystribog
import binascii

fio = "Галкин Алексей Дмитриевич".encode("utf-8")
hasher = _pystribog.StribogHash(_pystribog.Hash256)
hasher.update(fio)
digest = hasher.digest()

print("Полный хэш:", binascii.hexlify(digest).decode())
variant_number = digest[-1]
print("Номер варианта (от 0 до 255):", variant_number)