from main import bot, dp , anti_flood
from aiogram.types import Message, CallbackQuery
from keyboards.keyboard import *
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from datas.data import data_questions
from states.state import Game_state
import random


players = {}
last_question = {}
id_m = {}
id_h = {}
id_h_button = {}
id_m_button = {}

def get_question(data_questions, step=0):
    kb = InlineKeyboardMarkup(row_width=2)
    data = data_questions[step]
    keyboard_answers_button = [InlineKeyboardButton(text=i, callback_data=i) for i in data['answers']]
    return data['questions'], kb.add(*keyboard_answers_button), data['true_answer'], data['sum']

def true_answer(data: list, step=0):
    return data[step]['true_answer']

def check_user(user, score):
    for i in list(players):
        if i == user and score != None:
            players[user] = players[user] + int(score)
            return players[user]
    players[user] = 0
    return players[user]

def get_question_help_pb(text):
    kb = InlineKeyboardMarkup(row_width=1)
    return kb.add(InlineKeyboardButton(text=text, callback_data=text))

def get_question_help_50(data):
    kb = InlineKeyboardMarkup(row_width=2)
    return kb.add(*[InlineKeyboardButton(text=i, callback_data=i) for i in data])

@dp.message_handler(commands=['start'])
async def menu_command(m: Message):
    text = 'Игра - кто хочет стать миллионером!'
    msg_massage = await bot.send_message(m.from_user.id, text, reply_markup=kb_menu)
    id_m[m.from_user.id] = msg_massage.message_id

@dp.message_handler(text='Старт')
async def menu_command(m: Message):
    await bot.delete_message(chat_id=m.from_user.id, message_id=m.message_id)
    if m.from_user.id in id_m: 
        # print(f'm {id_m[m.from_user.id]}')
        await bot.delete_message(chat_id=m.from_user.id, message_id=id_m[m.from_user.id])
        del id_m[m.from_user.id]
    text = 'Игра - кто хочет стать миллионером!'
    msg_massage = await bot.send_message(m.from_user.id, text, reply_markup=kb_menu)
    id_m[m.from_user.id] = msg_massage.message_id

@dp.callback_query_handler(text='Старт', state=None)
async def games(m:CallbackQuery):
    score = check_user(m.from_user.id, None)
    question = get_question(data_questions, step=0)
    await bot.delete_message(chat_id=m.from_user.id, message_id=m.message.message_id)
    msg_help = await m.message.answer(text="Подсказки:", reply_markup=kb_help)
    id_h[m.from_user.id] = msg_help.message_id
    id_h_button[m.from_user.id] = msg_help.reply_markup.inline_keyboard
    # print(id_h_button[m.from_user.id])
    msg_massage = await m.message.answer(text=f"У Вас на счету  {score} руб.\nВопрос на {question[3]} руб:\n{question[0]}", reply_markup=question[1])
    id_m[m.from_user.id] = msg_massage.message_id
    id_m_button[m.from_user.id] = msg_massage.reply_markup.inline_keyboard
    last_question[m.from_user.id] = question
    await Game_state.q1.set()

    
@dp.callback_query_handler(text=true_answer(data_questions, 0), state=Game_state.q1)
async def answer1(m: CallbackQuery):
    question_score = get_question(data_questions, step=0)
    question = get_question(data_questions, step=1)
    score = check_user(m.from_user.id, question_score[3])
    await bot.delete_message(chat_id=m.from_user.id, message_id=m.message.message_id)
    msg_massage = await m.message.answer(text=f"Правильный ответ! Вы набрали {score} руб.\nВопрос на {question[3]} руб.:\n{question[0]}", reply_markup=question[1])
    id_m[m.from_user.id] = msg_massage.message_id
    id_m_button[m.from_user.id] = msg_massage.reply_markup.inline_keyboard
    last_question[m.from_user.id] = question
    await Game_state.next()

