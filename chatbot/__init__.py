# Make Vietnamese chatbot package importable
from .engine import chatbot
from .rules import CHATBOT_RULES

__all__ = ['chatbot', 'CHATBOT_RULES']
