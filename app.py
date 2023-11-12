import io
import json
import os
from flask import Flask, render_template, request

app = Flask(__name__)




@app.route('/')
def home():
    return render_template('home.html')

@app.route('/welcome.html')
def home():
    return render_template('welcome.html')

@app.route('/index.html')
def index():
    return render_template('index.html')



@app.route('/impact.html')
def impact():
    return render_template('impact.html')




@app.route('/aboutus.html')
def aboutus():
    return render_template('aboutus.html')




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

