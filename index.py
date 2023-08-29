from flask import Flask, render_template
# from flask_migrate import Migrate

from routers.routes import task
app = Flask(__name__)
app.config.from_object('config')

# migrate = Migrate(app, db)
app.register_blueprint(task, url_prefix='/users')

@app.route('/hello_world')
def index():
    return "hello world"
    # return render_template('index.html')
if __name__ == '__main__':
    app.debug = True
    app.run()