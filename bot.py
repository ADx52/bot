from flask import Flask
from flask import request
from requests import get
import os


token = os.environ['TOKEN']
url = f'https://api.telegram.org/bot{token}/'


otakBot = Flask(__name__)

def update(update):
  if 'new_chat_member' in str(update):
     nama_grup = update['message']['chat']['title']
     grup_id   = update['message']['chat']['id']
     mem_baru  = update['message']['new_chat_member']['first_name']
     teks      = f'Hai {mem_baru} !\nSelamat datang di Grup {nama_grup}'
     kirim_pesan(grup_id,teks)
  else:
     # disini bisa kita tambahin kode lainnya
     # misalnya membalas kalau ada oran yang ngechat ke bot kita 
     # dan kreasikan sesuai imajinasi kalian :)
     id = update['message']['chat']['id']
     kirim_pesan(id,'halo, Ada yang bisa saya bantu😊')
  
def kirim_pesan(id,teks):
  data = {
  'chat_id':id,
  'text':teks
  }
  get(url+'sendMessage',params=data)


@otakBot.route('/',methods=['POST','GET'])
def index():
  if request.method == 'POST':
     data_update = request.get_json()
     update(data_update)
     return "oke"
  else:
     return 'HALAMAN BOT PERTAMA SAYAHALAMAN INI BISA DI GANTI DENGAN KODE HTML'

if __name__ == '__main__':
  otakBot.run(host='0.0.0.0',port=int(os.environ.get('PORT','5000')),debug=True)
