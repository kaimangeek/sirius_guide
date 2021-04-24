from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram import ReplyKeyboardMarkup

TOKEN = '1566338322:AAEXng78RsvoT8mhr4Voqd8-P65_qFv3YTw'


def start(update, context):
    reply_keyboard = [['/sport_objects', '/amusements_objects'],
                      ['/education_objects']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text(
        "Приветствую, исследователь! Я бот-экскурсовод, который поможет тебе разобраться в федеральной территории "
        "«Сириус»"
        ". О каких объектах инфраструктуры Вы бы хотели узнать?",
        reply_markup=markup
    )


def help(update, context):
    update.message.reply_text(
        "Напишите /start")


def back(update, context):
    reply_keyboard = [['/sport_objects', '/amusements_objects'],
                      ['/education_objects']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
    update.message.reply_text(
        "Возвращаюсь обратно",
        reply_markup=markup
    )


def sport_objects(update, context):
    reply_keyboard = [['/Formula_1_track', '/Fisht_stadium', 'Speed_skating_center_Adler_Arena'],
                      ['/Ice_Palace_Bolshoi', '/Ice_arena_Puck', '/Curling_Center_Ice_Cube'],
                      ['/Ice_Palace_Iceberg', '/back']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text(
        "О каком объекте вы хотели бы узнать поподробнее?",
        reply_markup=markup
    )


def Fisht_stadium(update, context):
    context.bot.send_photo(
        update.message.chat_id,
        'https://api.parkseason.ru/images/54/f1/87a6da52ada2110573af4296c05836285a7bfd4995b54246948917.jpg')
    update.message.reply_text(
        "Этот объект считается самым грандиозным и основным сооружением. Здесь проходили церемонии открытия и закрытия"
        " XXII Зимних Олимпийских игр. После стадион закрыли на реконструкцию. В 2017 году здесь прошли футбольные "
        "матчи"
        " Кубка Конфедераций и финал Кубка России. На сегодняшний день на стадионе проводятся тренировки и матчи по "
        "футболу, а также идет подготовка к проведению Чемпионата Мира-2018."
    )


def Formula_1_track(update, context):
    context.bot.send_photo(
        update.message.chat_id,
        'https://kubnews.ru/upload/iblock/a06/a06c0a2710b160e7031b4b523dd1fbcd.jpg')
    update.message.reply_text(
        "Формула 1 – это высшая категория в автоспорте для машин с открытыми колесами. В ней сильнейшие пилоты ведут"
        " борьбу под пристальным вниманием миллионов болельщиков по всей планете."
    )


def Speed_skating_center_Adler_Arena(update, context):
    context.bot.send_photo(
        update.message.chat_id,
        'https://api.parkseason.ru/images/b1/07/e36f0d944dd622e7088a1612715ef91d5a7bfcdbaf0a3102175977.jpg')
    update.message.reply_text(
        "После открытия здесь прошли соревнования по конькобежному спорту. В апреле 2014 года на «Адлер-Арене» "
        "состоялся"
        " матч Кубка Федерации по теннису между женскими сборными России и Аргентины. Помимо этого, прошло первенство "
        "России по вольной борьбе среди юниоров. С сентября того же года на территории начала работу теннисная "
        "академия."
        " Также сегодня здесь находится центр гимнастики Юлии Барсуковой и тренажерный зал."
    )


def Ice_Palace_Bolshoi(update, context):
    context.bot.send_photo(
        update.message.chat_id,
        'https://api.parkseason.ru/images/b4/2e/b289405b70bbb80308d8b71cc64adb885a7bfeeb4d197423724946.jpg')
    update.message.reply_text(
        "Во время Олимпиады-2014, дворец был основным хоккейным стадионом. После, чтобы сооружение не пустовало, "
        "был создан хоккейный клуб «Сочи». Команда проводит здесь тренировки и матчи. Помимо этого, в стенах «Большого»"
        "был проведен Кубок Первого канала и матч Всех звезд КХЛ. На сегодняшний день стадион один из самых загруженных"
        "из всех Олимпийских объектов."
    )


def Ice_arena_Puck(update, context):
    context.bot.send_photo(
        update.message.chat_id,
        'https://api.parkseason.ru/images/64/7b/776f6c439938f501e4be18e3a3afe3fe5a7bfd52f3482852467996.jpg')
    update.message.reply_text(
        "В 2014 году здесь проводился хоккей и следж-хоккей паралимпиады. После планировалось переносить стадион во "
        "Владикавказ или в Краснодар, но идея провалилась из-за особенностей конструкции фундамента. Было принято "
        "решение об открытии Всероссийского детского спортивно-оздоровительного центра. С 2015 года здесь проводятся "
        "постоянные тренировки юных фигуристов и хоккеистов. С мая 2016 года часть площади «Шайбы» используется для "
        "шахматных классов."
    )


def Curling_Center_Ice_Cube(update, context):
    context.bot.send_photo(
        update.message.chat_id,
        'https://api.parkseason.ru/images/6f/de/349e4ffd1e42f9e76d658fec5137e1d85a7bfd1e8ee5d325653127.jpg')
    update.message.reply_text(
        "Спортивный объект предназначен исключительно для керлинга. Как и «Шайбу», его планировали перевозить. "
        "Впоследствии приняли решение о перевозке оборудования в Москву, само здание оставили на месте. В 2015 "
        "году здесь состоялся чемпионат мира по керлингу среди смешанных пар и ветеранов, а также прошел чемпионат "
        "России. После Олимпиады канал ТНТ здесь проводил съемки передачи Comedy Club. На сегодняшний день в центре "
        "проходят тренировки спортсменов и различные представления на льду."
    )


def Ice_Palace_Iceberg(update, context):
    context.bot.send_photo(
        update.message.chat_id,
        'https://api.parkseason.ru/images/4e/a6/54cadcff3bd421348bd8eead0352de505a7bfcf473f9b257744869.jpg')
    update.message.reply_text(
        "После триумфа российских фигуристов и шорт-трекеров на Олимпиаде, «Айсберг» стал главным символом Олимпиады "
        "для"
        " страны. Теперь здесь занимаются ученики школы фигурного катания Максима Транькова и Татьяны Волосожар. Также "
        "проводится международный хоккейный турнир «Кубок Черного Моря» среди молодежных сборных."
    )


def amusements_objects(update, context):
    reply_keyboard = [['/Olympic_embankment', '/Olympic_park'],
                      ['/Sochi_Park', '/back']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text(
        "О каком объекте вы хотели бы узнать поподробнее?",
        reply_markup=markup
    )


def Olympic_embankment(update, context):
    context.bot.send_photo(
        update.message.chat_id,
        'https://sochiguidebook.ru/wp-content/uploads/2017/02/olimpijskij-park-otel-vozle-morya.jpg')
    update.message.reply_text(
        "Набережная была построена в преддверии зимних олимпийских игр 2014, и безусловно, стала одной из "
        "достопримечательностей постолимпийского региона. Протяженность набережной равняется 7 километрам, "
        "а расположена она в адлерском районе городе Сочи, в имерегинской низменности, еще набережную называют"
        " «нижнеимеретинская», по месту расположения оной. Прогуливаясь по набережной, можно увидеть и Олимпийскую "
        "деревню, и разнообразные ледовые дворцы, находящиеся в Олимпийском парке"
    )


def Olympic_park(update, context):
    context.bot.send_photo(
        update.message.chat_id,
        'https://rider-skill.ru/wp-content/uploads/2019/01/olimpijskij-park-2.jpg')
    update.message.reply_text(
        "Новая достопримечательность Сочи – Олимпийский парк, работает каждый день с утра до позднего вечера, вход "
        "свободный. Кроме дворцов, построенных к зимней Олимпиаде, на огромной территории есть парк аттракционов, "
        "музеи, отель-замок, светомузыкальный фонтан."
    )


def Sochi_Park(update, context):
    context.bot.send_photo(
        update.message.chat_id,
        'https://bogatyr-castle.ru/local/pictures/text/xhead.jpg.pagespeed.ic.T3az25NBGI.jpg')
    update.message.reply_text(
        "Сочи Парк — первый тематический парк страны и один из наиболее мощных магнитов, притягивающих в Сочи туристов "
        "со всего мира. На протяжении шести лет он подтверждает звание лучшего в стране и СНГ открытого "
        "развлекательного парка с количеством посетителей свыше миллиона человек в год, а в 2016 году вошел в топ-25"
        " лучших парков Европы. На площади более 25 гектаров расположены аттракционы для всей семьи, многим из которых"
        " нет аналогов в России, а также отель-замок «Богатырь». Среди самых популярных аттракционов: экстремальные "
        "горки «Змей Горыныч» и «Квантовый скачок», а также самая высокая в стране башня свободного падения "
        "«Жар-птица»."
    )


def education_objects(update, context):
    reply_keyboard = [['/Park_of_Science_and_Art_Sirius', 'Lyceum_Sirius'],
                      ['/Educational_center_Sirius', '/back']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text(
        "О каком объекте вы хотели бы узнать поподробнее?",
        reply_markup=markup
    )


def Park_of_Science_and_Art_Sirius(update, context):
    context.bot.send_photo(
        update.message.chat_id,
        'https://reinfo-sochi.ru/media/zoo/images/1.'
        'Park_Sirius_1_ec0ef7998582b6f27462b0797d1a418a.jpg')
    update.message.reply_text(
        "Парк науки и искусства «Сириус» создан Фондом «Талант и успех» на базе олимпийской инфраструктуры – здания "
        "бывшего Главного медиацентра Олимпиады 2014 года."
        "Парк соединил в себе научные инновации и традиции мирового искусства. Здесь располагаются лаборатории для "
        "проектной и научно-исследовательской работы, мастерские, экспозиции и выставочные залы, учебные аудитории и "
        "классы, в которых работают ученики Центра, проходят фестивали науки и творчества, концерты классической музыки "
        "и балета, художественные выставки."
    )


def Lyceum_Sirius(update, context):
    context.bot.send_photo(
        update.message.chat_id,
        'https://cdn.discordapp.com/attachments/640978722618474546/835619454024024074/'
        '40801e1eddd1b10a41d3cda70a15f04c.png')
    update.message.reply_text(
        "Лицей объединяет крепкое классическое образование и новейшие образовательные технологии. Особенности обучения "
        "— индивидуальный учебный план и свободный выбор образовательной траектории. Занятия проходят в современных "
        "классах и лабораториях Центра «Сириус», Парка науки и искусства, на спортивных объектах Олимпийского парка."
    )


def Educational_center_Sirius(update, context):
    context.bot.send_photo(
        update.message.chat_id,
        'https://eng.spdm.ru/sites/default/files/halls/talant_i_uspekh_zdanie.png.jpeg')
    update.message.reply_text(
        "Образовательный центр «Сириус» в городе Сочи создан Образовательным Фондом «Талант и успех» на базе "
        "олимпийской инфраструктуры по инициативе Президента Российской Федерации В.В. Путина. Фонд учрежден "
        "24 декабря 2014 г. выдающимися российскими деятелями науки, спорта и искусства."
    )


def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("back", back))
    dp.add_handler(CommandHandler("sport_objects", sport_objects))
    dp.add_handler(CommandHandler("amusements_objects", amusements_objects))
    dp.add_handler(CommandHandler("education_objects", education_objects))
    dp.add_handler(CommandHandler("Fisht_stadium", Fisht_stadium))
    dp.add_handler(CommandHandler("Formula_1_track", Formula_1_track))
    dp.add_handler(CommandHandler("Speed_skating_center_Adler_Arena", Speed_skating_center_Adler_Arena))
    dp.add_handler(CommandHandler("Ice_Palace_Bolshoi", Ice_Palace_Bolshoi))
    dp.add_handler(CommandHandler("Ice_arena_Puck", Ice_arena_Puck))
    dp.add_handler(CommandHandler("Curling_Center_Ice_Cube", Curling_Center_Ice_Cube))
    dp.add_handler(CommandHandler("Ice_Palace_Iceberg", Ice_Palace_Iceberg))
    dp.add_handler(CommandHandler("Olympic_embankment", Olympic_embankment))
    dp.add_handler(CommandHandler("Olympic_park", Olympic_park))
    dp.add_handler(CommandHandler("Sochi_Park", Sochi_Park))
    dp.add_handler(CommandHandler("Park_of_Science_and_Art_Sirius", Park_of_Science_and_Art_Sirius))
    dp.add_handler(CommandHandler("Lyceum_Sirius", Lyceum_Sirius))
    dp.add_handler(CommandHandler("Educational_center_Sirius", Educational_center_Sirius))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print('start')
    main()
