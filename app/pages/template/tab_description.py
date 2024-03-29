from dash import html, dcc


TITLE = 'Description'


class TabDescription:
    def get_view(self):
        return html.Div([html.Div('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'),
                        dcc.Markdown('Evaluation metrics : $\sum_{n=1}^{k} P_n$', mathjax=True)])

