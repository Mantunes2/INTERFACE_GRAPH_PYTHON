import PySimpleGUI as sg

class file:
    def __init__(self):
        # Layout
        layout = [
            [sg.Text('Hello World'), sg.Input(key='Hello World')],
        ]
        # Declarar janela
        self.janela = sg.Window("jANELA").layout(layout)
    def Iniciar(self):
        while True:
            # Extrair Dados
            self.values = self.janela.Read()
            Hello_World = self.values['Hellow World']
            print(f'Hellow World: {Hellow_World}')
fel = file()
fel.Iniciar()
