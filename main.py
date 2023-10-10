from aiogram import Bot,  types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import os
from keyboards import start_menu, services_menu, connect_back, subscribe
from dotenv import load_dotenv
import os
load_dotenv()

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await bot.send_photo(message.chat.id, photo=open('img/arbitra_main.jpg', 'rb'), caption="""
<b>Привіт! Це бот Телеграм-агенції arbitra. Раді тебе бачити тут! Чим можемо бути корисні?</b>\n
"<b>Консультація</b>" - отримати глибоку професійну консультацію стосовно будь-якого питання в ТГ\n
"<b>Послуги</b>" - дізнатись,які послуги ми надаємо та прайс на них\n
"<b>Навчання</b>" - переглянути освітні можливості, які надає наша команда\n
"<b>Подарунок</b>" -  отримати безкоштовні корисні матеріали""", reply_markup=start_menu, parse_mode="HTML")

#     await message.answer_photo("""
# <b>Привіт! Це бот Телеграм-агенції arbitra. Раді тебе бачити тут! Чим можемо бути корисні?</b>\n
# "<b>Консультація</b>" - отримати глибоку професійну консультацію стосовно будь-якого питання в ТГ\n
# "<b>Послуги</b>" - дізнатись,які послуги ми надаємо та прайс на них\n
# "<b>Навчання</b>" - переглянути освітні можливості, які надає наша команда\n
# "<b>Подарунок</b>" -  отримати безкоштовні корисні матеріали""", reply_markup=start_menu, parse_mode="HTML")


