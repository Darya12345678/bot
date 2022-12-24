base = {}
with open (r'mn.txt', encoding ='utf-8') as f:
      for line in f:
        
         key,val = line.strip().split(':')
         
         base[key] = val.split()
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

print(base)
x = base
async def spravochnik(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    
      
    await update.message.reply_text(f'Список контактов: {x}')


app = ApplicationBuilder().token("5957186193:AAG21JDUYW3P9bJI4XPF_pn7pXOsPpAyHs4").build()

app.add_handler(CommandHandler("hello", spravochnik))

app.run_polling()