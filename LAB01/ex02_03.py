# Nhập số từ người dùng
so = int(input("Nhập một số nguyên: ")) 

# Kiểm tra xem số đó có phải số chẵn hay không
if so % 2 == 0: 
    print(so, "là số chẵn.")  # Dòng này phải thụt lề vào bên trong khối if
else: 
    print(so, "không phải là số chẵn.")  # Dòng này phải thụt lề vào bên trong khối else
