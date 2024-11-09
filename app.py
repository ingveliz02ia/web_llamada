from flask import Flask, request, render_template, redirect, url_for,flash 
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
    full_name = request.form['full_name']
    phone_number = request.form['phone_number']

    # Configura la URL del webhook de tu escenario de Make
    webhook_url = 'https://hook.eu2.make.com/dbxyau9e7ho5113994doa2acutm4n3be'

    # Datos a enviar al webhook
    data = {
        'full_name': full_name,
        'phone_number': phone_number
    }

    # Enviar datos al webhook usando una solicitud POST
    response = requests.post(webhook_url, json=data)
    if response.status_code == 200:
        flash ('¡Mensaje enviado con éxito!', 'success')
    else:
        flash ('Error al enviar los datos', 'error')
    
    return redirect(url_for('form'))
    
if __name__ == '__main__':
    #app.run(debug=True)
    serve(app, host='0.0.0.0', port=80)
