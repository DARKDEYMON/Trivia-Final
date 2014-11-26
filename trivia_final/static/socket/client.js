$(function($) {
    console.log( "ready!" );
    var socket = io('http://localhost:4000');
    socket.emit("test",{});
    socket.on('test', function(response) {
    	console.log(response.conectado);
	});
});