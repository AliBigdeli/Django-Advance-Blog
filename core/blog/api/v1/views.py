from rest_framework.decorators import api_view
from rest_framework.response import Response

data = {
    "id":1,
    "title":"hello"
}


@api_view()
def postList(request):
    return Response("ok")

@api_view()
def postDetail(request,id):
    return Response(data)