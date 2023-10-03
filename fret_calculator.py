from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    distances = []
    unit = 'metric'
    if request.method == 'POST':
        scale_length = float(request.form['scale_length'])
        unit = request.form.get('unit', 'metric')
        frets = int(request.form['frets'])
        distances = calculate_fret_distances(scale_length, frets)
        
        # Convert to inches if the selected unit is imperial
        if unit == 'imperial':
            distances = [round(d * 0.393701, 2) for d in distances]  # Convert cm to inches

    return render_template('index.html', distances=distances, unit=unit)

def calculate_fret_distances(scale_length, frets):
    distances = []
    for i in range(1, frets + 1):
        distance = scale_length - (scale_length / (2 ** (i / 12.0)))
        distances.append(round(distance, 2))
    return distances

if __name__ == '__main__':
    app.run(debug=True)
