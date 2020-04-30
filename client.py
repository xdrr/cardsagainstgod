import socketio, sys, os, uuid, argparse

class CardsAgainstIsolationClient(socketio.ClientNamespace):
    _player_id = "god"

    def __init__(self, game_id):
        super().__init__()

        self._game_id = game_id

    def on_connect(self):
        print("connected to server, joining game...")
        self.send({
            "event": "join_game",
            "player": self._player_id,
            "game": self._game_id
        })

    def on_message(self, data):
        print("incoming msg ->:", data)

    def on_connect_error(self):
        print("failed to connect ot server")

def cli(args, sio):
    while True:
        cmd_str = input("> ")

        if not len(cmd_str) or cmd_str == None:
            continue

        if len(cmd_str.split()) < 2:
            print("A command and args need to be provided")
            continue

        cmd, args = cmd_str.split(maxsplit=1)

        if cmd == "help":
            show_help()

        else:
            payload = {"event": cmd}

            for arg in args.split():
                if "=" not in arg:
                    print(f"Incomplete arg: {arg}")
                    break

                k, v = arg.split("=")
                payload[k] = v

            if len(args.split()) == len(payload.keys()) - 1:
                print("send")
                sio.send(payload)

def main(args):
    sio = socketio.Client()
    sio.register_namespace(CardsAgainstIsolationClient(args.g))
    sio.connect('https://cards.dparrish.com/socket.io/',
            headers={"Origin": "https://cards-against-isolation.web.app"}
    )

    cli(args, sio)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Cards against isolation: client")
    parser.add_argument("-g", type=str, required=True, help="Game to select")

    args = parser.parse_args()

    main(args)
