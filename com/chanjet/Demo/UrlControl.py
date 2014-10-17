import web
urls = (
#     "/.*","hello",
    "","SomePage",
    "/someotherpage1","tiao",
    "/tasks/.*", "signin",
    "/tasks/list", "listing",
    "/tasks/post", "post",
    "/tasks/chgpass", "chgpass",
    "/tasks/act", "actions",
    "/tasks/logout", "logout",
    "/tasks/signup", "signup",
    "/users/list/(.+)", "list_users"
)
app = web.application(urls,globals())
class SomePage:
    def GET(self):
        # Do some application logic here, and then:
#         return "SomePageaa"
        raise web.seeother('/someotherpage1')

class tiao():
    def GET(self):
        return "have redicted"
class list_users:
    def GET(self, name):
        return "Listing info about user: {0}".format(name)


class listing:
    def GET(self):
        return "listing begin"
class signin:
    def GET(self):
        return "signin begin"
class hello():
    def GET(self):
        return "Hello"
if __name__ == '__main__':
    app.run()