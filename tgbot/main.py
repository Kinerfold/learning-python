import os
import telebot
import speech_recognition as sr
from pydub import AudioSegment
from config import TOKEN
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

bot = telebot.TeleBot(TOKEN, threaded=True)

VOICE_DIR = "voices"
os.makedirs(VOICE_DIR, exist_ok=True)


def ogg_to_wav(ogg_path, wav_path):
    try:
        audio = AudioSegment.from_file(ogg_path, format="ogg")
        audio.export(wav_path, format="wav")
        logger.info(f"Конвертирован: {ogg_path} -> {wav_path}")
    except Exception as e:
        logger.error(f"Ошибка конвертации: {e}")
        raise


def recognize_speech(wav_path):
    recognizer = sr.Recognizer()
    
    try:
        with sr.AudioFile(wav_path) as source:
            audio = recognizer.record(source)
        
        text = recognizer.recognize_google(audio, language="ru-RU")
        logger.info(f"Распознано: {text}")
        return text
    except sr.UnknownValueError:
        logger.warning("Не удалось распознать речь")
        return "Не удалось распознать речь"
    except sr.RequestError as e:
        logger.error(f"Ошибка сервиса: {e}")
        return "Ошибка сервиса распознавания"
    except Exception as e:
        logger.error(f"Неожиданная ошибка: {e}")
        return "Ошибка при обработке"


@bot.message_handler(content_types=["voice"])
def handle_voice(message):
    try:
        
        bot.send_chat_action(message.chat.id, 'typing')
        
        logger.info(f"Получено голосовое сообщение от {message.from_user.id}")
        
        file_info = bot.get_file(message.voice.file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        ogg_path = os.path.join(VOICE_DIR, f"{message.message_id}.ogg")
        wav_path = os.path.join(VOICE_DIR, f"{message.message_id}.wav")

        with open(ogg_path, "wb") as f:
            f.write(downloaded_file)
        logger.info(f"Сохранен OGG файл: {ogg_path}")

        ogg_to_wav(ogg_path, wav_path)

        text = recognize_speech(wav_path)

        bot.send_message(message.chat.id, f"📝 Распознанный текст:\n\n{text}")

        try:
            if os.path.exists(ogg_path):
                os.remove(ogg_path)
            if os.path.exists(wav_path):
                os.remove(wav_path)
            logger.info("Временные файлы удалены")
        except Exception as e:
            logger.warning(f"Ошибка при удалении файлов: {e}")
            
    except Exception as e:
        logger.error(f"Ошибка при обработке голоса: {e}")
        bot.send_message(message.chat.id, f"Ошибка: {str(e)}")


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(
        message.chat.id,
        "Привет! Отправь мне голосовое сообщение, и я распознаю речь.\n\n"
        "Я поддерживаю русский язык.\n\n"
        "Говори чётко для лучшего распознавания."
    )


@bot.message_handler(commands=["help"])
def help_command(message):
    bot.send_message(
        message.chat.id,
        "Справка:\n\n"
        "Отправь голосовое сообщение\n"
        "Дожди обработки\n"
        "Получи распознанный текст\n\n"
        "Команды:\n"
        "/start - Начало\n"
        "/help - Справка"
    )


@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.send_message(message.chat.id, "Отправь мне голосовое сообщение")


if __name__ == "__main__":
    logger.info(" Бот запущен...")
    try:
        bot.infinity_polling(timeout=60, long_polling_timeout=60)
    except KeyboardInterrupt:
        logger.info("Бот остановлен")
    except Exception as e:
        logger.error(f"Ошибка: {e}")
