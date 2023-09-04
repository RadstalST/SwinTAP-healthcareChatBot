from ninja import NinjaAPI

api = NinjaAPI()

# @api.get("/hello")
# def hello(request):
#     return "hello world"

@api.get("/hello")
def hello_name(request, name: str):
    return {"hello": name}