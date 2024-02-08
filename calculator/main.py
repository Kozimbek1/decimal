# import os
# from calculator import add, minus, div, mul
# a = float(input("Birinchi sonni kiriting: "))
# b = float(input("Ikkinchi sonni kiriting: "))
# print(add.summa(a, b))
# print(minus.minus(a, b))
# print(div.div(a, b))
# print(mul.mul(a, b))
#
#
# import re
# def validate_ip(ip):
#     ip_pattern = re.compile(r'^(\d{1,3}\.){3}\d{1,3}$')
#     if ip_pattern.match(ip):
#         print(f"{ip} - bu IP-adres to'g'ri.")
#     else:
#         print(f"{ip} - bu IP-adres noto'g'ri.")
# def validate_password(password):
#     password_pattern = re.compile(r'^(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&+=!]).{8,}$')
#     if password_pattern.match(password):
#         print("To'g'ri parol.")
#     else:
#         print("Noto'g'ri parol.")
# ip_address = "192.168.1.1"
# password = "rbherntgmetnwtn"
#
# validate_ip(ip_address)
# validate_password(password)


import os
def get_file_type(file_path):
    file_extension = os.path.splitext(file_path)[1]
    file_types = {
        '.txt': 'Tekst fayl',
        '.jpg': 'JPEG rasm',
        '.png': 'PNG rasm',
        '.pdf': 'PDF-dokument',
    }
    return file_types.get(file_extension, 'Noaniq tip')

file_path = "example.txt"
file_type = get_file_type(file_path)
print(f"Fayl tipi '{file_path}': {file_type}")






