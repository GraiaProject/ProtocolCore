"""若需要抛出错误, 使用这些错误进行一个封装(`raise ... from ...`)

RequestFailed
  |- HTTPError
      |- WebsocketError

WrongInformation
  |- AuthenticateFailed
  |- InvaildSession
  |- ReleaseFailed
  |- WrongTarget

HeadlessClientException
  |- RateLimit
  |- InvaildRequest
  |- InvaildResponse
  |- WrongTarget
"""

class RequestFailed(Exception):
    pass

class HTTPError(RequestFailed):
    pass

class WebsocketError(HTTPError):
    pass

class WrongInformation(Exception):
    pass

class AuthenticateFailed(WrongInformation):
    pass

class InvaildSession(WrongInformation):
    pass

class ReleaseFailed(WrongInformation):
    pass

class HeadlessClientException(Exception):
    pass

class RateLimit(HeadlessClientException):
    pass

class InvaildRequest(HeadlessClientException):
    pass

class InvaildResponse(HeadlessClientException):
    pass

class WrongTarget(HeadlessClientException, WrongInformation):
    pass