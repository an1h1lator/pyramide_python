import cgi

from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response
from pyramid.view import view_config

#First view from http://ip:port
@view_config(route_name='home')
def home_view(request):
    #return Response('<p>Visit <a href="/howdy?name=Lisa">hello</a></>')
    return Response('<p>Visit <a href="/howdy/Lisa Ann">hello</a></>')

#Second view from http://ip:port/howdy
#@view_config(route_name='hello')
#def hello_view(request):
#    name = request.params.get('name', 'No Name')
#    body = '<p>Hi, %s this <a href="/goto">redirects</a></p>'
#    # cgi.escape to prevent Cross-Site Scripting (XSS) [CWE 79]
#    return Response(body % cgi.escape(name));

# /goto which issues HTTP redirect to the last view
@view_config (route_name='redirect')
def redirect_view(request):
    return  HTTPFound(location="/problem")

# /problem which causes a site error
@view_config (route_name='exception')
def exception_view(request):
    raise Exception()

@view_config (route_name='hello', renderer='app/views/hello_world.pt')
def hello_world(request):
    return dict(name = request.matchdict['name'])