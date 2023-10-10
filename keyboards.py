from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start_btn1 = InlineKeyboardButton(text="Консультація", callback_data="Consultation")
start_btn2 = InlineKeyboardButton(text="Послуги", callback_data="Service")
start_btn3 = InlineKeyboardButton(text="Навчання", callback_data="Teaching")
start_btn4 = InlineKeyboardButton(text="Подарунок", callback_data="Present")
start_btn5 = InlineKeyboardButton(text="Сервіс", callback_data="bla")
start_btn6 = InlineKeyboardButton(text="Інвестиції в ТГ", callback_data="bla")
start_menu = InlineKeyboardMarkup().add(start_btn1,start_btn2,start_btn3,start_btn4,start_btn5,start_btn6)

services_btn1 = InlineKeyboardButton(text="1", callback_data="one")
services_btn2 = InlineKeyboardButton(text="2", callback_data="two")
services_btn3 = InlineKeyboardButton(text="3", callback_data="three")
services_btn4 = InlineKeyboardButton(text="4", callback_data="four")
services_btn5 = InlineKeyboardButton(text="5", callback_data="five")
services_btn6 = InlineKeyboardButton(text="6", callback_data="six")
service_back_btn = InlineKeyboardButton(text="Назад", callback_data="service_back")

services_menu = InlineKeyboardMarkup().add(services_btn1,services_btn2,services_btn3,services_btn4,services_btn5,services_btn6)
services_menu.add(service_back_btn)

connect_btn1 = InlineKeyboardButton(text="Зв'язок", callback_data="connect")
connect_btn2 = InlineKeyboardButton(text="Назад", callback_data="connect_back")

connect_back = InlineKeyboardMarkup().add(connect_btn1)
connect_back.add(connect_btn2)

consultation_btn1 = InlineKeyboardButton(text="Зв'язок", callback_data="connect", url="https://t.me/arb1tra_manager")
consultation_btn2 = InlineKeyboardButton(text="Назад", callback_data="consultation_back")

connect_back = InlineKeyboardMarkup().add(consultation_btn1)
connect_back.add(consultation_btn2)

subscribe_btn1 = InlineKeyboardButton(text="Канал", callback_data="subscribe_1", url="https://t.me/arb1tra")
subscribe_btn2 = InlineKeyboardButton(text="Чат", callback_data="subscribe_2", url="https://t.me/community_arb1tra")
subscribe_btn3 = InlineKeyboardButton(text="Біржа каналів", callback_data="subscribe_3", url="https://t.me/channels_arb1tra")
subscribe_btn4 = InlineKeyboardButton(text="Біржа реклами", callback_data="subscribe_4", url="https://t.me/sellads_arb1tra")
subscribe_btn5 = InlineKeyboardButton(text="Покупка реклами", callback_data="subscribe_5", url="https://t.me/buyads_arb1tra")
subscribe_btn6 = InlineKeyboardButton(text="Готово!", callback_data="subscribe_done")

subscribe = InlineKeyboardMarkup().add(subscribe_btn1, subscribe_btn2)
subscribe.add(subscribe_btn3,subscribe_btn4)
subscribe.add(subscribe_btn5,subscribe_btn6)