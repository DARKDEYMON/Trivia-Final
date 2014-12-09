$( document ).ready(function() {
    $.createRom=function(l)
    {
        var cookies=document.cookie;
        var comienzo=cookies.indexOf("sessionid");
        console.log(leerCookie("sessionid"));
        ajaxresponse("sala",l);
    };
    
    console.log( "ready!" );
    var socket = io('http://localhost:4000');
    socket.emit("test",{});
    $('body').on('click', '#entrar', function(){
        console.log("entro");
        console.log(this);
        console.log($(this).attr("val"));
        ajaxresponse("sala",$(this).attr("val"));
    });
	$("#jugar").click(function(event) {
		console.log("clickeado!!"); 
		var cookies=document.cookie;
		var comienzo=cookies.indexOf("sessionid");
		console.log(leerCookie("sessionid"));
        ajaxresponse("django","");
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
    var conectar=function()
    {
        l=leerCookie("sessionid");
        console.log(l);
        $.ajax({
            url: 'http://127.0.0.1:4000/conectar/'+l,
            crossDomain: true,
           // xhrFields: {
             //     withCredentials: true
              // },
            //headers: { 'Access-Control-Allow-Origin': '*' },
            type: 'GET',
            dataType: 'html', //jsonp
            data: {},
        })
        .done(function() {
            console.log("Conectado !!!!");
        })
        .fail(function() {
            console.log("error");
        })
        .always(function() {
            console.log("complete");
        });
    };
    conectar();
    var ajaxresponse=function(url,idkey)
    {
        $.ajax({
            url: 'http://127.0.0.1:4000/'+url+'/'+idkey,
            crossDomain: true,
           // xhrFields: {
             //     withCredentials: true
              // },
            //headers: { 'Access-Control-Allow-Origin': '*' },
            type: 'GET',
            dataType: 'html', //jsonp
            data: {},
        })
        .done(function(html) {
            //console.log("paso");
            //console.log(html);
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