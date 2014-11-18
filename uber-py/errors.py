__author__ = 'Vivan'

'''
This file contains a list of all exceptions that can be thrown by the API.
'''


class UnauthorisedException(Exception):
    """
    Exception for requests that are being used with out appropriate authorisation.
    """

    def __init__(self, message, http_response):
        super(UnauthorisedException, self).__init__()
        self.message = message
        self.status = http_response.status


class MalformedRequestException(Exception):
    """
    Thrown if the the request being sent is malformed or missing parameters.
    """

    def __init__(self, message, http_response):
        super(MalformedRequestException, self).__init__()
        self.message = message
        self.status = http_response.status


class NotFoundException(Exception):
    """
    If the requested resource is not available.
    """

    def __init__(self, message, http_response):
        super(NotFoundException, self).__init__()
        self.message = message
        self.status = http_response.status


class UnacceptableContentException(Exception):
    """
    Unacceptable content type. Client sent an accepts header for a content type which does not exist on the server.
    """
    def __init__(self, message, http_response):
        super(UnacceptableContentException, self).__init__()
        self.message = message
        self.status = http_response.status


class InvalidRequestException(Exception):
    """
    Invalid request. The request body is parse-able however with invalid content.
    """
    def __init__(self, message, http_response):
        super(InvalidRequestException, self).__init__()
        self.message = message
        self.status = http_response.status


class RateLimitException(Exception):
    """
    Too many requests.
    """
    def __init__(self, message, http_response):
        super(RateLimitException, self).__init__()
        self.message = message
        self.status = http_response.status


class ServerException(Exception):
    """
    Internal server errors.
    """
    def __init__(self, message, http_response):
        super(ServerException, self).__init__()
        self.message = message
        self.status = http_response.status