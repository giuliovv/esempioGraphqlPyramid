import graphene

from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.view import view_config
from pyramid.session import SignedCookieSessionFactory

from webob_graphql import serve_graphql_request

from layerGraphql import Risultato

@view_config(
    route_name='graphql',
    # The serve_graphql_request method will detect what's the best renderer
    # to use, so it will do the json render automatically.
    # In summary, don't use the renderer='json' here :)
)
def graphql_view(request):
    context = {'session': request.session}
    schema = graphene.Schema(query=Risultato)
    return serve_graphql_request(request, schema, context_value=context, graphiql_enabled=True)#, batch_enabled=True)


if __name__ == '__main__':
    my_session_factory = SignedCookieSessionFactory('itsaseekreet')
    with Configurator() as config:
        config.add_route('graphql', '/graph')
        config.add_view(graphql_view, route_name='graphql')
        config.set_session_factory(my_session_factory)
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8765, app)
    server.serve_forever()