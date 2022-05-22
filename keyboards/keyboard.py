from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

menu = ['Старт', 'Выход']
kb_menu = InlineKeyboardMarkup(row_width=1)
kb_menu.add(*[InlineKeyboardButton(i, callback_data=i) for i in menu])

help_list = ['50/50','Помощь бота','Выход']
kb_help = InlineKeyboardMarkup(row_width=3)
kb_help.add(*[InlineKeyboardButton(i, callback_data=i) for i in help_list])

help_list_50 = ['50/50','Выход']
kb_help_50 = InlineKeyboardMarkup(row_width=2)
kb_help_50.add(*[InlineKeyboardButton(i, callback_data=i) for i in help_list_50])

help_list_pb = ['Помощь бота','Выход']
kb_help_pb = InlineKeyboardMarkup(row_width=2)
kb_help_pb.add(*[InlineKeyboardButton(i, callback_data=i) for i in help_list_pb])

kb_help_exit = InlineKeyboardMarkup(row_width=1)
kb_help_exit.add(InlineKeyboardButton('Выход', callback_data='Выход'))