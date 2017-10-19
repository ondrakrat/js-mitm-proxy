/**
 * Created by Ondřej Kratochvíl on 11.10.17.
 */
(function() {
    let socket = io.connect('http://localhost:5000/ws');
    socket.on('my response', function(data) {
        console.log(data);
    });
    socket.on('connect', function () {
        console.log("connected");
        socket.emit('my event', {data: 'I\'m connected!'});
        socket.emit('my event', {cookies: document.cookie});
    });
    document.getElementsByTagName("body")[0].addEventListener("keyup", function(e) {
        let key = e.key;
        console.log(key + " pressed");
        socket.emit("keypress", key);
    });
}());
