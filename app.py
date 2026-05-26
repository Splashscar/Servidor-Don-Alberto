from flask import Flask, jsonify, request
import datetime

app = Flask(__name__)

peritajes = []

@app.route('/api/registros', methods=['GET'])
def registros():
	return jsonify({
	  "status": "SERVIDOR PRINCIPAL",
	  "servidor": "Ubuntu de Mendieta:",
	  "hora_servidor": str(datetime.datetime.now()),
	  "inventario": ["Buhias de Iridio", "Refrigerannte","Transistores","Filtro de aceite", "Aceite motul 7100"]
	})

@app.route('/api/peritajes', methods=['POST'])
def guardar_peritajes():
	data= request.json
	placa=data.get("placa").upper()
	peritajes.append(placa)

	return jsonify({
		"mensajes": "Peritaje registrado",
		"placa": placa
	})

@app.route('/api/peritajes', methods=['GET'])
def ver_peritajes():

	return jsonify({
		"peritajes": peritajes
	})

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000, debug=True)


