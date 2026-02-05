from dataclasses import dataclass

class Profile:
    def view(request):
        pass
    def save(request):
        pass
    def find_friends(request):
        pass

class RequestHandler:
    def extract_query_param(request, param):
        pass
    def reply_OK(request, html):
        pass
    def reply_not_found(request, error):
        pass

class DatabaseHandler:
    def open_(location, user):
        pass
    def close(location):
        pass


@dataclass
class FrontendServer:
    profile: Profile = Profile()
    request_handler: RequestHandler = RequestHandler()
    database_handler: DatabaseHandler = DatabaseHandler()


# example usage of this code:
server = FrontendServer()
server.profile.view(request)