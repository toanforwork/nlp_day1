# Flask web application for Vietnamese Library Assistant Chatbot
from flask import Flask, render_template, request, jsonify
from chatbot import chatbot
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    """Render the main Vietnamese chatbot interface"""
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    """Handle chat messages and return bot response in Vietnamese"""
    try:
        data = request.get_json()
        user_message = data.get('message', '').strip()
        
        if not user_message:
            return jsonify({
                'response': 'Vui lòng nhập tin nhắn!',
                'timestamp': datetime.datetime.now().strftime('%H:%M')
            })
        
        # Get bot response
        bot_response = chatbot.get_response(user_message)
        
        return jsonify({
            'response': bot_response,
            'timestamp': datetime.datetime.now().strftime('%H:%M'),
            'user_message': user_message
        })
        
    except Exception as e:
        return jsonify({
            'response': 'Xin lỗi, tôi gặp lỗi. Vui lòng thử lại.',
            'timestamp': datetime.datetime.now().strftime('%H:%M'),
            'error': str(e)
        }), 500

@app.route('/help')
def help():
    """Return help information in Vietnamese"""
    help_message = chatbot.get_help_message()
    return jsonify({
        'response': help_message,
        'timestamp': datetime.datetime.now().strftime('%H:%M')
    })

@app.route('/rules')
def rules():
    """Show all available Vietnamese rules (for debugging/demo purposes)"""
    from chatbot.rules import CHATBOT_RULES
    return jsonify({
        'rules': CHATBOT_RULES,
        'total_rules': len(CHATBOT_RULES),
        'language': 'Vietnamese'
    })

if __name__ == '__main__':
    print("🚀 Đang khởi động Trợ lý Thư viện Tiếng Việt...")
    print("📚 Quy tắc đã tải:", len(chatbot.rules))
    print("🌐 Truy cập chatbot tại: http://localhost:5001")
    app.run(debug=True, host='0.0.0.0', port=5001)
