# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "fastapi",
#     "uvicorn",
# ]
# ///
import json
from fastapi import FastAPI,Query
from typing import List

json_str = '[{"name":"MyOAS","marks":37},{"name":"Q7x6xni1P2","marks":69},{"name":"Onp6Bo5j","marks":98},{"name":"AzUONTT76","marks":86},{"name":"JkdDoF","marks":49},{"name":"hDDgs","marks":24},{"name":"yZRRrqkIG","marks":73},{"name":"D9","marks":7},{"name":"amBQs8tA","marks":48},{"name":"n8N","marks":93},{"name":"QrP","marks":1},{"name":"Yq","marks":97},{"name":"c","marks":31},{"name":"6J3CjbL","marks":10},{"name":"qbEy1X","marks":81},{"name":"cGboZ","marks":82},{"name":"hVE2YbO7Qs","marks":54},{"name":"xWFmBbJjw","marks":36},{"name":"a3Dbl0","marks":1},{"name":"Ar","marks":89},{"name":"V8ABv3Od2U","marks":56},{"name":"14FJ","marks":72},{"name":"DR6","marks":33},{"name":"57eVM","marks":57},{"name":"46XIUaWtqm","marks":29},{"name":"gXxvy","marks":69},{"name":"8aPk","marks":44},{"name":"opx7eV1pGI","marks":83},{"name":"Tp","marks":91},{"name":"8au2FcXhx","marks":35},{"name":"I889Q","marks":29},{"name":"wRTV5Jd72","marks":74},{"name":"pwhh4bO","marks":32},{"name":"ghTMD1","marks":34},{"name":"TBUuMLUY","marks":87},{"name":"VICP4Gk","marks":41},{"name":"X4bzea4gl","marks":58},{"name":"JRAY","marks":97},{"name":"TCd","marks":67},{"name":"meGypCQZ","marks":27},{"name":"OHO8z3Vb","marks":35},{"name":"J","marks":73},{"name":"gIJx2Ptez","marks":60},{"name":"oItln","marks":42},{"name":"3NRXi","marks":85},{"name":"8P","marks":29},{"name":"kX8","marks":7},{"name":"ga5l","marks":56},{"name":"eN","marks":79},{"name":"9","marks":19},{"name":"fHz","marks":53},{"name":"lc5gH","marks":88},{"name":"9hMKP9M3E","marks":65},{"name":"Gj","marks":77},{"name":"yo4RctXO3F","marks":74},{"name":"uHUjOBt","marks":92},{"name":"2g271GwgP","marks":22},{"name":"gZYwK","marks":31},{"name":"j3PDcXy","marks":10},{"name":"ZXAZ9lZn3r","marks":6},{"name":"vxKjrOoTM","marks":1},{"name":"yHCrwpc1Dd","marks":69},{"name":"DNe","marks":34},{"name":"rp80DCSc","marks":40},{"name":"Jwzs","marks":70},{"name":"f","marks":51},{"name":"u39231SEEo","marks":36},{"name":"nj4SHvn","marks":7},{"name":"C","marks":46},{"name":"dCZoC","marks":53},{"name":"Qo4D6XxL","marks":20},{"name":"RulaOgeu","marks":92},{"name":"9A1AWVdb0","marks":49},{"name":"BfYxf","marks":79},{"name":"8YobzkLJ","marks":28},{"name":"dZiR","marks":6},{"name":"3dx1","marks":15},{"name":"ILpwgJJDC","marks":87},{"name":"0h2VTlZWMC","marks":74},{"name":"MWCLu","marks":45},{"name":"CotO","marks":84},{"name":"7FpoWBva","marks":75},{"name":"B0","marks":78},{"name":"mb","marks":87},{"name":"unxPQmb5","marks":58},{"name":"dAwvsQg0","marks":80},{"name":"taf","marks":92},{"name":"glg","marks":50},{"name":"veImUZ6o","marks":40},{"name":"SCP","marks":82},{"name":"9VhLF","marks":65},{"name":"dR","marks":23},{"name":"F","marks":30},{"name":"HN9HMMek","marks":45},{"name":"6oQ","marks":4},{"name":"7","marks":50},{"name":"1I2wUFLS","marks":41},{"name":"aWhGpOlvc","marks":45},{"name":"LmARG3ssY3","marks":34},{"name":"HF9","marks":86}]'
data = json.loads(json_str)
dict = {item['name']: item['marks'] for item in data}
# Create a FastAPI application
app = FastAPI()

# Define a route at the root web address ("/")
@app.get("/")
def read_root():
    return {"message": "HelloWorld!"}

@app.get("/api")
async def get_home(name: List[str] = Query(default=[])):
    mark = [0,0]
    mark[0] = dict[name[0]]
    mark[1] = dict[name[1]]
    return {"marks": mark}
