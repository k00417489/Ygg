from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Bot token
API_TOKEN = "7897818312:AAFkbO0cqipeSDBPegsgyFqAnSvFPRgb3wg"

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Create keyboard
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(KeyboardButton("ADD FUNDS"), KeyboardButton("BUY INDO IG"))
keyboard.add(KeyboardButton("BUY PREPAID"), KeyboardButton("BUY OLD IG"))
keyboard.add(KeyboardButton("MY BALANCE"), KeyboardButton("📦 STOCK"))
keyboard.add(KeyboardButton("CONTACT"))

@dp.message_handler(commands=["start"])
async def start(msg: types.Message):
    welcome_text = (
        "🔥WELCOME TO OLD IG/INDO IG/\n"
        "PREPAID IG SELLER BOT\n\n"
        "🚨 ANY PROBLEM? CONTACT @SPINNERRXXD\n\n"
        "📢 Join Our Channel @CHANNEL"
    )
    await msg.answer(welcome_text, reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "ADD FUNDS")
async def add_funds(msg: types.Message):
    await msg.answer("To add funds, contact admin @SPINNERRXXD")

@dp.message_handler(lambda message: message.text == "BUY INDO IG")
async def buy_indo(msg: types.Message):
    await msg.answer("Send payment and then Indo IG will be delivered.")

@dp.message_handler(lambda message: message.text == "BUY PREPAID")
async def buy_prepaid(msg: types.Message):
    await msg.answer("Send payment and then prepaid IG will be delivered.")

@dp.message_handler(lambda message: message.text == "BUY OLD IG")
async def buy_old(msg: types.Message):
    await msg.answer("Send payment and then old IG will be delivered.")

@dp.message_handler(lambda message: message.text == "MY BALANCE")
async def my_balance(msg: types.Message):
    await msg.answer("Your balance: ₹0. Please add funds.")

@dp.message_handler(lambda message: message.text == "📦 STOCK")
async def check_stock(msg: types.Message):
    await msg.answer("""Current stock:
- Indo IG: 5
- Prepaid IG: 10
- Old IG: 3""")

@dp.message_handler(lambda message: message.text == "CONTACT")
async def contact_admin(msg: types.Message):
    await msg.answer("Contact Admin: @SPINNERRXXD")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
