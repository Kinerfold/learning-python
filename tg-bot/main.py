import os
import telebot
import speech_recognition as sr
from pydub import AudioSegment
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

if not os.path.exists("voices"):
    os.mkdir("voices")

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(
        message.chat.id,
        "Привет! Отправь голосовое сообщение, и я переведу его в текст."
    )

@bot.message_handler(content_types=["voice"])
def voice_to_text(message):
    try:
        file_info = bot.get_file(message.voice.file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        ogg_path = f"voices/{message.voice.file_id}.ogg"
        wav_path = f"voices/{message.voice.file_id}.wav"

        with open(ogg_path, "wb") as f:
            f.write(downloaded_file)

        sound = AudioSegment.from_ogg(ogg_path)
        sound.export(wav_path, format="wav")

        r = sr.Recognizer()
        with sr.AudioFile(wav_path) as source:
            audio = r.record(source)

        text = r.recognize_google(audio, language="ru-RU")
        bot.reply_to(message, f"Я услышал:\n{text}")

        os.remove(ogg_path)
        os.remove(wav_path)
    except Exception as e:
        print(e)
        bot.reply_to(message, "Не удалось распознать голосовое сообщение :(")

print("Бот запущен")
bot.infinity_polling()