import os
from dotenv import load_dotenv

import requests

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response


class ConverterViewSet(viewsets.ViewSet):
    @action(methods=["get"], detail=False)
    def rates(self, request, *args, **kwargs):
        if request.method == "GET":
            curr_from = request.GET.get('from')
            curr_to = request.GET.get('to')
            value = request.GET.get('value')

            load_dotenv()
            appid = os.environ.get('SECRET_KEY')

            # url = 'http://data.fixer.io/api/convert?access_key={}&from={}&to={}&amount={}'
            url = 'http://data.fixer.io/api/latest?access_key={}'
            res = requests.get(url.format(appid)).json()

            result = (float(res['rates'][curr_to]) / (float(res['rates'][curr_from]))) * float(value)
            context = {"result": round(result, 2)
                       }

            return Response(context)
        else:
            return Response(
                {"error": f"Неправильный запрос"}, status.HTTP_400_BAD_REQUEST
            )
