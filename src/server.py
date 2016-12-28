from views import *
from apis import *

# app = create_app()
# app.debug = True

server = Server(app.wsgi_app)

if __name__ == "__main__":

	server.serve(port=5000)


