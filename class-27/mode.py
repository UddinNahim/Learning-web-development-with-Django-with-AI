"""
Syntax:
f = open(filename, mode)
operation on 'f' based on mode 
f.close()
"""

filename = 'file_handling.txt'
read_mode = 'r'
f = open(filename, read_mode)
content = f.read()
print(content)

f.close()