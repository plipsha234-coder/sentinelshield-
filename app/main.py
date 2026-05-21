from flask import flask 
from routes.routes import routes 

app = flask(_name_)

app.register_blueprint(routes)

if_name_=="_main_":
app.run(debug=True)