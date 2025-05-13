# Nhập X, Y từ người dùng
input_str = input("Nhập X, Y: ")

# Chuyển đổi chuỗi nhập vào thành một danh sách các số nguyên
dimensions = [int(x) for x in input_str.split(',')]

# Lấy số dòng và số cột từ danh sách dimensions
rowNum = dimensions[0]
colNum = dimensions[1]

# Tạo ma trận với kích thước rowNum x colNum, khởi tạo tất cả phần tử bằng 0
multilist = [[0 for col in range(colNum)] for row in range(rowNum)]

# Điền các giá trị vào ma trận, giá trị tại [row][col] là row * col
for row in range(rowNum):
    for col in range(colNum):
        multilist[row][col] = row * col

# In ra ma trận
print(multilist)
