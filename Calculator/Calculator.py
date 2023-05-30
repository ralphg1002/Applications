import PySimpleGUI as sg

def createWindow(theme):
    #Any gui elements under theme will get applied to theme
    sg.theme(theme)
    sg.set_options(font = ('Franklin', 15), button_element_size= (6,3))
    btnSize = (6,3)

    #Layout defines the layout of the window
    layout =[
        [sg.Text(text= 'Output', font= ('Franklin', 25), justification= 'right', expand_x= True, pad= (10, 15), right_click_menu= themeMenu, key = 'text')], #Can use sg.Push() to create an element that takes up as much spaces as possible
        [sg.Button(button_text= 'Clear', expand_x= True), sg.Button(button_text= 'Enter', expand_x= True)],
        [sg.Button(button_text= 7, size= btnSize), sg.Button(button_text= 8, size= btnSize), sg.Button(button_text= 9, size= btnSize), sg.Button(button_text= '*', size= btnSize)],
        [sg.Button(button_text= 4, size= btnSize), sg.Button(button_text= 5, size= btnSize), sg.Button(button_text= 6, size= btnSize), sg.Button(button_text= '/', size= btnSize)],
        [sg.Button(button_text= 1, size= btnSize), sg.Button(button_text= 2, size= btnSize), sg.Button(button_text= 3, size= btnSize), sg.Button(button_text= '-', size= btnSize)],
        [sg.Button(button_text= 0, expand_x= True), sg.Button(button_text= '.', size= btnSize), sg.Button(button_text= '+', size= btnSize)]
    ]

    return sg.Window('Calculator', layout)

#define theme menu and default window theme
themeMenu = ['menu', ['LightGrey1', 'DarkPurple6', 'LightBlue5', 'Darkgrey2', 'Random']]
window = createWindow('DarkBrown7')

currrentNum = []
operation = []

while True:
    event, values = window.read()
    #Close window
    if event == sg.WIN_CLOSED:
        break
    #Theme select
    elif event in themeMenu[1]:
        window.close()
        window = createWindow(event)

    #Buttons for typing numbers
    elif event in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']:
        currrentNum.append(event)
        numString = ''.join(currrentNum)
        window['text'].update(numString)

    #Buttons for selecting the operation
    elif event in ['+', '-', '/', '*']:
        operation.append(''.join(currrentNum))
        currrentNum = []
        operation.append(event)
        window['text'].update('')

    #Enter button
    elif event == 'Enter':
        operation.append(''.join(currrentNum))
        result = eval(''.join(operation))
        window['text'].update(result)
        operation = []

    #Clear button
    elif event == 'Clear':
        currrentNum = []
        operation = []
        window['text'].update('')



window.close()