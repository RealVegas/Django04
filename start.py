import signal
import subprocess


def run_server():
    # Запускаем сервер Django
    process = subprocess.Popen(['.venv/Scripts/python', 'advanced_news/manage.py', 'runserver'])

    try:
        process.wait()
    except KeyboardInterrupt:
        print("Завершение работы сервера...")
        process.send_signal(signal.SIGINT)  # Отправляем сигнал завершения процессу
        process.wait()  # Ожидаем завершения процесса
    finally:
        print("Сервер остановлен.")


if __name__ == '__main__':
    run_server()