def application(environ, start_reponse):
    status = '200 OK'
    headers = [('Content-type', 'text/plain')]
    query = environ['QUERY_STRING']
    response = ''
    for item in query.split('&'):
        response = response + item + "\r\n"
    start_reponse(status, headers)
    return response
