import os

# 1 - retornar a pasta atual
print(os.getcwd())

# 2 - Listar arquivos e pastas
print(os.listdir())

# 3 - Versão do SO
os.system('ver')

# 4 - Configurações da máquina
os.system('systeminfo')

# 5 - Limpar a tela do terminal
os.system('cls')

# 6 - Desligar computador
os.system('shutdown /s')

# 7 - Cancelar o desligamento
os.system('shutdown /a')

# 8 - Desligar Computador Imediatamente
# os.system('shutdown /s /t /0')

def turn_off_one_hour():
  os.system('shutdown /s /t 3600')

def turn_off_half_an_hour():
  os.system('shutdown /s /t 1800')

def cancel_shutdown():
  os.system('shutdown /a')