@dp.callback_query_handler()
async def check_button(call: types.CallbackQuery):
    user_id = call['from']['id']
    user_found = False
    with open("users_id.txt", 'r') as file:
        if os.stat("users_id.txt").st_size != 0:
            for id in file.readlines():
                if f'{user_id} \n'  == id:
                    user_found = True
        else:
            user_found = False


    if not user_found:
        with open("users_id.txt", 'a') as file:
            file.write(f'{user_id} \n')

    if call.data == "Service":
        await call.message.answer_photo(open('img/arbitra_service.jpg','rb'), caption="<b>Наші послуги:</b>\n\n1. Створення <b>рекламних креативів</b>\n\n2. Професійний <b>закуп реклами</b>\n\n3. <b>Налагодження процесів</b> у ТГ-бізнесі\n\n4.<b> Підбір каналу</b> на покупку\n\n5. <b>Посередництво</b> при укладенні угод 6. <b>Розробка ботів</b> будь-якої складності\n\nДізнатись деталі про послугу - обирай кнопку з відповідною цифрою!", reply_markup=services_menu, parse_mode="HTML")

    
    elif call.data == "Consultation":
        await call.message.answer_photo(open('img/arbitra_consultation.jpg','rb'), caption="Якщо тобі потрібна <b>професійна консультація практика в ТГ-бізнесі</b>, після якої ти не тільки зрозумієш як все працює, а і отримаєш купу крутих порад - звертайся до нас, ми в цьому допоможемо!  \n\nТи можеш задавати абсолютно <b>будь-які питання</b>, ми з радістю відповімо на них. \n\nЩоб замовити, пиши менеджеру '<code>Хочу консультацію!</code>' \n\n<b>Контакт: @arb1tra_manager</b>", reply_markup=connect_back, parse_mode="HTML")
    
    elif call.data == "Teaching":
        await call.message.answer_photo(open('img/arbitra_teaching.jpg','rb'), caption="<b>Навчання ми оформили у вигляді посібника</b>, в якому зручно переглядати теми, які цікавлять і за потреби повертатись до них. \nУ вищих рівнях доступу є також <b>додаткові плюшки)</b>  \n\nУ файлі, прикріпленому нижче ти можеш ознайомитись із рівнями доступу детально та обрати той варіант, який тобі <b>підходить найбільше:</b>", parse_mode="HTML")

        with open("tarifs_arbitra.pdf", 'rb') as file:
            await call.message.answer_document(file)
        await call.message.answer("Тепер, коли ти розумієш, який <b>рівень потрібен</b> - пиши менеджеру текст: '<code>Хочу навчання від arbitra</code>' та вказуй рівень!  \n\n<b>Контакт: @arb1tra_manager</b>", reply_markup=connect_back, parse_mode="HTML")
    
    elif call.data == "Present":    
        await call.message.answer("<b>Підготували цілу купу подарунків, які тобі точно будуть корисними і допоможуть працювати в ТГ ще ефективніше:</b>   \n\n1. <b>CRM-система</b> для Телеграм-каналів. \n\nЗабудь про застарілі і незручні ексельки, <b>виведи керування проектами на новий рівень</b> разом із нашою системою.   \n\n2. <b>Гайд по продажу реклами</b> - керівництво по тому, як потрібно <b>продавати рекламу</b> в Телеграм-каналах.   \n\n3. <b>Самий повний список чатів і каналів</b>, які просто необхідні для роботи. Біржі, корисне, новини та багато іншого - <b>все там!</b>   \n\nПерш ніж отримати, <b>підпишись на наші ресурси</b> :)", reply_markup=subscribe, parse_mode="HTML")
    
    if call.data == "one":
        await call.message.answer_photo(open('img/arbitra_creative.jpg','rb'), caption="<b>Потрібен рекламний креатив з високою конверсією? Ми працюємо до результату!</b> \n\nВартість <b>1 креативу - 100$</b>, необмежені правки до результату 8грн / пдп \n\n<b>Вартість 5 креативів - 250$</b>, необмежені правки до результату 8грн / пдп  \n\n<i>*для каналів звичайних тематик, складні і нестандартні тематики обговорюються окремо</i> \n\nЩоб замовити, пиши менеджеру '<code>Хочу креатив!</code>'  \n\n<b>Контакт: @arb1tra_manager</b>", reply_markup=connect_back, parse_mode="HTML")

    elif call.data == "two":
        await call.message.answer_photo(open('img/arbitra_adbuy.jpg','rb'), caption="<b>Треба багато якісного трафіку з Телеграм-каналів? Закупаємо професійно будь-які об'єми! </b>\n\n  Мінімальний бюджет - <b>50 000грн</b>, Вартість послуги - <b>20%*</b> від бюджету.  \n*на великих бюджетах можливий торг :)   \n\n<b>У послугу входить:</b> \n- підбір креативів \n- слідкування за якістю креативу \n- підбір каналів для розміщення \n- комунікація з адмінами \n- розміщення по вигідним цінам \n- формування та надання статистики закупу \n- аналітика + консультація по додатковим джерелам трафіку.   \n\nЩоб замовити, пиши менеджеру '<code>Хочу закуп!</code>'  \n\n<b>Контакт: @arb1tra_manager</b>", reply_markup=connect_back, parse_mode="HTML")

    elif call.data == "three":
        await call.message.answer_photo(open('img/arbitra_processes.jpg','rb'), caption="<b>Ми допоможемо тобі налагодити усі процеси твого Телеграм-бізнесу!</b>   \n\nДо послуги входить: \n- Налаштування процесів постингу на канал \n- підбір контентщика \n- визначення форматів\n- візуальне оформлення\n- налаштування ботів для постингу реклами та інструкція за потреби \n- Налаштування СРМ-системи для каналів \n- рекомендації по взаємодії з працівниками та іншими адмінами \n- Гайд по продажу реклами \n- Допомога в оформленні та веденні ФОП   Вартість <b>250$</b>/канал   \n\nЩоб замовити, пиши менеджеру '<code>Хочу налаштування!</code>'  \n\n<b>Контакт: @arb1tra_manager</b>", reply_markup=connect_back, parse_mode="HTML")

    elif call.data == "four":
        await call.message.answer_photo(open('img/arbitra_channelcheck.jpg','rb'), caption="<b>Хочеш придбати готовий бізнес в ТГ, але боїшся шахраїв чи потрапити на неякісний канал? Ми тобі допоможемо обрати найкращий варіант на ринку!</b>   \n\nВартість перевірки 1 каналу - <b>500грн</b>   \n\nВартість повного підбору - <b>150$</b>   \n\nЩоб замовити, пиши менеджеру '<code>Хочу підбір!</code>'  \n\n<b>Контакт: @arb1tra_manager</b>", reply_markup=connect_back, parse_mode="HTML")

    elif call.data == "five":
        await call.message.answer_photo(open('img/arbitra_poserednutsvo.jpg','rb'), caption="<b>Хочеш придбати готовий бізнес в ТГ, але боїшся шахраїв? \nПроведи угоду через нашого гаранта, безпека угоди гарантована!</b>  \n\n Вартість послуги посередництва - 3% але не менше 500грн   Також ти отримаєш список рекомендацій стосовно того, як захистити себе та свій бізнес від зловмисників!   Щоб замовити, пиши менеджеру '<code>Треба гарант!</code>'  \n\n<b>Контакт: @arb1tra_manager</b>", reply_markup=connect_back, parse_mode="HTML")

    elif call.data == "six":
        await call.message.answer_photo(open('img/arbitra_botdev.jpg','rb'), caption="<b>Розробка Телеграм-ботів будь-якої складності! Отримай якісний продукт, який не підведе тебе та твої очікування.</b>   \n\nВартість розробки - найнижча ціна на ринку, від 50$   \n\nЩоб замовити, пиши менеджеру '<code>Хочу бота!</code>'  \n\n<b>Контакт: @arb1tra_manager</b>", reply_markup=connect_back, parse_mode="HTML")
    
    if call.data == "service_back":
        await call.message.answer_photo(open('img/arbitra_main.jpg','rb'), caption="<b>Чим можемо бути корисні?</b> \n\n'<b>Консультація</b>' - отримати глибоку професійну консультацію стосовно будь-якого питання в ТГ \n\n'<b>Послуги</b>' - дізнатись, які послуги ми надаємо та прайс на них \n\n'<b>Навчання</b>' - переглянути освітні можливості, які надає наша команда  \n\n'<b>Сервіс</b>'- ознайомитись із корисним функціоналом для ТГ-адмінів та менеджерів \n\n'<b>Подарунок</b>' - отримати безкоштовні корисні матеріали", reply_markup=start_menu, parse_mode="HTML")
    
    if call.data == "connect_back":
        await call.message.answer_photo(open('img/arbitra_service.jpg','rb'), caption="Наші послуги:\n\n1. Створення рекламних креативів\n\n2. Професійний закуп реклами\n\n3. Налагодження процесів у ТГ-бізнесі\n\n4. Підбір каналу на покупку\n\n5. Посередництво при укладенні угод 6. Розробка ботів будь-якої складності\n\nДізнатись деталі про послугу - обирай кнопку з відповідною цифрою!", reply_markup=services_menu, parse_mode="HTML")
    
    if call.data == "consultation_back":
        await call.message.answer_photo(open('img/arbitra_main.jpg','rb'), caption="Чим можемо бути корисні?   'Консультація' - отримати глибоку професійну консультацію стосовно будь-якого питання в ТГ   'Послуги' - дізнатись, які послуги ми надаємо та прайс на них   'Навчання' - переглянути освітні можливості, які надає наша команда   'Сервіс'- ознайомитись із корисним функціоналом для ТГ-адмінів та менеджерів   'Подарунок' - отримати безкоштовні корисні матеріали", reply_markup=start_menu, parse_mode="HTML")
    
    if call.data == 'subscribe_done':
        chats = [
            '@arb1tra',
            '@community_arb1tra',
            '@channels_arb1tra',
            '@sellads_arb1tra',
            '@buyads_arb1tra'
        ]
        subscribed = True
        for chat in chats:
            user_channel_status = await bot.get_chat_member(chat_id=chat, user_id=call['from']['id'])
            if user_channel_status['status'] == 'left':
                subscribed = False
                
            
        if subscribed:
            await call.message.answer("<b>Дякую за підписку! Тримай свої подарунки:</b> \n\n1. <b>Telegram Dashboard</b> - https://arbitra.notion.site/Telegram-Dashboard-5e2a194e404d406897d289dd23e7508d?pvs=4 \n<b>Інструкція</b> - https://youtu.be/Lw8vy9Lcvyk \n\n2. <b>Гайд по продажу реклами в Telegram</b> - \nhttps://arbitra.notion.site/Telegram-76942dd5e4e5434c9502c61df3bd20ba?pvs=4 \n\n3. <b>Самий повний список адмінських чатів, каналів, бірж</b> - \nhttps://arbitra.notion.site/bonus-4-987493b887ee4688b414f33432cec023?pvs=4", parse_mode="HTML", reply_markup=connect_back)            
        else:
            await call.message.answer("Ой... Пiдписку не пiдтверджено. <b>Перевiр, чи є підписка на всі ресурси!</b>", parse_mode="HTML")
    await call.answer()


@dp.message_handler(text='/specialcodefornotify')
async def notify_users(message: types.Message):
    with open("users_id.txt", 'r') as file:
        for id in file.readlines():
            await bot.send_message(id, 'Тестова розсилка!', parse_mode="HTML")

if __name__ == '__main__':
    executor.start_polling(dp)