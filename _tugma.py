from aiogram.types import InlineKeyboardMarkup , InlineKeyboardButton

mainMenu = InlineKeyboardMarkup(row_width=2)
bolm2 = InlineKeyboardMarkup(row_width=2)
adminMenu = InlineKeyboardMarkup(row_width=2)
btnRandom = InlineKeyboardButton(text="Kuchuklar đ"  , callback_data="btnRandom" )
btnRandom2 = InlineKeyboardButton(text="Mushuklar đâ" , callback_data="btnRandom2")
btnRandom3 = InlineKeyboardButton(text="Ilonlar đ" , callback_data="btnRandom3")
btnRandom4 = InlineKeyboardButton(text="Quyonlar  đ" , callback_data="btnRandom4")
btnRandom5 = InlineKeyboardButton(text="Sichqonlar  đ" , callback_data="btnRandom5")
btnRandom6 = InlineKeyboardButton(text="Qushlar  đĻ" , callback_data="btnRandom6")
statik = InlineKeyboardButton(text="Statistika đ"  , callback_data="stats" )
foydalanuvchilar = InlineKeyboardButton(text="Foydalanuvchilar đĨ" , callback_data="userfayl")
ikkibol = InlineKeyboardButton(text="Boshqa hayvonlar rasmi đĻĢ"  , callback_data="boshqa" )

mainMenu.row(btnRandom, btnRandom2)
mainMenu.row(btnRandom3,btnRandom4)
mainMenu.row(btnRandom5,btnRandom6)
mainMenu.add(ikkibol)
mainMenu.add(statik)



xabar_yuborish = InlineKeyboardButton(text="Xabarlar âī¸"  , callback_data="sendmsg" )
statlar = InlineKeyboardButton(text="Statistika đ"  , callback_data="stats" )
adminMenu.insert(xabar_yuborish)
adminMenu.add(statlar)
adminMenu.add(foydalanuvchilar)


ikkibolm1 = InlineKeyboardButton(text="Otlar đ"  , callback_data="otlar" )
ikkibolm2 = InlineKeyboardButton(text="Pandalar đŧ"  , callback_data="pandalar" )
ikkibolm3 = InlineKeyboardButton(text="Pingvinlar đ§"  , callback_data="pinvgin" )
ikkibolm4 = InlineKeyboardButton(text="Sherlar đĻ "  , callback_data="sherlar" )
ikkibolm5 = InlineKeyboardButton(text="Tovuslar đĻ "  , callback_data="tovus" )
ikkibolm6 = InlineKeyboardButton(text="Tovuqlar đ "  , callback_data="tovuq" )
ikkibolm7 = InlineKeyboardButton(text="Orqaga đ "  , callback_data="ortga" )
bolm2.row(ikkibolm1,ikkibolm2)
bolm2.row(ikkibolm3,ikkibolm4)
bolm2.row(ikkibolm5,ikkibolm6)
bolm2.add(ikkibolm7)


