from django.http import JsonResponse
from django.core.cache import cache
from rest_framework import views
import sys

from .models import HistoryDeals, Deal
from .serializers import DealSerializer
from .logic import csv_data, get_response


class RootView(views.APIView):
    page_cache = 'page_cache'

    def get(self, request):
        print("GET")
        try:
            if cache.get(self.page_cache):
                is_cache = True
                five_clients = cache.get(self.page_cache)
            else:
                is_cache = False
                five_clients = get_response.sort_data()
                cache.set(self.page_cache, five_clients, 60)  # one minute
        except:
            return JsonResponse({'status': 'Error', 'desc': ' '.join([str(exc) for exc in sys.exc_info()])})
        return JsonResponse({'status': 'OK', 'cached': is_cache, 'response': five_clients})

    def post(self, request):
        try:
            history = HistoryDeals()
            history.save()
            if request.FILES:
                for key_file in request.FILES:
                    data = request.FILES[key_file].read().decode('utf-8')
                    # было бы лучше отправить все данные одним запросом к базе данных...
                    deals_list = []
                    for deal in csv_data.to_db(data):
                        d = Deal(**deal, deal=history)
                        deals_list.append(d)
                    Deal.objects.bulk_create(deals_list)
                cache.delete(self.page_cache)
                return JsonResponse({'status': 'OK'})

            else:
                history.delete()
                return JsonResponse({'status': 'Error', 'desc': 'not found data in POST method'})

        except:
            history.delete()
            return JsonResponse({'status': 'Error', 'desc': ' '.join([str(exc) for exc in sys.exc_info()])})
