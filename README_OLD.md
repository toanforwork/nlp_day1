# Trợ lý Thư viện Tiếng Việt - Hệ thống NLP Dựa trên Quy tắc

## 📚 Tổng quan Dự án

Đây là chatbot dựa trên quy tắc được thiết kế cho trợ lý thư viện đại học bằng tiếng Việt. Nó minh họa các nguyên tắc cơ bản của xử lý ngôn ngữ tự nhiên dựa trên quy tắc với giao diện web.

## 🎯 Tính năng

- **14 Quy tắc Toàn diện** bao gồm các dịch vụ thư viện
- **Giao diện Web** với trò chuyện thời gian thực
- **Công cụ Khớp Mẫu** với khả năng chịu lỗi chính tả cơ bản
- **Nút Hành động Nhanh** cho các truy vấn thông dụng
- **Thiết kế Responsive** cho di động và máy tính để bàn
- **Hỗ trợ Tiếng Việt** với xử lý dấu tiếng Việt

## 🛠️ Công nghệ Sử dụng

- **Backend**: Python Flask
- **Frontend**: HTML, CSS, JavaScript
- **Phương pháp NLP**: Khớp từ khóa dựa trên quy tắc
- **Kiến trúc**: Thiết kế modular với công cụ quy tắc riêng biệt

## 📋 Danh mục Quy tắc

1. **Giờ Thư viện** - Giờ mở/đóng cửa
2. **Tìm kiếm Sách** - Tìm và định vị sách
3. **Phòng Học** - Đặt chỗ và tình trạng sẵn có
4. **Truy cập Máy tính** - WiFi, in ấn, máy tính
5. **Phí & Tiền phạt** - Phí trễ hạn và thông tin thanh toán
6. **Vị trí** - Hướng dẫn đường đi và chỗ đậu xe
7. **Thông tin Liên hệ** - Điện thoại, email, trợ giúp nhân viên
8. **Quản lý Tài khoản** - Thẻ thư viện và đăng nhập
9. **Gia hạn** - Gia hạn sách và ngày đáo hạn
10. **Chính sách Tiếng ồn** - Khu vực yên tĩnh vs hợp tác
11. **Hỗ trợ Nghiên cứu** - Cơ sở dữ liệu và tài nguyên học thuật
12. **Chính sách Thức ăn** - Nơi được phép ăn/uống
13. **Đồ Thất lạc** - Chính sách đồ bị mất
14. **Sao chép/Quét** - Thiết bị và chi phí

## 🚀 Cài đặt & Thiết lập

### Yêu cầu Tiên quyết

- Python 3.7+
- pip (trình quản lý gói Python)

### Các bước Cài đặt

1. **Điều hướng đến thư mục dự án**:

   ```powershell
   cd "d:\Documents\Master\NLP\DAY1\library-chatbot-vietnamese"
   ```

2. **Cài đặt phụ thuộc**:

   ```powershell
   pip install -r requirements.txt
   ```

3. **Chạy ứng dụng**:

   ```powershell
   python app.py
   ```

4. **Truy cập chatbot**:
   - Mở trình duyệt
   - Đi tới: `http://localhost:5001`

## 💡 Ví dụ Sử dụng

### Truy vấn Thành công:

- "Thư viện mở cửa lúc mấy giờ?" → Lịch thư viện
- "Làm thế nào để tìm sách?" → Hướng dẫn tìm kiếm
- "Tôi có thể đặt phòng học không?" → Thông tin đặt chỗ
- "Thư viện ở đâu?" → Địa chỉ và hướng dẫn
- "Phí trễ hạn là bao nhiêu?" → Thông tin tiền phạt

### Kiểm tra Hạn chế:

- "Lịch hoạt động của thư viện?" (test từ đồng nghĩa)
- "Tôi có thể ăn ở đâu?" (chính sách thức ăn)
- "Thu vien mo cua luc may gio?" (test lỗi chính tả/không dấu)
- "Kể cho tôi nghe về vật lý lượng tử" (ngoài phạm vi)

## 🔧 Kiến trúc Hệ thống

```
library-chatbot-vietnamese/
├── app.py                 # Flask web server
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html        # Chat interface
├── static/
│   ├── style.css         # Styling
│   └── script.js         # Frontend logic
└── chatbot/
    ├── __init__.py       # Package init
    ├── engine.py         # Pattern matching logic
    └── rules.py          # Rule definitions
```

## 🤖 Chi tiết Công cụ Chatbot

### Cấu trúc Quy tắc:

```python
{
    "id": 1,
    "keywords": ["giờ", "mở", "đóng", "thời gian"],
    "response": "📅 Thư viện mở cửa: Thứ Hai - Thứ Sáu: 8:00 - 22:00..."
}
```

### Quy trình Khớp:

1. **Tiền xử lý Đầu vào**: Chữ thường, loại bỏ dấu câu
2. **Loại bỏ Dấu**: Hỗ trợ text có/không có dấu tiếng Việt
3. **Phát hiện Từ khóa**: Kiểm tra khớp chính xác
4. **Hệ thống Tính điểm**: Quy tắc có nhiều khớp hơn điểm cao hơn
5. **Tương tự Cơ bản**: Tương tự dựa trên ký tự cho lỗi chính tả
6. **Chọn Phản hồi**: Trả về phản hồi quy tắc điểm cao nhất

## ⚠️ Hạn chế Đã biết

### Hạn chế Ngay lập tức:

1. **Từ vựng Hạn chế**: Chỉ phản hồi các từ khóa được định nghĩa trước
2. **Không Xử lý Từ đồng nghĩa**: "lịch" ≠ "giờ" nếu không có quy tắc rõ ràng
3. **Khả năng Chịu lỗi Chính tả Kém**: Khớp tương tự đơn giản, dễ bị hỏng
4. **Không có Bộ nhớ Ngữ cảnh**: Mỗi truy vấn độc lập
5. **Phản hồi Cứng nhắc**: Không thể thích ứng với tình huống người dùng cụ thể

### Hạn chế Nghiêm trọng:

1. **Không có Khả năng Học hỏi**: Không thể cải thiện từ tương tác người dùng
2. **Cứng nhắc Miền**: Không thể xử lý câu hỏi ngoài miền thư viện
3. **Không Hiểu Ý định**: Dựa hoàn toàn vào sự xuất hiện từ khóa
4. **Luồng Cuộc trò chuyện Hạn chế**: Không thể duy trì đối thoại nhiều lượt
5. **Không Cá nhân hóa**: Cùng phản hồi cho tất cả người dùng

## 🇻🇳 Tính năng Đặc biệt Tiếng Việt

### Xử lý Dấu:

- Hỗ trợ text có dấu: "giờ", "mở", "đóng"
- Hỗ trợ text không dấu: "gio", "mo", "dong"
- Khớp linh hoạt: "sách" = "sach"

### Bản địa hóa:

- Giao diện hoàn toàn tiếng Việt
- Phản hồi tự nhiên tiếng Việt
- Từ khóa và cụm từ Việt Nam

## 🔍 Kiểm tra Hạn chế

Thử các truy vấn này để thấy hạn chế:

- **Từ đồng nghĩa**: "lịch" vs "giờ", "tìm" vs "tra cứu"
- **Lỗi chính tả**: "thu vien", "sach co san"
- **Ngữ cảnh**: "Còn cuối tuần thì sao?" (sau khi hỏi về giờ)
- **Ngoài miền**: "Thời tiết thế nào?", "Làm thế nào nấu phở?"
- **Truy vấn phức tạp**: "Tôi cần chỗ yên tĩnh để học cho kỳ thi hóa học"

## 🌐 API Endpoints

- `GET /` - Giao diện chat chính
- `POST /chat` - Gửi tin nhắn và nhận phản hồi
- `GET /help` - Lấy thông tin trợ giúp
- `GET /rules` - Xem tất cả quy tắc (endpoint debug)

## 🎓 Giá trị Giáo dục

Dự án này minh họa:

- **Nguyên tắc cơ bản NLP dựa trên quy tắc**
- **Kỹ thuật khớp mẫu**
- **Tích hợp ứng dụng web**
- **Thiết kế kiến trúc chatbot**
- **Phân tích và hiểu hạn chế**
- **Xử lý ngôn ngữ tiếng Việt**

## 🔄 Cải tiến Tiềm năng

Để khắc phục hạn chế:

1. **Thêm từ điển từ đồng nghĩa** để mở rộng từ khóa
2. **Triển khai khớp chuỗi mờ** để xử lý lỗi chính tả tốt hơn
3. **Thêm quản lý ngữ cảnh** cho cuộc trò chuyện nhiều lượt
4. **Sử dụng phân loại ý định** thay vì khớp từ khóa
5. **Triển khai máy học** để tạo phản hồi
6. **Thêm bộ nhớ cuộc trò chuyện** để cá nhân hóa
7. **Tích hợp xử lý ngôn ngữ tiếng Việt nâng cao**

## 👨‍💻 Phát triển

### Thêm Quy tắc Mới:

1. Chỉnh sửa `chatbot/rules.py`
2. Thêm quy tắc mới vào danh sách `CHATBOT_RULES`
3. Khởi động lại ứng dụng

### Sửa đổi Logic Phản hồi:

1. Chỉnh sửa `chatbot/engine.py`
2. Sửa đổi phương thức `find_matching_rule()`
3. Kiểm tra với nhiều đầu vào khác nhau

## 📊 Điểm Thảo luận

### Hạn chế Ngay lập tức:

- **Phụ thuộc Từ khóa**: Thất bại khi người dùng không sử dụng từ mong đợi
- **Không Hiểu Ngữ cảnh**: Không thể xử lý câu hỏi theo dõi
- **Miền Hạn chế**: Hoàn toàn hỏng với câu hỏi ngoài phạm vi

### Hạn chế Nghiêm trọng:

- **Không Học hỏi**: Không thể cải thiện mà không cập nhật quy tắc thủ công
- **Vấn đề Khả năng mở rộng**: Thêm quy tắc trở nên phức tạp theo cấp số nhân
- **Chi phí Bảo trì**: Mỗi tình huống mới yêu cầu lập trình thủ công

### Tác động Thực tế:

- **Frustration Người dùng**: Xử lý kém các biến thể ngôn ngữ tự nhiên
- **Tiện ích Hạn chế**: Không thể xử lý truy vấn phức tạp, nhiều phần
- **Không linh hoạt**: Không thể thích ứng với chính sách thư viện mới mà không thay đổi mã

## 📈 Chỉ số Thành công

Chatbot thành công minh họa:

- ✅ 14+ danh mục quy tắc toàn diện
- ✅ Giao diện người dùng dựa trên web
- ✅ Tạo phản hồi thời gian thực
- ✅ Khớp mẫu cơ bản
- ✅ Tài liệu hạn chế rõ ràng
- ✅ Hỗ trợ đầy đủ tiếng Việt với xử lý dấu

---

**Được tạo cho**: Khóa học NLP - Ngày 1  
**Mục đích**: Demo giáo dục chatbot dựa trên quy tắc bằng tiếng Việt  
**Giấy phép**: MIT
