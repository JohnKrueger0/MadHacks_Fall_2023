import io
import json
import os
from flask import Flask, render_template, request, jsonify
from io import BytesIO
from PIL import Image
import base64
import superScheduleGenerator as gen

width, height = 300, 200
img = Image.new('RGB', (width, height), color='red')

buffered = BytesIO()
img.save(buffered, format="JPEG")
img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')

img_data = "data:image/jpeg;base64," + img_str

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

# @app.route('/welcome.html')
# def home():
#     return render_template('welcome.html')


@app.route('/index.html')
def index():
    return render_template('index.html', img_data=img_data)



@app.route('/impact.html')
def impact():
    return render_template('impact.html')




@app.route('/aboutus.html')
def aboutus():
    return render_template('aboutus.html')


@app.route('/submit', methods=['POST'])
def submit():
    data = request.json['values']  # Retrieve the values sent from the frontend
    # Now 'data' contains the 12 values you submitted

    # Do whatever processing you need with this data
    print(data)  # Just an example; you might do something more meaningful

    img = gen.sortSchedules(gen.getSchedules()).paintSchedule()

    # Convert the PIL image to a base64 encoded string
    buffered = BytesIO()
    img.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')

    img_data = "data:image/jpeg;base64," + img_str
    
    #return 'PEEEEEEENIS'#render_template('index.html', img_data=img)
    #
    # return render_template('index.html', img_data=img_data)
    return jsonify({"img_data": img_data})

    #return 'Data received on the backend!'  # Sending a response back to the frontend

@app.route('/check_image', methods=['GET'])
def check_image():
    # Perform any checks here and return the current image URL
    # Replace this with your logic to determine the image URL
    #image_url = "https://via.placeholder.com/150"  # Placeholder URL for the generated image

    return jsonify({"img_data": img_data})

# def order_projects_by_weight(projects):
#     try:
#         return int(projects['weight'])
#     except KeyError:
#         return 0


# @app.route('/projects/<title>')
# def project(title):
#     projects = get_static_json("static/projects/projects.json")['projects']
#     experiences = get_static_json("static/experiences/experiences.json")['experiences']

#     in_project = next((p for p in projects if p['link'] == title), None)
#     in_exp = next((p for p in experiences if p['link'] == title), None)

#     if in_project is None and in_exp is None:
#         return render_template('404.html'), 404
#     elif in_project is not None and in_exp is not None:
#         selected = in_exp
#     elif in_project is not None:
#         selected = in_project
#     else:
#         selected = in_exp

#     # load html if the json file doesn't contain a description
#     if 'description' not in selected:
#         path = "experiences" if in_exp is not None else "projects"
#         selected['description'] = io.open(get_static_file(
#             'static/%s/%s/%s.html' % (path, selected['link'], selected['link'])), "r", encoding="utf-8").read()
#     return render_template('project.html', common=common, project=selected)


# @app.errorhandler(404)
# def page_not_found(e):
#     return render_template('404.html'), 404


# def get_static_file(path):
#     site_root = os.path.realpath(os.path.dirname(__file__))
#     return os.path.join(site_root, path)


# def get_static_json(path):
#     return json.load(open(get_static_file(path)))


if __name__ == "__main__":
    print("running py app")
    app.run(host="127.0.0.1", port=5000, debug=True)

