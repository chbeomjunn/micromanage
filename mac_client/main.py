import websocket
import _thread
import time
import rel
from lib import macos


api_base = "mmbe.pexl.pw"
websocket_endpoint = "wss://" + api_base + "/ws"


def on_message(ws, message):
    print(message)

def on_error(ws, error):
    print(error)

def on_close(ws, close_status_code, close_msg):
    exit()

def on_open(ws):
    print("Opened connection")
    ws.send()

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(websocket_endpoint,
                              on_open=on_open,
                              on_message=on_message,
                              on_error=on_error,
                              on_close=on_close)

    ws.run_forever(dispatcher=rel, reconnect=5)  # Set dispatcher to automatic reconnection, 5 second reconnect delay if connection closed unexpectedly
    rel.signal(2, rel.abort)  # Keyboard Interrupt
    rel.dispatch()
