import uuid
from django.utils.deprecation import MiddlewareMixin
from .settings import _req_local # reuse thread-local

class RequestIDMiddleware(MiddlewareMixin):
    """"
    Adds X-Request-ID header (incoming or generated) and stores it
    for logging filter to include in log times.
    """
    def process_request(self, request):
        rid = request.headers.get("X-Request-ID") or uuid.uuid4().hex
        _req_local.request_id = rid
        request.request_id = rid

    def process_response(self, request, response):
        try:
            rid = getattr(request, "request_id", getattr(_req_local, "request_id", None))
            if rid:
                response["X-Request-ID"] = rid
        finally:
            try:
                del _req_local.request_id
            except Exception:
                pass

        return response