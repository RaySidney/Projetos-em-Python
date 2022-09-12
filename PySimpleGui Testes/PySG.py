import PySimpleGUI as sg

sg.theme('DarkAmber')

#TAMANHO DA TELA
WIN_W = 30
WIN_H = 60

#menu layout
menu_layout = [
    ['File', ['Save', 'Exit']],
    ['Tools', ['Waiting']],
    ['Help', ['About']]
]

#Elementos da tela
layout = [
    [sg.Menu(menu_layout)],
    [sg.Input('0', size=(int(WIN_W/2), 1), font=('Consolas', 20), key='VISOR'),
    sg.Button('<-', font=('Consolas', 20), key='APAGAR'),
    sg.Button('C', font=('Consolas', 20), key='LIMPAR')],

    [sg.Button('1', font=('Consolas', 20), key='UM'),
    sg.Button('2', font=('Consolas', 20), key='DOIS'),
    sg.Button('3', font=('Consolas', 20), key='TRES'),
    sg.Button('+', font=('Consolas', 20), key='SOMA'),
    sg.Button('-', font=('Consolas', 20), key='SUBT')],
    #ROW3
    [sg.Button('4', font=('Consolas', 20), key='QUATRO'),
     sg.Button('5', font=('Consolas', 20), key='CINCO'),
     sg.Button('6', font=('Consolas', 20), key='SEIS'),
     sg.Button('*', font=('Consolas', 20), key='MULT'),
     sg.Button('/', font=('Consolas', 20), key='DIV')],
    #ROW4
    [sg.Button('7', font=('Consolas', 20), key='SETE'),
     sg.Button('8', font=('Consolas', 20), key='OITO'),
     sg.Button('9', font=('Consolas', 20), key='NOVE'),
     sg.Button('0', font=('Consolas', 20), key='ZERO'),
     sg.Button('=', font=('Consolas', 20), key='IGUAL')],
]
class App():
    def __init__(self):
        self.window = sg.Window('PySg', layout=layout, margins=(0, 0), resizable=True, return_keyboard_events=False)
        self.result = 0
        self.oper = ''
        self.window.read(timeout=1)

        for i in range(1,5):
            for button in layout[i]:
                button.expand(expand_x=True, expand_y=True)

    #função do menu_layout
    def about(self):
        sg.popup('About', 'Criado por Ray Sidney para treinar Python com a livraria PySimpleGui', 'Contact me: raysprs@gmail.com')

    #Função do visor
    def resulter(self):
        if self.oper == '+':
            return float(float(self.result) + float(self.values['VISOR']))

        if self.oper == '-':
            return float(float(self.result) - float(self.values['VISOR']))

        if self.oper == '/':
            return float(float(self.result) / float(self.values['VISOR']))

        if self.oper == '*':
            return float(float(self.result) * float(self.values['VISOR']))

    #RODAR O APP
    def start(self):
        while True:
            event, self.values = self.window.read()
            if event in (None, 'Exit', sg.WIN_CLOSED):
                break
            if event in ('About'):
                self.about()

            if event in ('UM'):
                if self.values['VISOR']== '0':
                    self.window['VISOR'].update(value='1')
                else:
                    self.window['VISOR'].update(value=self.values['VISOR'] + '1')

            if event in ('DOIS'):
                if self.values['VISOR']== '0':
                    self.window['VISOR'].update(value='2')
                else:
                    self.window['VISOR'].update(value=self.values['VISOR'] + '2')

            if event in ('TRES'):
                if self.values['VISOR']== '0':
                    self.window['VISOR'].update(value='3')
                else:
                    self.window['VISOR'].update(value=self.values['VISOR'] + '3')

            if event in ('QUATRO'):
                if self.values['VISOR']== '0':
                    self.window['VISOR'].update(value='4')
                else:
                    self.window['VISOR'].update(value=self.values['VISOR'] + '4')

            if event in ('CINCO'):
                if self.values['VISOR']== '0':
                    self.window['VISOR'].update(value='5')
                else:
                    self.window['VISOR'].update(value=self.values['VISOR'] + '5')

            if event in ('SEIS'):
                if self.values['VISOR']== '0':
                    self.window['VISOR'].update(value='6')
                else:
                    self.window['VISOR'].update(value=self.values['VISOR'] + '6')

            if event in ('SETE'):
                if self.values['VISOR']== '0':
                    self.window['VISOR'].update(value='7')
                else:
                    self.window['VISOR'].update(value=self.values['VISOR'] + '7')

            if event in ('OITO'):
                if self.values['VISOR']== '0':
                    self.window['VISOR'].update(value='8')
                else:
                    self.window['VISOR'].update(value=self.values['VISOR'] + '8')

            if event in ('NOVE'):
                if self.values['VISOR']== '0':
                    self.window['VISOR'].update(value='9')
                else:
                    self.window['VISOR'].update(value=self.values['VISOR'] + '9')

            if event in ('ZERO'):
                if self.values['VISOR']== '0':
                    self.window['VISOR'].update(value='0')
                else:
                    self.window['VISOR'].update(value=self.values['VISOR'] + '0')

            #função especial, apagar e limpar
            if event in ['LIMPAR']:
                self.result = 0
                self.window['VISOR'].update(value=self.result)

            if event in ['APAGAR']:
                self.window['VISOR'].update(value=self.values['VISOR'][:-1])

            #funções +-*/
            if event in ('SOMA'):
                if self.oper != '':
                    self.result = self.resulter()
                else:
                    self.oper = '+'
                    self.result = self.values['VISOR']
                self.window['VISOR'].update(value='')

            if event in ('SUBT'):
                if self.oper != '':
                    self.result = self.resulter()
                else:
                    self.oper = '-'
                    self.result = self.values['VISOR']
                self.window['VISOR'].update(value='')

            if event in ('DIV'):
                if self.oper != '':
                    self.result = self.resulter()
                else:
                    self.oper = '/'
                    self.result = self.values['VISOR']
                self.window['VISOR'].update(value='')

            if event in ('MULT'):
                if self.oper != '':
                    self.result = self.resulter()
                else:
                    self.oper = '*'
                    self.result = self.values['VISOR']
                self.window['VISOR'].update(value='')

            if event in ('IGUAL'):
                self.result = self.resulter()
                self.window['VISOR'].update(value=self.result)
                self.result = 0
                self.oper = ''

App().start()