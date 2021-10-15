"""
Automação de organização  e limpeza da pasta download.

By Carlos Henrique Barros Silva Campos

versão - 1.0
"""

import os
import glob
import shutil
from pathlib import Path
import pyautogui as py

contro = []

py.alert(text='Pronto para começar?', title='Organizador de arquivos', button='OK')

try:
    download = Path.home() / "Downloads"

except:
    pass


def Organizador():
    global controle
    os.chdir(download)
    for arquivo in glob.glob('*.*'):
        format_file = arquivo.split('.')
        formato = format_file[1]
        contro.append(formato)

    controle = set(contro)


def Gerador_de_pasta():
    Organizador()
    for pasta in controle:
        try:
            os.mkdir(f'{download}\\{pasta}')

        except:
            pass


def Mover():
    Gerador_de_pasta()
    os.chdir(download)
    lista = list(controle)
    for file in lista:
        for move in glob.glob(f'*.{file}'):
            id = lista.index(file)
            if file == list(controle)[id]:
                shutil.move(move, f'{download}\\{file}')


def main():
    Mover()


if __name__ == '__main__':
    main()