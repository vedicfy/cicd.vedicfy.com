from django.http import JsonResponse

def simple_get_request(request):
    return JsonResponse({'message': 'Hello, this is a simple GET API'})
