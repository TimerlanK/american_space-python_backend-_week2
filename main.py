from fastapi import FastAPI
import requests

app = FastAPI()

# some database data
db_data = {
    'Tim': {
        'age': 29,
        'ocupation': 'aspiring data scientist'
    },
    'Bika': {
        'age': 26,
        'ocupation': 'aspiring data miner'
    },
    'Tomi': {
        'age': 23,
        'ocupation': 'aspiring business lady'
    },
    'Zhanatgul': {
        'age': 52,
        'ocupation': 'doctor'
    }
}

# print(list(db_data.keys()))


class RequestAPI:
    url = 'http://api.quotable.io/random'

    def get_quote(self):
        result = requests.get(self.url).json()

        return result["content"]

    def get_text_with_quote_for_name(self, name):
        if name in list(db_data.keys()):
            return "%s's advice to you is: %s" % (name, self.get_quote())
        else:
            return 'No such family member. Please go to (.../family) for list of people needed inspiration from'


@app.get('/')
def index():
    text = \
    "Hi here is the citemap. 1) Browse (.../family) for list of people needed inspiration 2) Browse (.../family/name_from_family) for more information about family members) 3) Browse (.../inspiration/name_from_family) to get inspiration quote from desired family member"
    return (text)


@app.get('/family')
def names():
    return 'Family members are Tim, Bika, Tomi, Zhanatgul'

@app.get('/family/{name}')
def describe_family(name):
    name = name.lower().capitalize()
    if name not in list(db_data.keys()):
        return 'No such family member. Please go to (.../family) for list of people needed inspiration'
    return db_data[str(name)]


@app.get('/inspiration/{name}')
def get_inspiration(name):
    name = name.lower().capitalize()
    if name not in list(db_data.keys()):
        return 'No such family member. Please go to (.../family) for list of people needed inspiration'
    my_request = RequestAPI()
    return my_request.get_text_with_quote_for_name(name)