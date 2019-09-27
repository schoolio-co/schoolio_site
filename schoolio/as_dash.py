# -*- coding: utf-8 -*-
import sys

import dash
import dash_core_components as dcc
import dash_html_components as dhc


def dispatcher(request):
    '''
    Main function
    @param request: Request object
    '''

    app = _create_app()
    params = {
        'data': request.body,
        'method': request.method,
        'content_type': request.content_type
    }
    with app.server.test_request_context(request.path, **params):
        app.server.preprocess_request()
        try:
            response = app.server.full_dispatch_request()
        except Exception as e:
            response = app.server.make_response(app.server.handle_exception(e))
        return response.get_data()


def create_app(layout):
    ''' Creates dash application '''
    app = dash.Dash()
    app.layout = layout
    @app.callback(
        dash.dependencies.Output('content', 'children'),
        [dash.dependencies.Input('url', 'pathname')]
    )
    def display_page(pathname):
        ''' '''
        if not pathname:
            return ''
        if pathname == '/':
            return dash_index()
        method = pathname[1:].replace('-', '_')
        func = getattr(sys.modules[__name__], method, None)
        if func:
            return func()
        return 'Unknown link'
    return app


if __name__ == '__main__':
    app = _create_app()
    app.run_server()

