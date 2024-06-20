import os
from botTelegram import bot, start_bot
from report_generator import generate_report
from email_sender import send_email
from utils.file_manager import clear_images

def main():
    print("Iniciando el bot de Telegram...")
    start_bot()

if __name__ == "__main__":
    main()