@dp.callback_query_handler(text=true_answer(data_questions, 1), state=Game_state.q2)
async def answer2(m: CallbackQuery):
    question_score = get_question(data_questions, step=1)
    question = get_question(data_questions, step=2)
    score = check_user(m.from_user.id, question_score[3])
    await bot.delete_message(chat_id=m.from_user.id, message_id=m.message.message_id)
    msg_massage = await m.message.answer(text=f"Правильный ответ! Вы набрали {score} руб.\nВопрос на {question[3]} руб.:\n{question[0]}", reply_markup=question[1])
    id_m[m.from_user.id] = msg_massage.message_id
    id_m_button[m.from_user.id] = msg_massage.reply_markup.inline_keyboard
    last_question[m.from_user.id] = question
    await Game_state.next()

@dp.callback_query_handler(text=true_answer(data_questions, 2), state=Game_state.q3)
async def answer3(m: CallbackQuery):
    question_score = get_question(data_questions, step=2)
    question = get_question(data_questions, step=3)
    score = check_user(m.from_user.id, question_score[3])
    await bot.delete_message(chat_id=m.from_user.id, message_id=m.message.message_id)
    msg_massage = await m.message.answer(text=f"Правильный ответ! Вы набрали {score} руб.\nВопрос на {question[3]} руб.:\n{question[0]}", reply_markup=question[1])
    id_m[m.from_user.id] = msg_massage.message_id
    id_m_button[m.from_user.id] = msg_massage.reply_markup.inline_keyboard
    last_question[m.from_user.id] = question
    await Game_state.next()

@dp.callback_query_handler(text=true_answer(data_questions, 3), state=Game_state.q4)
async def answer4(m: CallbackQuery):
    question_score = get_question(data_questions, step=3)
    question = get_question(data_questions, step=4)
    score = check_user(m.from_user.id, question_score[3])
    await bot.delete_message(chat_id=m.from_user.id, message_id=m.message.message_id)
    msg_massage = await m.message.answer(text=f"Правильный ответ! Вы набрали {score} руб.\nВопрос на {question[3]} руб.:\n{question[0]}", reply_markup=question[1])
    id_m[m.from_user.id] = msg_massage.message_id
    id_m_button[m.from_user.id] = msg_massage.reply_markup.inline_keyboard
    last_question[m.from_user.id] = question
    await Game_state.next()

@dp.callback_query_handler(text=true_answer(data_questions, 4), state=Game_state.q5)
async def answer5(m: CallbackQuery):
    question_score = get_question(data_questions, step=4)
    question = get_question(data_questions, step=5)
    score = check_user(m.from_user.id, question_score[3])
    await bot.delete_message(chat_id=m.from_user.id, message_id=m.message.message_id)
    msg_massage = await m.message.answer(text=f"Правильный ответ! Вы набрали {score} руб.\nВопрос на {question[3]} руб.:\n{question[0]}", reply_markup=question[1])
    id_m[m.from_user.id] = msg_massage.message_id
    id_m_button[m.from_user.id] = msg_massage.reply_markup.inline_keyboard
    last_question[m.from_user.id] = question
    await Game_state.next()

@dp.callback_query_handler(text=true_answer(data_questions, 5), state=Game_state.q6)
async def answer6(m: CallbackQuery):
    question_score = get_question(data_questions, step=5)
    question = get_question(data_questions, step=6)
    score = check_user(m.from_user.id, question_score[3])
    await bot.delete_message(chat_id=m.from_user.id, message_id=m.message.message_id)
    msg_massage = await m.message.answer(text=f"Правильный ответ! Вы набрали {score} руб.\nВопрос на {question[3]} руб.:\n{question[0]}", reply_markup=question[1])
    id_m[m.from_user.id] = msg_massage.message_id
    id_m_button[m.from_user.id] = msg_massage.reply_markup.inline_keyboard
    last_question[m.from_user.id] = question
    await Game_state.next()

@dp.callback_query_handler(text=true_answer(data_questions, 6), state=Game_state.q7)
async def answer7(m: CallbackQuery):
    question_score = get_question(data_questions, step=6)
    question = get_question(data_questions, step=7)
    score = check_user(m.from_user.id, question_score[3])
    await bot.delete_message(chat_id=m.from_user.id, message_id=m.message.message_id)
    msg_massage = await m.message.answer(text=f"Правильный ответ! Вы набрали {score} руб.\nВопрос на {question[3]} руб.:\n{question[0]}", reply_markup=question[1])
    id_m[m.from_user.id] = msg_massage.message_id
    id_m_button[m.from_user.id] = msg_massage.reply_markup.inline_keyboard
    last_question[m.from_user.id] = question
    await Game_state.next()

