# js-mitm-proxy
Example of JS injection using Man-in-the-middle proxy

## How to
* Visit [mitm.it]() and install the mitmproxy certificate (this downloads the certificates to `~/mitmproxy/`)
* Setup browser to use proxy `localhost:port_number` (for all types of requests)
* Setup port forwarding from port 80 and 443 to `port_number`
  * `sudo sysctl -w net.ipv4.ip_forward=1`
  * `sudo iptables -t nat -A PREROUTING -i wlan1 -p tcp --dport 80 -j REDIRECT --to-port 8080`
  * `sudo iptables -t nat -A PREROUTING -i wlan1 -p tcp --dport 443 -j REDIRECT --to-port 8080`
* Start MITM proxy with `mitmproxy -p port_number`

At this moment, you can already sniff all communication through the proxy in a neat CLI.

If you want to modify the requests via script, do the following instead of the last step:
* Start MITM proxy with `mitmdump -p port_number -s script.py`

#### Python WebSocket server
Install required packages: `pip install flask flask_socketio gevent gevent-websocket` and run the server 
with `python websocket_server.py`. The server runs on `https://localhost:5000`, websocket is exposed at 
`localhost:5000/ws`. WSS hack: allow mixed content in browser.

## Useful links
* https://mitmproxy.org/
* https://security.stackexchange.com/questions/72652/javascript-injection-using-man-in-the-middle-attack
* http://pankajmalhotra.com/Injecting-Javascript-In-HTML-Content-Using-MITM-Proxy
* https://blog.heckel.xyz/2013/07/01/how-to-use-mitmproxy-to-read-and-modify-https-traffic-of-your-phone/
* https://blog.miguelgrinberg.com/post/easy-websockets-with-flask-and-gevent
