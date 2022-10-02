import random
import time

import PySimpleGUI as sg


class App:
    def __init__(self):
        sg.theme('DarkTeal12')  # Add a touch of color
        self.window = sg.Window('Rock, Paper, Scissors', self.layout(), element_justification='center',icon='res/Rock-Paper-Scissors_icon.ico')

    @staticmethod
    def layout():
        # All the stuff inside your window.
        layout = [
            [sg.Button(image_filename='res/small/rock.png', pad=10, key='rock', button_color='#005691', border_width=2),
             sg.Button(image_filename='res/small/paper.png', pad=10, key='paper', button_color='#005691',
                       border_width=2),
             sg.Button(image_filename='res/small/scissors.png', pad=10, key='scissors', button_color='#005691',
                       border_width=2)],
            [sg.Image(size=(297, 297), key='big_img')],
            [sg.Text(key='result', font=('Arial', 20))]
        ]
        return layout

    def rps(self, option):
        self.window['result'].update('')
        variants = ['rock', 'paper', 'scissors']
        result = random.choice(variants)

        for x in range(5):
            for opt in range(3):
                self.window['big_img'].update(filename='res/big/{}.png'.format(variants[opt]))
                self.window.finalize()
                time.sleep(.08)
        self.window['big_img'].update(filename='res/big/{}.png'.format(result))

        if option == result:
            msg = 'Tie, you both select same', 'black'
        elif option == 'rock' and result == 'paper':
            msg = 'You loose, computer select paper.', 'red'
        elif option == 'rock' and result == 'scissors':
            msg = 'You win, computer select scissors.', 'limegreen'
        elif option == 'paper' and result == 'scissors':
            msg = 'You loose, computer select scissors.', 'red'
        elif option == 'paper' and result == 'rock':
            msg = 'You win, computer select rock.', 'limegreen'
        elif option == 'scissors' and result == 'rock':
            msg = 'You loose, computer select rock.', 'red'
        elif option == 'scissors' and result == 'paper':
            msg = 'You win, computer select paper.', 'limegreen'
        else:
            msg = 'Invalid: choose any one -- rock, paper, scissors.'

        self.window['result'].update(msg[0], text_color=msg[1])

    def run(self):
        # Event Loop to process "events" and get the "values" of the inputs
        while True:
            event, values = self.window.read()
            # msg = event, values)
            if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
                break
            if event == 'rock' or event == 'paper' or event == 'scissors':
                self.rps(event)
        self.window.close()


if __name__ == '__main__':
    app = App()
    app.run()
