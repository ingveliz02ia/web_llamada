from flask import Flask, request, render_template, redirect, url_for, flash
import requests
from waitress import serve

app = Flask(__name__)
app.secret_key = '4f3c2e1d9a8c7b6a5e4d3c2b1f0a9e8c7b6a5e4d3c2b1f0a9e8c7d6a5f4c3e2'

# Ruta para mostrar el formulario
@app.route('/')
def form():
    print("cargando la pagina")
    return render_template('form.html')

# Ruta para procesar el formulario y enviar datos al webhook
@app.route('/submit', methods=['POST'])
def submit():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email_name']
    phone_number = request.form['phone_number']

    # Configura la URL del webhook de tu escenario de Make
    
    webhook_urlA = 'https://hook.eu2.make.com/166lob9xw6acc3u5y72y31rh3ke1dr9n' #make
    webhook_urlB = 'https://datosiniciales-production.up.railway.app/receive-data' #funciono
    #webhook_urlA = 'https://2c46-209-45-58-245.ngrok-free.app/receive-data'# Quisimos agregarle alservidor no se logro
        

    # Datos a enviar al webhook
    data = {
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'phone_number': phone_number
    }

    # Enviar datos al webhook usando una solicitud POST
    responseA = requests.post(webhook_urlA, json=data)
    responseB = requests.post(webhook_urlB, json=data)

    if responseA.status_code == 200 and responseB.status_code == 200:
        flash('¡Mensaje enviado con éxito!', 'success')
    else:
        flash('Error al enviar los datos', 'error')

    return redirect(url_for('form'))

if __name__ == '__main__':
    app.run(debug=True)
    #serve(app, host='0.0.0.0', port=80)

