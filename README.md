# Loan Default Prediction
 Dự án này sử dụng mô hình học máy XGBoost để dự đoán khả năng vỡ nợ của khách hàng dựa trên các đặc trưng tài chính và cá nhân. Mô hình này giúp các tổ chức tài chính đánh giá nguy cơ vỡ nợ của khách hàng khi xét duyệt khoản vay. 
### Mục đích
 Mô hình dự đoán này được thiết kế để giúp các tổ chức tài chính giảm thiểu rủi ro bằng cách dự đoán khả năng vỡ nợ của khách hàng dựa trên các tính năng như điểm tín dụng, thu nhập, số tháng làm việc, số lượng tín dụng hiện tại, tỷ lệ nợ trên thu nhập, và các đặc trưng cá nhân khác.
### Cấu trúc dự án
* Data/:Chứa dữ liệu để huấn luyện và kiểm tra mô hình.
* models/:Chứa mô hình đã huấn luyện và các tệp cấu trúc của mô hình.
* notebooks/:Chứa các jupyternotebook dùng để phân tích dữ liệu,huấn luyện và kiểm tra mô hình.
* src/:chứa mã nguồn triển khai chức năng dự đoán.
### Tiền xử lý dữ liệu
* Chuyển đổi các biến phân loại (như Education, EmploymentType, MaritalStatus) thành các giá trị số.
* Xử lý dữ liệu bị mất cân bằng.
### Giải thích các biến
* LoanID:ID duy nhất của khoản vay. Đây là một mã nhận dạng cho mỗi khoản vay.
* Age:Tuổi của người vay.
* Income:Thu nhập hàng năm của người vay.
* LoanAmount:Số tiền vay mà người vay yêu cầu.
* CreditScore:Điểm tín dụng của người vay, cho thấy mức độ tín nhiệm trong việc vay nợ.
* MonthsEmployed:Số tháng người vay đã làm việc tại công ty hiện tại.
* NumCreditLines:Số lượng các dòng tín dụng mà người vay đang sử dụng (bao gồm các thẻ tín dụng, vay tiêu dùng, v.v.).
* InterestRate:Lãi suất mà người vay phải trả cho khoản vay.
* LoanTerm:Thời gian vay.
* DTIRatio:Tỷ lệ nợ trên thu nhập (Debt-to-Income Ratio), chỉ số này giúp đánh giá khả năng trả nợ của người vay.
* Education:Trình độ học vấn của người vay.
* EmploymentType:Loại hình công việc của người vay.
* MaritalStatus:Tình trạng hôn nhân của người vay.
* HasMortgage:Người vay có khoản vay thế chấp hay không.
* HasDependents:Người vay có phụ thuộc hay không.
* LoanPurpose:Mục đích của khoản vay.
* HasCoSigner:Khoản vay có người đồng ký hay không.
* Biến mục tiêu. Nếu giá trị là 1, người vay đã vỡ nợ (default); nếu là 0, người vay không vỡ nợ.
### Đánh giá mô hình
Mô hình dự đoán khả năng vỡ nợ (loan default) của mô hình đã đạt được độ chính xác Accuracy = 86.21%. Tuy nhiên, khi xem xét các chỉ số như Precision = 32.60%, Recall = 18.14%, và F1-Score = 23.31%,mô hình nhận thấy mô hình có một số vấn đề trong việc phát hiện đúng các khách hàng có nguy cơ vỡ nợ.
### Dự đoán 
Chương trình cho nhập các thông số vào (như age,income,loanamount,v.v.) và dự đoán khả năng vỡ nợ của khách hàng và từ đó đưa ra quyết định có nên cho khách hàng này vay không.