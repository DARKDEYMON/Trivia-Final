$(function($) {
    console.log( "ready!" );
    var socket = io('http://localhost:4000');
    socket.emit("test",{});
    socket.on('test', function(response) {
    	console.log(response.conectado);
	});
	$("#jugar").click(function(event) {
		console.log("clickeado!!"); 
		var cookies=document.cookie;
		var comienzo=cookies.indexOf("sessionid");
		console.log(leerCookie("sessionid"));
        ajaxresponse(leerCookie("sessionid"));
	});
	var leerCookie=function(nombre) {
        var lista = document.cookie.split(";");
        micookie="";
        for (var i in lista) {
            var busca = lista[i].search(nombre);
            if (busca > -1)
            {
            	micookie=lista[i];
            }
        }
        var igual = micookie.indexOf("=");
        var valor = micookie.substring(igual+1);
        return valor;
    };
    var ajaxresponse=function(idkey)
    {
        $.ajax({
            url: 'http://127.0.0.1:4000/django/'+idkey,
            headers: { 'Access-Control-Allow-Origin': '*' },
            type: 'GET',
            dataType: 'html', //jsomp
            data: {},
        })
        .done(function(html) {
            console.log("paso");
            console.log(html);
            $("#contenido").html();
            $("#contenido").html(html);
        })
        .fail(function() {
            console.log("error");
        })
        .always(function() {
            console.log("complete");
        });
        
    };
});

