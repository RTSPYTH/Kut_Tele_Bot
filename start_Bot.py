
from decouple import config
import telebot
from telebot import types

bot = telebot.TeleBot(config("TOKEN_BOT"))


@bot.message_handler(commands=["start", ])
def get_started(message):
    text = "Здравствуйте, добро пожаловать, с вами телеграмм бот строительной компании Кут. \nЧем я могу вам помочь?"
    murkup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton(text="Телефон☎️")
    btn2 = types.KeyboardButton(text="📍 Адрес🗺")
    btn3 = types.KeyboardButton(text="Сайт📧")
    btn4 = types.KeyboardButton(text="Режим работы🕖")
    btn5 = types.KeyboardButton(text="Объекты 🏠")
    btn6 = types.KeyboardButton(text="Оставить заявку 📝")
    murkup_reply.add(btn1, btn2, btn3, btn4, btn5, btn6)
    bot.send_message(message.chat.id, text, reply_markup=murkup_reply)


@bot.message_handler(func=lambda message: message.text == "Телефон☎️" or message.text == "📍 Адрес🗺"
                                          or message.text == "Сайт📧" or message.text == "Режим работы🕖"
                                          or message.text == "Объекты 🏠" or message.text == "Оставить заявку 📝")
def send_answer(message):
    if message.text == "Телефон☎️":
        text = "📞  <b>+996 557–00–99–00 \n📞  +996 507–00–99–00</b>"
        bot.send_message(message.chat.id, text, parse_mode='HTML')

    elif message.text == "📍 Адрес🗺":
        murkup_in = types.InlineKeyboardMarkup()
        text1 = "Выберите филиал:"
        btn1 = types.InlineKeyboardButton(text="1-ый филиал", callback_data="1-ый филиал")
        btn2 = types.InlineKeyboardButton(text="2-ой филиал", callback_data="2-ой филиал")
        murkup_in.add(btn1, btn2)
        bot.send_message(message.chat.id, text1, reply_markup=murkup_in)

    elif message.text == "Сайт📧":
        text = "https://kutstroy.kg"
        bot.send_message(message.chat.id, text)

    elif message.text == "Режим работы🕖":
        text = "<b>🤵 ПН-ПТ \n⏱ 09:00 - 19:00</b>"
        bot.send_message(message.chat.id, text, parse_mode='HTML')

    elif message.text == "Объекты 🏠":
        text = '🏠 Выберите объект:'
        markup_in = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text="Кут Парк", callback_data="kut_park")
        btn2 = types.InlineKeyboardButton(text="Умут", callback_data="umut")
        btn3 = types.InlineKeyboardButton(text="Ак Ниет", callback_data="ak_niet")
        btn4 = types.InlineKeyboardButton(text="Кут Орго", callback_data="kut_orgo")
        markup_in.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id, text, reply_markup=markup_in)

    elif message.text == "Оставить заявку 📝":
        chat_id = -624808870
        text = "Пожалуйста, заполните следующие поля:" \
               "\n<b>ФИО:</b>" \
               "\n<b>Ваш номер телефона:</b>" \
               "\n<b>Ваш email:</b>"
        bot.send_message(message.chat.id, text, parse_mode="HTML")
        bot.send_message(chat_id, text, parse_mode="HTML")


@bot.message_handler(content_types=['text'])
def send_to_group(message):
    msg = message.text
    chat_id = -624808870
    bot.send_message(chat_id, msg)


@bot.callback_query_handler(func=lambda call: call.data.startswith("1-ый филиал") or call.data.startswith("2-ой филиал"))
def send_query(call):
    if call.data == "1-ый филиал":
        text = "<b>📍 ул. Льва Толстого, 110 1 этаж</b>"
        link_to_gis = '[📍 Посмотреть в 2GIS](https://go.2gis.com/lnbsu)'
        bot.send_message(call.message.chat.id, text, parse_mode="HTML")
        bot.send_message(call.message.chat.id, link_to_gis, parse_mode='MarkdownV2')
    elif call.data == "2-ой филиал":
        text = "<b>📍 ул. Турусбекова, 109</b>"
        link_to_gis = '[📍 Посмотреть в 2GIS](https://go.2gis.com/ej6gh)'
        bot.send_message(call.message.chat.id, text, parse_mode="HTML")
        bot.send_message(call.message.chat.id, link_to_gis, parse_mode='MarkdownV2')


@bot.callback_query_handler(func=lambda call: call.data.startswith("kut_park")
                            or call.data.startswith("umut")
                            or call.data.startswith("ak_niet")
                            or call.data.startswith("kut_orgo"))
