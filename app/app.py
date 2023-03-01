import dash
import dash_html_components as html
import dash_auth

# Define a list of valid username-password pairs
VALID_USERNAME_PASSWORD_PAIRS = {
    'user1': 'password1',
    'user2': 'password2'
}

# Create a Dash app instance
app = dash.Dash(__name__)

# Create a server object for the app
server = app.server

# Define the app's layout
app.layout = html.Div([
    html.H1('Hello, World!'),
])

# Authenticate users using the BasicAuth object
auth = dash_auth.BasicAuth(
    app,
    VALID_USERNAME_PASSWORD_PAIRS
)

if __name__ == '__main__':
    app.run_server(debug=True)
