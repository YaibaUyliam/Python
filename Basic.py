import numpy as np

## Khởi tạo và in ra số chiều của ma trận 
#   arr = np.array([1, 1], [2, 2])
#   arr = np.ones((3,2))
#   print(arr.shape)

## Chỉnh sửa số chiều của ma trận
#   np.reshape(a, b, c)

## In array có điều kiện
#   arr = np.arange(9)      # Tạo mảng có thứ tự từ 0->8 
#   condi = arr%2==0        # Tạo mảng boolean chỉ có các phần tử True False
#   print(arr[condi])       # In ra mảng chứa các phần tử của arr nhưng nếu vị trí tương ứng True thì giữ nguyên giá trị còn lại = 0 

## Nhân vô hướng (inner product), nhân vecto với ma trận (vector-matrix multiplication), matrix-matrix multiplication   
#   arr = arr1.dot(arr2) 
#   arr = np.dot(arr1, arr2)

## Chuyển vị (Transpose)
#   arr.T

## Các hàm random 
#   arr = np.random.random()
#   arr = np.random.randint(low, hight, size=(3,2)) # Tạo ra ma trận chứa các số nguyên có kích cỡ 3x2

## Tính tổng trong array và max, min 
#   sum1 = arr.sum()    # Tổng các phần tử trong array  
#   sum1 = arr.sum(axis=0) # sum1 là mảng 1 chiều chứa các phần tử là tổng của hàng dọc tương ứng
#   sum1 = arr.sum(axis=1) # sum2 là mảng 1 chiều chứa các phần tử là tổng của hàng ngang tương ứng
#   arr.max(axis=0) # Lấy max theo cột, tương tự như trên 

## Broadcasting(Cho phép 2 mảng ko cùng số chiều thích hợp có thể cộng hoặc nhân cho nhau)
#   Ví dụ cộng 2 ma trận 4x3 và 1x3 thì nó tạo 1 ma trận 4x3 để cộng với ma trận đầu

## Một vài kĩ năng xử lí dữ liệu
#   X = np.genfromtxt('Nhập tên file', delimiter=',', dtype='float', 
#                           usecols=[nhập các dòng muốn lấy trong dữ liệu], skip_header=1)
