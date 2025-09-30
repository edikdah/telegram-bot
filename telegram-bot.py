importtelebot;b
ot =telebot.TeleBot('8051689493:AAGQB6Ec2DaFYh8JZsosDwvOjTKSoiWcW00');#тут токен бота@bo
t.message_handler(content_types=['text'])#слушаем ботаdef 
get_text(message):   i
f message.text =="Привет": #проверям сообщение от пользователя      
  bot.send_message(message.from_user.id,"Здравствуй, мой дорогойдруг!") #отвечаем пользователю    elif
 message.text =="/help":       bo
t.send_message(message.from_user.id,"напиши: Привет")    else:  
     bot.
send_message(message.from_user.id,"я тебя не понимаю, напиши '/help'")bot.polling(n
one_stop=True,interval=0)# ботпостоянно будет опрашивает сервер
