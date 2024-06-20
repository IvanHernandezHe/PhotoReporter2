import telebot
from telebot import types
from utils.file_manager import save_image, get_saved_images, clear_images

TOKEN = '7375526041:AAHjABWlwdK00t8C3dc6pgPvUSGYJ4MTaH8'

bot = telebot.TeleBot(TOKEN)

# ------------------------------------------------------- Incicio de bot ------------------------------------------------------------------------- #

#Comando /Start

@bot.message_handler(commands=['start'])
def send_welcome(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    create_report_button = types.KeyboardButton('Crear reporte')
    view_report_button = types.KeyboardButton('Ver reportes anteriores')

    markup.add(view_report_button,create_report_button)

    bot.reply_to(message, 'Bienvenido al reporteador fotográfico. \nSelecciona la opción a realizar.', reply_markup=markup)


# ------------------------------------------------------- Sección crear reporte ----------------------------------------------------------------- #

#Comando Crear reporte

@bot.message_handler(func=lambda message: message.text == 'Crear reporte')
def create_report(message):

    # Cual es el nombre del reporte?

    # Leer texto de reporte

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    end_button = types.KeyboardButton('Finalizar carga de imágenes')
    cancel_button = types.KeyboardButton('Cancelar')
    markup.add(cancel_button, end_button)
    bot.reply_to(message, 'Sesión de envío de imágenes iniciada. \nPuedes comenzar a enviar tus imágenes para crear el reporte...\n\nSelecciona "Finalizar" para terminar de cargar fotos.\nSelecciona "Cancelar" si deseas terminar la operación.', reply_markup=markup)

    #return titulo de reporte

    clear_images()


@bot.message_handler(func=lambda message: message.text == 'Finalizar carga de imágenes')
def end_session(message):
    bot.reply_to(message, 'Procesando imágenes...')
    generar_reporte(message.chat.id)

# def generate_report_and_send_email(chat_id):
#     from report_generator import generate_report
#     from email_sender import send_email
#     report_path = generate_report()
#     send_email(report_path)
#     bot.send_message(chat_id, 'El reporte ha sido enviado por correo.')


def generar_reporte(chat_id):
    
    #En esta función debería de recibir por parametro el texto
    images = get_saved_images()

    if len(images) == 0:
        bot.send_message(chat_id, 'No se recibio ninguna foto.\nVuelve a intentar o cancela la operación.')

    else:
        # generate_report()
        bot.send_message(chat_id, 'Generando reporte...')
        enviar_pdf_chat(chat_id)


def enviar_pdf_chat(chat_id):

    from report_generator import generate_report
    report_path = generate_report()

    if report_path:
        with open(report_path, 'rb') as report_file:
            bot.send_document(chat_id, report_file)
    else:
        bot.send_message(chat_id, 'Error al generar el reporte.')            


@bot.message_handler(content_types=['photo'])
def handle_image(message):
    # Descargar la foto
    file_info = bot.get_file(message.photo[-1].file_id)
    file = bot.download_file(file_info.file_path)
    save_image(file)
    
    # Crear y enviar teclado de respuesta
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    end_button = types.KeyboardButton('Finalizar carga de imágenes')
    cancel_button = types.KeyboardButton('Cancelar')
    markup.add(cancel_button, end_button)
    
    # Enviar mensaje de confirmación
    bot.reply_to(message, 'Imagen recibida.',reply_markup=markup)
    






# ------------------------------------------------------- Seccion ver reportes anteriores ------------------------------------------------------- #

#Comando ver reportes anteriores

@bot.message_handler(func=lambda message: message.text == 'Ver reportes anteriores')
def view_reports(message):
    bot.reply_to(message, 'Función en proceso.')

# ------------------------------------------------------- Seccion ver reportes anteriores ------------------------------------------------------- #


@bot.message_handler(func=lambda message: message.text == 'Cancelar')
def cancel(message):
    send_welcome(message)













def start_bot():
    bot.polling(none_stop=True)

if __name__ == "__main__":
    start_bot()
