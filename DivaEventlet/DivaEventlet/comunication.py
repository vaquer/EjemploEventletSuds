from django.conf import settings
from suds.client import Client

class MapfreSoap(Client):
    """Este es el cliente que va a consumir las peticiones SOAP"""

    def __init__(self):
        """ Inicializamos el cliente y le pasamos el parametro my_wsdl"""
        assert getattr(settings, 'MAPFRE_WSDL')
        self._client = Client(getattr(settings, 'MAPFRE_WSDL'))

    def get_mapfre_response(self):
        """Este va a ser el metodo que va a hacer la peticion al servicio web"""
        response_soap = self._client.service.WS_TW_ACotiza()
        self._response_mapfre = response_soap

        return response_soap


class AbaSoap(Client):
    def __init__(self):
        assert getattr(settings, 'ABA_WSDL')
        self._client = Client(getattr(settings, 'ABA_WSDL'))

    def get_aba_response(self):
        response_soap = self._client.service.CotizaWsAuto()
        self._response_aba = response_soap

        return response_soap


class IPSoap(Client):
    def __init__(self):
        assert getattr(settings, 'IP_WSDL')
        self._client = Client(getattr(settings, 'IP_WSDL'))

    def get_ip_response(self):
        response_soap = self._client.service.TestResponse()
        self._response_ip = response_soap

        return response_soap
