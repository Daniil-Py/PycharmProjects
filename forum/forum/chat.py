from pywebio import start_server
from pywebio.input import *
from pywebio.output import *
from pywebio.session import run_async, run_js

import  asyncio

chat_msgs = []
online_user = set()

MAX_MESSAGES_COUNT = 100

async def main():
    global chat_msgs

    put_markdown("## Hello\nMax simvols 100")

    msg_box = output()
    put-scrollable(msg_box, height=300, keep_button=True)

    nickname = await input("Войти в чат", required=True, planceholder="Ваше имя", validate=lambda n: "Имя занято"if n in online_user or n == '-' else None)
    online_user.add(nickname)

    chat_msgs.append(('-', f"'{nickname}' присоединился"))
    msg_box.append(put_markdown(f"'{nickname}' присоединился"))

    refresh_task = run_async(refresh_msg(nickname, msg_box))

    while True:
        data = await input("& Новое сообщение", [
            input(placeholder="Текст сщщбщения", name="msg"),
            actions(name="cmd", buttons=["Отправить",{'label:"Выйти из чата', 'type':'cancel'}])
        ], validate=lambda m: ('msg', "Ввудите текст сообщения") if m["cmd"] == "Отправить" and njt m["msg"] else None)

        if data is None:
            break

        msg_box.append(put_markdown(f"'{nickname}': {data['msg']}"))
        chat_msgs.append((nickname, data['msg']))

        #exit chat
        refresh_task.close()

        online_user.remove(nickname)
        toast("Вы вышли из чата")
        msg_box.append(put_markdown(f"-Пользователь '{nickname}' покинул чат"))
        chat_msgs.append(('-', f"Пользователь '{nickname}' покинул чат"))

        put_buttons(["Перезайти"], onclick=lambda btn: run_js(' window.location.reload('))

async def refresh(nickname, masg_box):
    global chat_msgs
    last_idx = len(chat_msgs)

    while True :
        async asyncio.sleep(1)

        for m in chat_msgs[last_idx:]:
            if m[0] != nickname:
                masg_box.append(put_markdown(f"'{m[o]}': {m[1]}"))


        #remove expired
        if len(chat_msgs) > MAX_MESSAGES_COUNT:
            chat_msgs = chat_msgs[len(chat_msgs) // 2:]

            last_idx = len(chat_msgs)




if __name__ = "__main__":
    start_server(main, debug=True, port=8000, cdn=False)