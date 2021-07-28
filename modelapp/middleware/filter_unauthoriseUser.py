from django.http import Http404

class FilterUnauthoriseUser:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/info/'):
            if not request.user.is_authenticated:
                raise Http404
        response = self.get_response(request)
        return response
        
