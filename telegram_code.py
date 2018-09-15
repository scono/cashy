import telepot
from datetime import date

bot     = telepot.Bot('++++++ hier id einfügen ++++++')
chat_id = ('++++++ chat id einfügen ++++++')

def send_result(q_str, answer_tuples, a_ans):
    text    = '<i>' + q_str + '</i>\n\n'

    if a_ans == '':
        text    += '<b>Keine Antwort</b>\n\n'

    for ans in answer_tuples:
        if ans[0] == a_ans:
            text += '<b>->' + str(ans[1]) + '</b>\n'
        else:  
            text += str(ans[1]) + '\n'

    for chat in chat_id:
        bot.sendMessage(chat, text, parse_mode='HTML')

def send_hello():
    text =  '-------------------------\n'
    text += ' CASHSHOW am ' + str(date.today()) + '\n'
    text += '-------------------------\n'
    
    for chat in chat_id:
        bot.sendMessage(chat, text, parse_mode='HTML')


    
#path = r'C:\Users\Gottkönig\\bilder\20180808_210228.png'
#photo = open(path, 'rb')
#bot.sendPhoto(chat_id, photo, caption=None, parse_mode=None, disable_notification=None, reply_to_message_id=None, reply_markup=None)             

if __name__ == "__main__":
    send_hello()