from binary import binary

bin=binary("test")
print(bin.encrypt())
print(bin.decrypt(bin.encrypt()))
