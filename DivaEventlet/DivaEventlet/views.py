import eventlet
from django.http import HttpResponse
from .comunication import MapfreSoap, AbaSoap, IPSoap


def test_eventlet(request):
    http_response = []
    number_service = [1, 2, 3]

    pool = eventlet.GreenPool()

    try:
        for response in pool.imap(get_service, number_service):
            http_response.append(response)
    except:
        pass

    return HttpResponse(http_response)


def get_service(number_service):
    if number_service == 1:
        mapfre = MapfreSoap()
        return mapfre.get_mapfre_response()
    elif number_service == 2:
        aba = AbaSoap()
        return aba.get_aba_response()
    else:
        ipsoap = IPSoap
        return ipsoap.get_ip_response()
