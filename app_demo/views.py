from django.http import JsonResponse
from django.views import View
from .tasks import get_entity


class EntityView(View):

    def get(self, request):
        get_entity.delay()
        return JsonResponse({"status": 2000, "msg": "success", "data": ""})
