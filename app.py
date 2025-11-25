from flask import Flask, jsonify, render_template_string
import random

app = Flask(__name__)

# Datos simulados de la Liga Pro
tabla_posiciones = [
    {"equipo": "Independiente del Valle", "puntos": 35, "pj": 15},
    {"equipo": "Liga de Quito", "puntos": 33, "pj": 15},
    {"equipo": "Barcelona SC", "puntos": 31, "pj": 15},
    {"equipo": "El Nacional", "puntos": 28, "pj": 15},
    {"equipo": "Aucas", "puntos": 25, "pj": 15}
]

# Simulación de IA: Predicción de próximo ganador
def predecir_ganador():
    # Lógica simple: Mayor probabilidad al que tiene más puntos + factor aleatorio
    candidatos = sorted(tabla_posiciones, key=lambda x: x['puntos'], reverse=True)[:3]
    ganador = random.choice(candidatos)
    return ganador['equipo']

@app.route('/')
def home():
    prediccion = predecir_ganador()
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Liga Pro - Tabla y Predicciones</title>
        <style>
            body {{ font-family: Arial, sans-serif; background-color: #f4f4f9; text-align: center; }}
            table {{ margin: 0 auto; border-collapse: collapse; width: 50%; }}
            th, td {{ border: 1px solid #ddd; padding: 8px; }}
            th {{ background-color: #04AA6D; color: white; }}
            .prediccion {{ color: #d9534f; font-weight: bold; font-size: 1.2em; margin-top: 20px; }}
        </style>
    </head>
    <body>
        <h1>Tabla de Posiciones - Liga Pro Ecuador</h1>
        <table>
            <tr><th>Equipo</th><th>Puntos</th><th>PJ</th></tr>
            {''.join([f"<tr><td>{t['equipo']}</td><td>{t['puntos']}</td><td>{t['pj']}</td></tr>" for t in tabla_posiciones])}
        </table>
        <div class="prediccion">
            IA Predicción: El próximo campeón podría ser <strong>{prediccion}</strong>
        </div>
        <p><em>Versión: reyes-1.0.5</em></p>
    </body>
    </html>
    """
    return html

@app.route('/api/tabla')
def api_tabla():
    return jsonify(tabla_posiciones)

if __name__ == '__main__':
    # Puerto 5000 interno (estándar Flask)
    app.run(host='0.0.0.0', port=1001)