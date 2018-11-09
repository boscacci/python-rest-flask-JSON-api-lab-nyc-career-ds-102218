import pdb
# import Flask, render_template, jsonify
from flask import Flask, render_template, jsonify
# import Pictures
from pictures_data import Pictures
# create Flask app
app = Flask(__name__)
# --- API Routes ---
@app.route('/api/pictures')
def api_pictures():
    return jsonify(Pictures)

@app.route('/api/pictures/<int:id>')
def api_picture_id(id):
    return jsonify(Pictures[id-1])

@app.route('/api/pictures/<country>')
def api_picture_country(country):
    country_list = [pic for pic in Pictures if pic['country'].lower() == country]
    return jsonify(country_list)

# --- HTML Routes ---

@app.route('/pictures')
def pictures():
    html = ''
    for pic in Pictures:
        html += '<img src = %s width = 300px> </img>' % pic['picture_url']
    return html

@app.route('/pictures/<int:id>')
def picture_id(id):
    html = ''
    html += '<img src = %s width = 800px> </img>' % Pictures[id-1]['picture_url']
    return html

@app.route('/pictures/<country>')
def picture_country(country):
    country_list = [pic for pic in Pictures if pic['country'].lower() == country]
    html = ''
    for country in country_list:
        html += '<img src = %s width = 500px></img>' % country['picture_url']
    return html


# run our Flask app
if __name__ == '__main__':
    app.debug = True
    app.run()