from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

BOT_TOKEN = "7308900514:AAFNat6E-5ZjfJuViXwKWBAesD-m-7AMdhw"

def start(update: Update, context: CallbackContext):
    message = (
        "မင်္ဂလာပါရှင့် 🌸\n"
        "KZ BOOST Support teams မှ သင့်အတွက် အသင့်ရှိနေပါတယ်။\n"
        "🕒 24hr service\n\n"
        "ဘာများ ကူညီပေးရမလည်းရှင့်\n"
        "အတတ်နိုင်ဆုံး ကြိုးစားပေးမှာပါ 💪\n\n"
        "📦 Order တင်ချင်ပါက /o\n"
        "🔁 Refill ပြန်ဖြည့်ချင်ပါက /r\n\n"
        "သင့်ရဲ့ ဆန္ဒကို ပြောလိုက်ပါ 😊"
    )

    update.message.reply_text(message)

def order(update: Update, context: CallbackContext):
    update.message.reply_text(
        "📦 Order တင်ရန်\n"
        "လိုချင်သော service ကို အသေးစိတ်ပြောပေးပါရှင့် 😊"
    )

def refill(update: Update, context: CallbackContext):
    update.message.reply_text(
        "🔁 Refill ပြန်ဖြည့်ရန်\n"
        "Order ID ကို ပို့ပေးပါရှင့် 🙏"
    )

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("o", order))
    dp.add_handler(CommandHandler("r", refill))

    updater.start_polling()
    updater.idle()

if name == "main":
    main()