@dp.callback_query_handler(text=true_answer(data_questions, 7), state=Game_state.q8)
async def answer8(m: CallbackQuery):
    question_score = get_question(data_questions, step=7)
    question = get_question(data_questions, step=8)
    score = check_user(m.from_user.id, question_score[3])
    await bot.delete_message(chat_id=m.from_user.id, message_id=m.message.message_id)
    msg_massage = await m.message.answer(text=f"Правильный ответ! Вы набрали {score} руб.\nВопрос на {question[3]} руб.:\n{question[0]}", reply_markup=question[1])
    id_m[m.from_user.id] = msg_massage.message_id
    id_m_button[m.from_user.id] = msg_massage.reply_markup.inline_keyboard
    last_question[m.from_user.id] = question
    await Game_state.next()

@dp.callback_query_handler(text=true_answer(data_questions, 8), state=Game_state.q9)
async def answer9(m: CallbackQuery):
    question_score = get_question(data_questions, step=8)
    question = get_question(data_questions, step=9)
    score = check_user(m.from_user.id, question_score[3])
    await bot.delete_message(chat_id=m.from_user.id, message_id=m.message.message_id)
    msg_massage = await m.message.answer(text=f"Правильный ответ! Вы набрали {score} руб.\nВопрос на {question[3]} руб.:\n{question[0]}", reply_markup=question[1])
    id_m[m.from_user.id] = msg_massage.message_id
    id_m_button[m.from_user.id] = msg_massage.reply_markup.inline_keyboard
    last_question[m.from_user.id] = question
    await Game_state.next()

@dp.callback_query_handler(text=true_answer(data_questions, 9), state=Game_state.q10)
async def answer10(m: CallbackQuery):
    question_score = get_question(data_questions, step=9)
    question = get_question(data_questions, step=10)
    score = check_user(m.from_user.id, question_score[3])
    await bot.delete_message(chat_id=m.from_user.id, message_id=m.message.message_id)
    msg_massage = await m.message.answer(text=f"Правильный ответ! Вы набрали {score} руб.\nВопрос на {question[3]} руб.:\n{question[0]}", reply_markup=question[1])
    id_m[m.from_user.id] = msg_massage.message_id
    id_m_button[m.from_user.id] = msg_massage.reply_markup.inline_keyboard
    last_question[m.from_user.id] = question
    await Game_state.next()

@dp.callback_query_handler(text=true_answer(data_questions, 10), state=Game_state.q11)
async def answer11(m: CallbackQuery, state: FSMContext):
    question_score = get_question(data_questions, step=10)
    score = check_user(m.from_user.id, question_score[3])
    await bot.delete_message(chat_id=m.from_user.id, message_id=m.message.message_id)
    if m.from_user.id in id_h: 
        # print(f'h {id_h[m.from_user.id]}')
        await bot.delete_message(chat_id=m.from_user.id, message_id=id_h[m.from_user.id])
        del id_h[m.from_user.id]
    msg_massage = await m.message.answer(text=f'Вы набрали {score} руб. и прошли игру!!!', reply_markup=kb_menu)
    id_m[m.from_user.id] = msg_massage.message_id
    await state.finish()

@dp.callback_query_handler(text='Выход', state='*')
async def return_menu(m:CallbackQuery, state: FSMContext):
    await state.finish()
    if m.from_user.id in id_h: 
        # print(f'h {id_h[m.from_user.id]}')
        await bot.delete_message(chat_id=m.from_user.id, message_id=id_h[m.from_user.id])
        del id_h[m.from_user.id]
    if m.from_user.id in id_m: 
        # print(f'm {id_m[m.from_user.id]}')
        await bot.delete_message(chat_id=m.from_user.id, message_id=id_m[m.from_user.id])
        del id_m[m.from_user.id]

