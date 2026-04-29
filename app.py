from flask import Flask, render_template, request, redirect

app = Flask(__name__)

carrito = []

@app.route('/')
def index():
    total = sum(item['precio'] * item['cantidad'] for item in carrito)
    return render_template('index.html', carrito=carrito, total=total)

@app.route('/agregar', methods=['POST'])
def agregar():
    producto = request.form['producto']
    precio = float(request.form['precio'])
    cantidad = int(request.form['cantidad'])

    carrito.append({
        'producto': producto,
        'precio': precio,
        'cantidad': cantidad
    })

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)