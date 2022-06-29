# © 2022, Dandy technology LLC

from api_hub import settings_api_hub
from waitress import serve
import sys

app = settings_api_hub()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        ip = sys.argv[1]
    else:
        ip = '127.0.0.1'
    print(ip)
    serve(app, host=ip, port=5000)
