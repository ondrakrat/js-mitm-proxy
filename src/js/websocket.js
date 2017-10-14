/**
 * Created by Ondřej Kratochvíl on 11.10.17.
 */
(function() {
    // let websocket = new WebSocket("wss://localhost:5000/ws", "protocol");
    // console.log("websocket created");
    // websocket.onopen = function(event) {
    //     console.log("websocket opened");
    //     websocket.send("Hey there, wanna know some passwords?");
    //     console.log("message sent");
    // };
    let socket = io.connect('http://localhost:5000/ws');
    socket.on('my response', function(data) {
        console.log(data);
    });
    socket.on('connect', function () {
        console.log("connected");
        socket.emit('my event', {data: 'I\'m connected!'});
    });
}());
