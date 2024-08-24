from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Example coordinates list
coordinates = [
    {'lat': 51.505, 'lon': -0.09, 'number': 1},
    {'lat': 21.515, 'lon': -0.1, 'number': 2},
    {'lat': 31.525, 'lon': -0.12, 'number': 7}
]

# coordinates = [
#     ([51.505, -0.09], 1),
#     ([51.515, -0.1],2),
#     ([51.525, -0.12],6)
# ]
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/coordinates')
def get_coordinates():
    return jsonify(coordinates)

if __name__ == '__main__':
    app.run(debug=True)