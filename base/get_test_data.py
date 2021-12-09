import json


class GetTestData:
    @classmethod
    def get_data(cls, filename, data_demo):
        list = []
        with open("./data/%s.json" % filename, encoding="utf-8") as f:
            data = json.load(f).get(data_demo)
            for i in data.values():
                list.append(i)
        return list