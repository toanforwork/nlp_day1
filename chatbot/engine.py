# Vietnamese Rule-based chatbot engine
import re
from .rules import CHATBOT_RULES, DEFAULT_RESPONSE, GREETING_KEYWORDS, GREETING_RESPONSE

class VietnameseLibraryChatbot:
    def __init__(self):
        self.rules = CHATBOT_RULES
        self.conversation_history = []
    
    def preprocess_input(self, user_input):
        """Làm sạch và chuẩn hóa đầu vào của người dùng"""
        # Chuyển về chữ thường và loại bỏ khoảng trắng thừa
        processed = user_input.lower().strip()
        # Loại bỏ dấu câu trừ dấu nháy
        processed = re.sub(r"[^\w\s']", "", processed)
        return processed
    
    def remove_vietnamese_accents(self, text):
        """Loại bỏ dấu tiếng Việt để so khớp linh hoạt hơn"""
        # Bản đồ chuyển đổi từ có dấu sang không dấu
        vietnamese_map = {
            'á': 'a', 'à': 'a', 'ả': 'a', 'ã': 'a', 'ạ': 'a',
            'ấ': 'a', 'ầ': 'a', 'ẩ': 'a', 'ẫ': 'a', 'ậ': 'a',
            'ắ': 'a', 'ằ': 'a', 'ẳ': 'a', 'ẵ': 'a', 'ặ': 'a',
            'é': 'e', 'è': 'e', 'ẻ': 'e', 'ẽ': 'e', 'ẹ': 'e',
            'ế': 'e', 'ề': 'e', 'ể': 'e', 'ễ': 'e', 'ệ': 'e',
            'í': 'i', 'ì': 'i', 'ỉ': 'i', 'ĩ': 'i', 'ị': 'i',
            'ó': 'o', 'ò': 'o', 'ỏ': 'o', 'õ': 'o', 'ọ': 'o',
            'ố': 'o', 'ồ': 'o', 'ổ': 'o', 'ỗ': 'o', 'ộ': 'o',
            'ớ': 'o', 'ờ': 'o', 'ở': 'o', 'ỡ': 'o', 'ợ': 'o',
            'ú': 'u', 'ù': 'u', 'ủ': 'u', 'ũ': 'u', 'ụ': 'u',
            'ứ': 'u', 'ừ': 'u', 'ử': 'u', 'ữ': 'u', 'ự': 'u',
            'ý': 'y', 'ỳ': 'y', 'ỷ': 'y', 'ỹ': 'y', 'ỵ': 'y',
            'đ': 'd'
        }
        
        result = ""
        for char in text:
            result += vietnamese_map.get(char, char)
        return result
    
    def check_greeting(self, user_input):
        """Kiểm tra xem đầu vào có phải lời chào không"""
        processed_input = self.preprocess_input(user_input)
        words = processed_input.split()
        
        for word in words:
            for greeting in GREETING_KEYWORDS:
                if word == greeting.lower() or self.remove_vietnamese_accents(word) == self.remove_vietnamese_accents(greeting.lower()):
                    return True
        return False
    
    def find_matching_rule(self, user_input):
        """Tìm quy tắc khớp tốt nhất dựa trên sự xuất hiện của từ khóa"""
        processed_input = self.preprocess_input(user_input)
        processed_no_accent = self.remove_vietnamese_accents(processed_input)
        
        # Kiểm tra lời chào trước
        if self.check_greeting(user_input):
            return GREETING_RESPONSE
        
        # Tính điểm cho mỗi quy tắc dựa trên từ khóa khớp
        rule_scores = []
        
        for rule in self.rules:
            score = 0
            matched_keywords = []
            
            for keyword in rule["keywords"]:
                keyword_lower = keyword.lower()
                keyword_no_accent = self.remove_vietnamese_accents(keyword_lower)
                
                # Kiểm tra từ khóa xuất hiện trong đầu vào
                if keyword_lower in processed_input or keyword_no_accent in processed_no_accent:
                    score += 1
                    matched_keywords.append(keyword)
                    
                # Kiểm tra khớp một phần (để xử lý lỗi chính tả)
                words = processed_input.split()
                words_no_accent = processed_no_accent.split()
                
                for word, word_no_accent in zip(words, words_no_accent):
                    if len(word) > 2 and len(keyword_lower) > 2:
                        # Kiểm tra tương tự đơn giản cho lỗi chính tả
                        if (self.simple_similarity(word, keyword_lower) > 0.7 or 
                            self.simple_similarity(word_no_accent, keyword_no_accent) > 0.7):
                            score += 0.5
                            if keyword not in matched_keywords:
                                matched_keywords.append(keyword)
            
            if score > 0:
                rule_scores.append({
                    "rule": rule,
                    "score": score,
                    "matched_keywords": matched_keywords
                })
        
        # Trả về quy tắc có điểm cao nhất
        if rule_scores:
            best_rule = max(rule_scores, key=lambda x: x["score"])
            return best_rule["rule"]["response"]
        
        return DEFAULT_RESPONSE
    
    def simple_similarity(self, word1, word2):
        """Tính toán độ tương tự đơn giản giữa hai từ"""
        if len(word1) == 0 or len(word2) == 0:
            return 0
        
        # Đếm ký tự chung
        common_chars = 0
        for char in word1:
            if char in word2:
                common_chars += 1
        
        # Điểm tương tự đơn giản
        similarity = common_chars / max(len(word1), len(word2))
        return similarity
    
    def get_response(self, user_input):
        """Lấy phản hồi chatbot cho đầu vào người dùng"""
        if not user_input or not user_input.strip():
            return "Vui lòng hỏi tôi một câu hỏi về thư viện!"
        
        # Lưu trữ cuộc trò chuyện
        self.conversation_history.append({"user": user_input, "timestamp": None})
        
        # Tìm quy tắc khớp và lấy phản hồi
        response = self.find_matching_rule(user_input)
        
        # Lưu trữ phản hồi bot
        self.conversation_history.append({"bot": response, "timestamp": None})
        
        return response
    
    def get_help_message(self):
        """Trả về thông điệp trợ giúp với các chủ đề có sẵn"""
        help_text = """
        🆘 Tôi có thể giúp bạn với:
        • Giờ mở cửa và lịch hoạt động thư viện
        • Tìm kiếm và tra cứu sách
        • Đặt phòng học
        • Truy cập máy tính và máy in
        • Phí và tiền phạt thư viện
        • Vị trí và đường đi
        • Thông tin liên hệ
        • Chính sách thư viện
        • Thông tin tài khoản và thẻ
        • Cơ sở dữ liệu và tài nguyên nghiên cứu
        
        Hãy hỏi tôi câu hỏi về bất kỳ chủ đề nào trong số này!
        """
        return help_text.strip()

# Tạo instance chatbot toàn cục
chatbot = VietnameseLibraryChatbot()
