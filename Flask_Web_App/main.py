from Website import create_app

app = create_app()

#Runs this only if this file is ran, not imported
if __name__ == '__main__':
    #Reruns web server if any changes are made to code
    app.run(debug=True)
