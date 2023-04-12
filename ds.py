from pypresence import Presence

RPC = Presence("11111111111111111") #CLIENT_ID

btns = [{
         "label" : "TEXT" , #ТЕКСТ КНОПКИ
         "url" : "TEXT" #ССЫЛКА КНОПКИ
        },
        
        {
         "label" : "TEXT", #ТЕКСТ КНОПКИ
         "url" : "TEXT" #ССЫЛКА КНОПКИ
        }
]

RPC.connect()
RPC.update(
    details='TEXT', #ОПИСАНИЕ
    buttons=btns,
    large_image='TEXT', #НАЗВАНИЕ ОСНОВНОГО ИЗОБРАЖЕНИЯ С САЙТА
    small_image='TEXTTEXT', #НАЗВАНИЕ МАЛЕНЬКОГО ИЗОБРАЖЕНИЯ С САЙТА
    large_text='TEXT', #ПРИ НАВЕДЕНИИ НА ОСНОВНОЕ ИЗОБРАЖЕНИЕ БУДЕТ ВЫВОДИТЬСЯ ДАННЫЙ ТЕКСТ
    small_text='TEXT' #ПРИ НАВЕДЕНИИ НА МАЛЕНЬКОЕ ИЗОБРАЖЕНИЕ БУДЕТ ВЫВОДИТЬСЯ ДАННЫЙ ТЕКСТ
)

input()
