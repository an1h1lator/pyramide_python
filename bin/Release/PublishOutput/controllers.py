def hello_world(request):
    url = request.url
    name = request.params.get('name', 'No name provided');
    body = 'URL %s with name: %s' % (url, name)
    return Response(
        content_type="text/plain",
        body=body
    )