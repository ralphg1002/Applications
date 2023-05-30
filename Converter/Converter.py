import PySimpleGUI as sg

#Layout defines the layout of the window
layout = [
    [sg.Button(button_text= 'Convert', key= 'Convert Button'), sg.Spin(values= ['lbs to kgs', 'miles to kms', 'secs to mins'], key= 'Units',size= 20)],
    [sg.Input(key= 'Input')],
    [sg.Text(text= '', background_color= 'sandy brown', enable_events= True, key= 'Output Text')]
]

#Create window
window = sg.Window(title= 'Converter', layout= layout, background_color= 'sandy brown')

while True:
    event, values = window.read()
    #Close the window if close button is pressed on window
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Convert Button':
        #Access window like dictionary to update value of Text
        inputVal = values['Input']
        #Error check for user input
        if inputVal.isnumeric():
            match values['Units']:
                case 'lbs to kgs':
                    output = round(float(inputVal) * 0.4536, 3)
                    outputString = f'{inputVal} lbs are {output} kgs.'
                case 'miles to kms':
                    output = round(float(inputVal) * 1.609, 3)
                    outputString = f'{inputVal} kms are {output} miles.'
                case 'secs to mins':
                    output = round(float(inputVal) / 60, 3)
                    outputString = f'{inputVal} seconds are {output} minutes.'
            #Update output text accoirdingly
            window['Output Text'].update(outputString)
        else:
            #Update output text accoirdingly
            window['Output Text'].update('Please Enter a Number.')
                    
            

window.close()