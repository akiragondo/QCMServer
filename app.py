from flask import Flask
from flask_restful import Api

from Resources.sample import Sample

app = Flask(__name__)
api = Api(app)

api.add_resource(Sample, "/sample/<int:id>")

if __name__ == "__main__":
  app.run()
