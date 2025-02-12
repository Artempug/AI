# AI
 simple Telegram bot using GPT-4o Mini (via GPT4Free) to generate AI responses. Supports /ai commands and replies. Built with python-telegram-bot

### Repository Description

**AI-Powered Telegram Bot with GPT-4o Mini**

This repository contains a simple yet powerful Telegram bot that utilizes **GPT-4o Mini** (via GPT4Free) to generate AI-driven responses. Users can interact with the bot using commands or by replying to its messages, making it a convenient AI chat assistant.

### Features:
- **/start** – Welcome message and usage instructions.
- **/ai <message>** – Sends a user-provided message to the AI and returns a response.
- **Reply Handling** – The bot responds to messages that reply to its previous outputs.
- **Logging** – Integrated logging for better monitoring and debugging.

### Technologies Used:
- **Python** – Core programming language.
- **python-telegram-bot** – Handles bot interactions.
- **GPT4Free (g4f)** – Provides AI responses without requiring OpenAI API keys.

### Setup & Usage:
1. Install dependencies:
   ```bash
   pip install python-telegram-bot g4f
   ```
2. Replace `"Your Token"` with your actual **Telegram bot token** in the `main()` function.
3. Run the bot:
   ```bash
   python bot.py
   ```
4. Start chatting with your AI-powered Telegram assistant!

🚀 **Feel free to fork, modify, and enhance the bot for your needs!**
