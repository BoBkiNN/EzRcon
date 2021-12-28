from mcrcon import MCRcon, MCRconException
from socket import gaierror
from config import host,password,port

mcr = MCRcon(host, password, port)
print(f"Подключаюсь к {host}:{port}")

try:
	mcr.connect()
except gaierror:
	print("Сервер не найден.")
	exit()
except ConnectionRefusedError:
	print("Невозможно подключиться к rcon, проверьте правильность порта")
	exit()
except MCRconException:
	print("Неверный пароль")
	exit()

print("Для отключения напишите close")
work = True

while work == True:
	arg = input("Консоль:~/$ ")
	print(f"~/$ {arg}")
	if arg == "close":
		mcr.disconnect()
		work = False
		print("Отключаюсь...")
	else:
		resp = mcr.command(arg)
		print(resp)