import logging
from telegram import Update, Message
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Initialize GPT4Free client
from g4f.client import Client

client = Client()

# Configure logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


# Define the start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        'Hello! Send me a message with /ai or reply to one of my messages to get an AI response.')


# Define the /ai command handler
async def ai_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_message = ' '.join(context.args)
    if not user_message:
        await update.message.reply_text('Please provide a message after /ai.')
        return

    await generate_ai_response(update, user_message)


# Define a message handler for replies
async def handle_reply(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message.reply_to_message and update.message.reply_to_message.from_user.id == context.bot.id:
        user_message = update.message.text
        await generate_ai_response(update, user_message)


# Function to generate AI response
async def generate_ai_response(update: Update, user_message: str) -> None:
    await update.message.reply_text('Processing your request...')

    # Use GPT4Free to generate a response
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": user_message}],
        web_search=False
    )
    ai_message = response.choices[0].message.content

    # Send the AI-generated response back to the user
    await update.message.reply_text(ai_message)


# Define main function to run the bot
def main():
    # Replace 'YOUR_TOKEN_HERE' with your actual Telegram bot token
    application = Application.builder().token("YOUR TOKEN").build()

    # Register the command and message handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("ai", ai_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_reply))

    # Start the Bot
    application.run_polling()


if __name__ == '__main__':
    main()
