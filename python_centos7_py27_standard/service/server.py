from flask import Flask
from flask_restful import Resource, Api
import platform
import os

class ApiRoot(Resource):
    def get(self):
      return {'status': 'success', 'info': 'yes!!!', 'service': 'python.centos.py2.7', 'version': platform.python_version(), 'uid': os.getuid()}


if __name__ == "__main__":
  try:
    app = Flask(__name__)
    api = Api(app)
    app.config['DEBUG'] = True
    api.add_resource(ApiRoot, '/')

    app.run(host='0.0.0.0',port=9000,threaded=True,use_reloader=False)
  except KeyboardInterrupt:
    pass
