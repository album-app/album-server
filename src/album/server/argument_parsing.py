from album.api import Album
from album.server.server import AlbumServer

def start_server(album_instance: Album, args):
    server = AlbumServer(args.port, args.host)
    server.setup(album_instance)
    server.start()


def create_server_parser(parser):
    p = parser.create_command_parser('server', start_server,
                                     'start an album server.')
    p.add_argument('--port', type=int, required=False, default=8080, help='Port')
    p.add_argument('--host', type=str, required=False, default="127.0.0.1", help='Host')
