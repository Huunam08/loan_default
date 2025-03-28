import numpy as np
from joblib import load

# đường dẫn đến models
model = load('models/xgboost_model.pkl')

# danh sách các cột cần nhập
features = ['Age', 'Income', 'LoanAmount', 'CreditScore', 'MonthsEmployed',
       'NumCreditLines', 'InterestRate', 'LoanTerm', 'DTIRatio', 'Education',
       'EmploymentType', 'MaritalStatus', 'HasMortgage', 'HasDependents',
       'LoanPurpose', 'HasCoSigner']
print("Mô hình cần nhập các chỉ số sau:")
for i, name in enumerate(features):
    print(f"{i + 1}. {name}")
# yêu cầu nhập đúng theo thứ tự
input_values = []
print("Nhập các giá trị đầu vào:")
for name in features:
    while True:
        try:
            value = float(input(f"{name}: "))
            input_values.append(value)
            break
        except ValueError:
            print("Giá trị không hợp lệ. Vui lòng nhập lại.")
#chuyển đổi thành các mảng numpy
input_data = np.array([input_values])
# kiểm tra số lượng cột khớp với mô hình
if input_data.shape[1] != len(features):
    raise ValueError(f"Số lượng cột không khớp với mô hình. Mô hình yêu cầu {len(features)} cột.")
# dự đoán
prediction = model.predict(input_data)
print("Dự đoán: ", prediction[0])
# In kết quả dự đoán
if prediction[0] == 1:
    print("Dự đoán: Default (1) - Khách hàng có khả năng vỡ nợ.")
else:
    print("Dự đoán: No default (0) - Khách hàng không có khả năng vỡ nợ.")