@dp.message_handler(text='Выход')
async def menu_command(m: Message):
    await bot.delete_message(chat_id=m.from_user.id, message_id=m.message_id)
    if m.from_user.id in id_h: 
        # print(f'h {id_h[m.from_user.id]}')
        await bot.delete_message(chat_id=m.from_user.id, message_id=id_h[m.from_user.id])
        del id_h[m.from_user.id]
    if m.from_user.id in id_m: 
        # print(f'm {id_m[m.from_user.id]}')
        await bot.delete_message(chat_id=m.from_user.id, message_id=id_m[m.from_user.id])
        del id_m[m.from_user.id]

@dp.message_handler(text='Выход', state='*')
async def menu_command(m: Message, state: FSMContext):
    await bot.delete_message(chat_id=m.from_user.id, message_id=m.message_id)
    await state.finish()
    if m.from_user.id in id_h: 
        # print(f'h {id_h[m.from_user.id]}')
        await bot.delete_message(chat_id=m.from_user.id, message_id=id_h[m.from_user.id])
        del id_h[m.from_user.id]
    if m.from_user.id in id_m: 
        # print(f'm {id_m[m.from_user.id]}')
        await bot.delete_message(chat_id=m.from_user.id, message_id=id_m[m.from_user.id])
        del id_m[m.from_user.id]
    
@dp.callback_query_handler(text='Помощь бота', state='*')
async def help_bot(m: CallbackQuery, state: FSMContext):
    if id_h_button[m.from_user.id][0][1]['text'] == 'Помощь бота':
        msg_help = await bot.edit_message_reply_markup(chat_id = m.from_user.id, message_id = id_h[m.from_user.id],inline_message_id = id_h[m.from_user.id], reply_markup = kb_help_50)
        id_h_button[m.from_user.id] = msg_help.reply_markup.inline_keyboard
    else:
        await bot.edit_message_reply_markup(chat_id = m.from_user.id, message_id = id_h[m.from_user.id],inline_message_id = id_h[m.from_user.id], reply_markup = kb_help_exit)
    # print(last_question[m.from_user.id][2])
    await bot.edit_message_reply_markup(chat_id = m.from_user.id, message_id = id_m[m.from_user.id], inline_message_id = id_m[m.from_user.id], reply_markup = get_question_help_pb(last_question[m.from_user.id][2]))

@dp.callback_query_handler(text='50/50', state='*')
async def help_bot(m: CallbackQuery):
    if id_h_button[m.from_user.id][0][1]['text'] == 'Помощь бота':
        msg_help = await bot.edit_message_reply_markup(chat_id = m.from_user.id, message_id = id_h[m.from_user.id],inline_message_id = id_h[m.from_user.id], reply_markup = kb_help_pb)
        id_h_button[m.from_user.id] = msg_help.reply_markup.inline_keyboard
    else:
        await bot.edit_message_reply_markup(chat_id = m.from_user.id, message_id = id_h[m.from_user.id],inline_message_id = id_h[m.from_user.id], reply_markup = kb_help_exit)
    # print(id_m_button[m.from_user.id])
    button = []
    for i in id_m_button[m.from_user.id]:
        for j in i:
           button.append(j['text'])
    # print(button)
    button.remove(last_question[m.from_user.id][2])
    button.pop(random.randrange(len(button)))
    button.pop(random.randrange(len(button)))
    button.append(last_question[m.from_user.id][2])
    await bot.edit_message_reply_markup(chat_id = m.from_user.id, message_id = id_m[m.from_user.id],inline_message_id = id_m[m.from_user.id], reply_markup = get_question_help_50(button))

@dp.callback_query_handler(state='*')
async def return_menu(m: CallbackQuery, state: FSMContext):
    await bot.delete_message(chat_id=m.from_user.id, message_id=m.message.message_id)
    await state.finish()
    if m.from_user.id in id_h: 
        # print(f'h {id_h[m.from_user.id]}')
        await bot.delete_message(chat_id=m.from_user.id, message_id=id_h[m.from_user.id])
        del id_h[m.from_user.id]
    msg_massage = await m.message.answer(text=f'Вы не отгадали, правильный ответ "{last_question[m.from_user.id][2]}"\nВы набрали {players[m.from_user.id]} очков', reply_markup=kb_menu)
    id_m[m.from_user.id] = msg_massage.message_id