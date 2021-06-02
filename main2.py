@bot.message_handler(content_types=['text'])

def checker(message):
    if message.text == message:
        bot.send_message(message.from_user.id, "Chooose the currency you want to convert" + message + "to, than enter needed value", reply_markup=kb_usd())

checker(USD_txt)
checker(EUR_txt)
checker(GBP_txt)
checker(RUB_txt)


def anymsg(message):

    # second step(usd to)
    if message.text == 'usd -> UAH🇺🇦':
        bot.register_next_step_handler(message, usd_uah)
    if message.text == 'usd -> EUR🇪🇺':
        bot.register_next_step_handler(message, usd_eur)
    if message.text == 'usd -> GBP🇬🇧':
        bot.register_next_step_handler(message, usd_gbp)
    if message.text == 'usd -> RUB🇷🇺':
        bot.register_next_step_handler(message, usd_rub)
