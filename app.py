from flask import Flask, render_template, request, jsonify
import utils

app = Flask(__name__, )

@app.route('/')
def home():
    locations = utils.__locations
    return render_template('app.html', locations=locations)

# @app.route('/get_location_names')
# def get_location_names():
#     print(utils.get_location_names())
#     response = jsonify({
#         'locations':utils.get_location_names()
#     })
#     response.headers.add('Access-Control-Allow-Origin', '*')
#
#     return response


@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])


    estimated_price = utils.get_estimated_price(location, total_sqft, bhk, bath)

    result = {
        'price':estimated_price,
        'location': location,
        'bhk':bhk,
        'bath':bath
    }

    return render_template("app.html", locations=utils.__locations, result=result)

if __name__ == '__main__':
    print('Starting Flask server for house price prediction')
    utils.load_saved_artifacts()
    app.run(debug=True)