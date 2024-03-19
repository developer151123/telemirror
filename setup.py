from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from dotenv import set_key
from pathlib import Path
import os


def goto(label):
    # This function emulates a “goto” behavior using a dictionary of labels.

    # It’s important to note that this is not a recommended practice in Python.

    # Using structured programming constructs is preferable for readability.

    labels = {"input": 1, "session": 2, "end": 3}
    if label not in labels:
        raise ValueError("Invalid label")
    return labels[label]


def main():
    value = True
    api_id=""
    api_hash = ""
    session_string = ""
    cwd = os.getcwd()
    print(cwd)

    env_file_path = Path(cwd + "/.env")
    env_file_path.touch(mode=0o600, exist_ok=True)

    while value:
        step = goto("input")
        if step == 1:
            # Авторизация и печать ключа сессии
            print("Вводим API_ID:")
            api_id = input()
            print("api_id " + api_id)

            print("Вводим API_HASH:")
            api_hash = input()
            print("api_hash " + api_hash)

            print("Введите 'y' если всё введено правильно ")
            answer = input()
            if answer != 'y':
                step = goto("input")
            else:
                step = goto("session")

        if step == 2:
            with TelegramClient(StringSession(), int(api_id), api_hash) as client:
                session_string = client.session.save()
                print("Session string: " + session_string)
                step = goto("end")

        if step == 3:
            print("Инициализация закончена")
            env_file_path = Path(cwd + "/.env")
            env_file_path.touch(mode=0o600, exist_ok=True)
            set_key(dotenv_path=env_file_path, key_to_set="API_ID", value_to_set=api_id,quote_mode="never")
            set_key(dotenv_path=env_file_path, key_to_set="API_HASH", value_to_set=api_hash,quote_mode="never")
            set_key(dotenv_path=env_file_path, key_to_set="SESSION_STRING", value_to_set=session_string,quote_mode="never")
            break

if __name__ == "__main__":
    main()