from sanic import Blueprint, Sanic, response
from sanic.response import json

PREFECTURES_JSON_PATH = './data/created_json/prefectures.json'
TODAY_TOTAL_JSON_PATH = './data/created_json/today_total.json'

app = Sanic()

apiv1 = Blueprint('apiv1', url_prefix='/api/v1')


@app.route('/')
async def index(request):
    return json({'message': 'Web API to get COVID-19(coronavirus) information of each prefecture in Japan.'})


@apiv1.route('/total')
async def total(request):
    return await response.file(TODAY_TOTAL_JSON_PATH)


@apiv1.route('/prefectures')
async def prefectures(request):
    return await response.file(PREFECTURES_JSON_PATH)



api = Blueprint.group(apiv1)
app.blueprint(api)
