with open("data.txt", "r") as file:
    for line in file:
        # Tách giá trị chiều cao và cân nặng từ mỗi dòng và chuyển đổi thành số thực
        weight, height = map(float, line.strip().split()) #0
        
        # Xác định điều kiện hợp lệ
        if (weight <= 0 or height <= 0): #1
            print("Đầu vào không hợp lệ!") #2
        else:
            # Tính chỉ số BMI
            BMI = round(weight / (height ** 2), 1) #3

            # Đưa ra đánh giá về BMI
            if BMI < 18.5: #4
                print("Nhẹ cân") #5
            elif 18.5 <= BMI < 23: #6
                print("Bình thường") #7
            elif 23 <= BMI < 30: #8
                print("Thừa cân") #9
            else:
                print("Béo phì") #10