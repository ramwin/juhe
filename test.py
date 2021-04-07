from juhe import API
import pprint


api = API()
print("当前汇率: ")

key = input("输入汇率key: ")
key = key or "ea634711720a27cbc2d34402987009ba"

pprint.pprint(
    api.query_exchange(key),
    indent=4,
)

key = input("输入笑话key: ")
key = key or "341969d376e88299435aa784b6902916"

pprint.pprint(
    api.get_jokes(key),
    indent=4,
)
