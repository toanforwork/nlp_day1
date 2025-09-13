# Quy tắc chatbot dựa trên luật cho Trợ lý Thư viện (Vietnamese)
# Mỗi quy tắc chứa từ khóa và phản hồi tương ứng

CHATBOT_RULES = [
    {
        "id": 1,
        "keywords": ["giờ", "mở", "đóng", "thời gian", "lịch", "hoạt động", "mở cửa", "đóng cửa"],
        "response": "📅 Thư viện mở cửa: Thứ Hai - Thứ Sáu: 8:00 - 22:00, Thứ Bảy - Chủ Nhật: 10:00 - 20:00. Đóng cửa vào các ngày lễ lớn."
    },
    {
        "id": 2,
        "keywords": ["sách", "tìm", "tìm kiếm", "tra cứu", "catalog", "có sẵn", "kho", "danh mục"],
        "response": "📚 Bạn có thể tìm sách qua hệ thống trực tuyến tại library.university.edu hoặc nhờ thủ thư tại quầy tham khảo hỗ trợ."
    },
    {
        "id": 3,
        "keywords": ["phòng", "học", "đặt", "đặt chỗ", "nhóm", "phòng học", "reservation", "booking"],
        "response": "🏠 Phòng học có thể đặt trực tuyến qua hệ thống đặt chỗ. Phòng cá nhân: tối đa 2 giờ, phòng nhóm: tối đa 4 giờ."
    },
    {
        "id": 4,
        "keywords": ["máy tính", "laptop", "wifi", "mạng", "in", "máy in", "internet"],
        "response": "💻 Chúng tôi có hơn 50 máy tính, WiFi miễn phí (mạng: UnivLibrary), và dịch vụ in ấn: 2,000đ/trang trắng đen, 5,000đ/trang màu."
    },
    {
        "id": 5,
        "keywords": ["phí", "phạt", "trễ", "quá hạn", "tiền phạt", "nộp phạt"],
        "response": "💰 Phí trễ hạn: 10,000đ/ngày cho sách thường, 50,000đ/ngày cho tài liệu dự trữ. Có thể thanh toán trực tuyến hoặc tại quầy."
    },
    {
        "id": 6,
        "keywords": ["địa chỉ", "vị trí", "ở đâu", "đường", "chỗ đậu xe", "parking", "tìm đường"],
        "response": "📍 Chúng tôi ở 123 Đường Campus, Tòa nhà Chính, Tầng 2. Có chỗ đậu xe tại Bãi A & B. Có thang máy và cầu thang."
    },
    {
        "id": 7,
        "keywords": ["liên hệ", "điện thoại", "email", "giúp", "thủ thư", "hỗ trợ"],
        "response": "📞 Liên hệ: Điện thoại (555) 123-4567, Email: library@university.edu. Thủ thư tham khảo có mặt trong giờ mở cửa."
    },
    {
        "id": 8,
        "keywords": ["thẻ", "tài khoản", "đăng nhập", "đăng ký", "thẻ thư viện", "id"],
        "response": "🆔 Sử dụng thẻ sinh viên làm thẻ thư viện. Người dùng mới cần kích hoạt tài khoản tại quầy với giấy tờ tùy thân có ảnh."
    },
    {
        "id": 9,
        "keywords": ["gia hạn", "mượn", "trả", "hạn", "checkout", "renew"],
        "response": "🔄 Sách có thể gia hạn trực tuyến hoặc qua điện thoại nếu không có người đặt trước. Thời hạn: 3 tuần cho sinh viên, 1 tuần cho tài liệu dự trữ."
    },
    {
        "id": 10,
        "keywords": ["yên lặng", "im lặng", "ồn", "nói chuyện", "điện thoại", "tiếng ồn"],
        "response": "🤫 Tầng 2 là khu vực học tập yên tĩnh (không nói chuyện), Tầng 3 cho thảo luận nhóm, Tầng 1 là không gian hợp tác."
    },
    {
        "id": 11,
        "keywords": ["cơ sở dữ liệu", "nghiên cứu", "tạp chí", "bài báo", "học thuật", "database"],
        "response": "🔍 Truy cập hơn 200 cơ sở dữ liệu học thuật qua website. Cần hỗ trợ nghiên cứu? Đặt lịch tư vấn với thủ thư nghiên cứu."
    },
    {
        "id": 12,
        "keywords": ["đồ ăn", "đồ uống", "ăn", "cà phê", "nước", "thức ăn"],
        "response": "☕ Cho phép mang nước vào toàn bộ thư viện. Đồ ăn và đồ uống khác chỉ được phép ở khu vực chỉ định tầng 1 gần quán cà phê."
    },
    {
        "id": 13,
        "keywords": ["thất lạc", "mất", "để quên", "bỏ quên", "đồ thất lạc"],
        "response": "🔍 Kiểm tra đồ thất lạc tại quầy lễ tân. Đồ được giữ trong 30 ngày. Với đồ có giá trị, chúng tôi sẽ liên hệ nếu có thông tin."
    },
    {
        "id": 14,
        "keywords": ["photocopy", "scan", "sao chép", "photo", "máy photocopy"],
        "response": "📄 Máy photocopy/scan tự phục vụ có ở mỗi tầng. Thẻ photocopy có thể mua ở quầy lễ tân hoặc mang tiền lẻ."
    }
]

# Phản hồi mặc định khi không có quy tắc nào khớp
DEFAULT_RESPONSE = "🤖 Xin lỗi, tôi không hiểu câu hỏi của bạn. Vui lòng hỏi về giờ mở cửa, sách, phòng học, máy tính, hoặc liên hệ thủ thư để được hỗ trợ thêm!"

# Phản hồi chào hỏi
GREETING_KEYWORDS = ["xin chào", "chào", "hello", "hi", "chào buổi sáng", "chào buổi chiều", "chào buổi tối"]
GREETING_RESPONSE = "👋 Xin chào! Tôi là Trợ lý Thư viện. Tôi có thể giúp bạn thông tin về giờ mở cửa, tìm sách, đặt phòng học và nhiều hơn nữa. Bạn muốn biết gì?"