def send_request_room(call):
    if call.data == "kut_park":
        text = "<b>ЖК КУТ ПАРК</b> - это наш восьмой объект, он будет расположен по адресу <b>ул. Манаса/Васильева</b>. \
               \nКомплекс состоит из компактных и практичных планировок от 29 до 80м2.  \
               \n\n✔️750 квартир \
               \n✔️18 блоков \
                \n✔️5 этажей  \
                \n✔️2,5 га территория \
                \n✔️планировки от 29м2 до 80м2"
        photo_url = "https://kutstroy.kg/buildings/June2021/pfJ3NgxdJ8IXutUYxCJM.jpg"

    elif call.data == "umut":
        text = "<b>ЖК УМУТ</b> это наш девятый объект, который будет расположен по адресу <b>Джамгерчинова 291/Патриса Лумумбы.</b> \
                        \nКомплекс состоит из квартир с различными планировками от \
                        \n\n✔️672 квартир \
                        \n✔️10 блоков \
                        \n✔️9 этажей \
                        \n✔️2,5 га территория \
                        \nпланировки от 38-104м2"
        photo_url = "https://kutstroy.kg/buildings/August2021/vZAkqM6yVotcIuIM0ZfG.jpg"

    elif call.data == "ak_niet":
        text = "<b>ЖК АК НИЕТ</b> это  наш третий социальный объект, который строится по адресу <b>ул.7 апреля 1/1 (Горького/Алматинка)</b>. Особенность этого комплекса в его облегчённых условиях приобретения. Комплекс сдаётся без первоначального взноса с максимальным сроком рассрочки до 60 месяцев. \
                \n\n✔️1300 квартир \
                \n✔️19 блоков \
                \n✔️10 этажей \
                \n✔️3 га территория \
                \n✔️планировки от 40м2 до 104м2"
        photo_url = "https://kutstroy.kg/buildings/May2021/XDFcLDxdJfUqK2HHlHAD.jpg"

    elif call.data == "kut_orgo":
        text = "<b>ЖК КУТ ƟРГƟ</b> это наш второй социальный проект.  \
               Комплекс отличается своими условиями приобретения.  \
               Этот объект продаётся полностью без первоначального взноса. Удобное расположение комплекса, разумные планировки, наличие всех коммуникаций и многое другое  \
               гарантирует вам комфортное проживание. \
                \n\n✔️Количество этажей: 10 \
                \n✔️Количество блоков: 9 \
                \n✔️Количество квартир: 636 \
                \n✔️Планировки квартир от 30м2 до 126м2"
        photo_url = "https://kutstroy.kg/buildings/December2020/FLau7BupcjeIxcPkrj2Q.jpg"

    bot.send_message(call.message.chat.id, text, parse_mode="HTML")
    bot.send_photo(call.message.chat.id, photo_url)
    text = "Выберите квартиру: "
    markup_in = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("1 комнатная квартира", callback_data="one_room")
    btn2 = types.InlineKeyboardButton("2 комнатная квартира", callback_data="two_rooms")
    btn3 = types.InlineKeyboardButton("3 комнатная квартира", callback_data="three_rooms")
    markup_in.add(btn1, btn2, btn3)
    bot.send_message(call.message.chat.id, text, reply_markup=markup_in)


@bot.callback_query_handler(func=lambda call: call.data.startswith("one_room") or call.data.startswith("two_rooms")
                                              or call.data.startswith("three_rooms"))
def send_request_info(call):
    area1 = 42
    area2 = 64
    area3 = 80

    money1 = 550
    money2 = 600
    money3 = 650

    percentage1 = 30
    percentage2 = 25
    percentage3 = 23


    divide_by_month1 = 24
    divide_by_month2 = 36
    divide_by_month3 = 36

    if call.data == "one_room":
        text = "<b>1 комнатная квартира</b>"\
                f"\nОбщая площадь: {area1} м2 \
                \nСтоимость 1 м2 = {money1}$ \
                \nОбщая стоимость квартиры: {area1 * money1}$ \
                \nПервый взнос: {percentage1}% от общей стоимости = {area1 * money1 * percentage1/100}$ \
                \nРассрочка на каждый месяц ({divide_by_month1}):  \
                {round(((area1 * money1) - (area1 * money1 * percentage1 / 100)) / divide_by_month1,2)} $"
        bot.send_message(call.message.chat.id, text, parse_mode="HTML")

    elif call.data == "two_rooms":
        text = "<b>2 комнатная квартира</b>"\
                f"\nОбщая площадь: {area2} м2 \
                \nСтоимость 1 м2 = {money2}$ \
                \nОбщая стоимость квартиры: {area2 * money2}$ \
                \nПервый взнос: {percentage2}% от общей стоимости = {area2 * money2 * percentage2 / 100}$ \
                \nРассрочка на каждый месяц ({divide_by_month2}): \
                {round(((area2 * money2) - (area2 * money2 * percentage2 / 100)) / divide_by_month2,2)} $"
        bot.send_message(call.message.chat.id, text, parse_mode="HTML")

    elif call.data == "three_rooms":
        text = "<b>3 комнатная квартира</b>"\
                f"\nОбщая площадь: {area3} м2 \
                \nСтоимость 1 м2 = {money3}$ \
                \nОбщая стоимость квартиры: {area3 * money3}$ \
                \nПервый взнос: {percentage3}% от общей стоимости = {area3 * money3 * percentage3 / 100}$ \
                \nРассрочка на каждый месяц ({divide_by_month3}): \
                {round(((area3 * money3) - (area3 * money3 * percentage3 / 100)) / divide_by_month3,2)} $"
        bot.send_message(call.message.chat.id, text, parse_mode="HTML")
    text = "Если Вас устраивают условия, то оставьте заявку нажав на кнопку <b>'Оставить заявку 📝'</b>"
    bot.send_message(call.message.chat.id, text, parse_mode = 'HTML')

bot.polling()