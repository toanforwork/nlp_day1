# Trợ lý Thư viện - ChatBot Rule-Based NLP

## THÀNH VIÊN

1. Trần Thị Minh Ánh - 2531302
2. Phạm Đinh Quốc Hòa - 2531307
3. Hà Quốc Toàn - 2531314
4. Nguyễn Phương Thịnh - 2531313

## MỤC TIÊU TỔNG QUÁT

- **Minh họa nguyên lý cơ bản của NLP Rule-Based** trong môi trường thực tế
- **Thể hiện quá trình phát triển chatbot** từ ý tưởng đến sản phẩm hoàn chỉnh trên nền tảng Web

- **Nghiên cứu xử lý ngôn ngữ tiếng Việt** với các đặc thù về dấu thanh và cấu trúc
- **Thử nghiệm pattern matching** với ngôn ngữ có nhiều biến thể chính tả

## MỤC TIÊU CỤ THỂ

### **1. Xử lý Ngôn ngữ Tiếng Việt**

**Mục tiêu:** Tạo chatbot hiểu và phản hồi bằng tiếng Việt tự nhiên

**Thực hiện:**

- Xử lý tiếng Việt có dấu/không dấu
- Giao diện người dùng dễ sử dụng

**Ví dụ:**

```
Input: "Thu vien mo cua luc may gio?" (không dấu)
Output: "📅 Thư viện mở cửa: Thứ Hai - Thứ Sáu: 8:00 - 22:00..."
```

### **2. Pattern Matching**

**Mục tiêu:** Xử lý một số trường hợp sai chính tả

**Thực hiện:**

- **Accent Normalization**: Xử lý `"sách" ~ "sach"`
- **Fuzzy Matching**: Chịu lỗi chính tả với similarity > 70%
- **Multi-level Scoring**: Ưu tiên khớp chính xác > 0.5
- **Keyword Expansion**: Từ khóa dựa trên Rule đã định nghĩa

### **3. Domain Knowledge Management**

**Mục tiêu:** Quản lý thông tin hoạt động của thư viện

**Cấu trúc kiến thức:**

- **Giờ hoạt động**: Thứ 2-6 (8h-22h), Cuối tuần (10h-20h)
- **Dịch vụ sách**: Tìm kiếm, mượn trả, gia hạn
- **Cơ sở vật chất**: Phòng học, máy tính, WiFi, in ấn
- **Chính sách**: Phí, tiền phạt, quy định
- **Hỗ trợ học tập**: Database, nghiên cứu, tư vấn

---

**Quick Start:**

```bash
cd library-chatbot-vietnamese
pip install -r requirements.txt
python app.py
# Truy cập: http://localhost:5001
```
