from flask_restful import Resource

samples = [
    {
        "id":1,
        "time-stamp":'March 22, 2020, 8:20 p.m.',
        "resistance":100,
        "frequency":100,
        "label":-1
    },
    {
        "id":2,
        "time-stamp":'March 22, 2020, 8:30 p.m.',
        "resistance":100,
        "frequency":400,
        "label":-1
    },
    {
        "id":3,
        "time-stamp":'March 22, 2020, 8:40 p.m.',
        "resistance":100,
        "frequency":300,
        "label":-1
    },
    {
        "id":4,
        "time-stamp":'March 22, 2020, 8:50 p.m.',
        "resistance":100,
        "frequency":200,
        "label":-1
    }
]


class Sample(Resource):
  def get(self, id):
    for sample in samples:
      if(id == sample["id"]):
        return sample, 200
    return "Item not found for the id: {}".format(id), 404
