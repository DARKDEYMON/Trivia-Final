var express = require('express');
var cookieParser = require('cookie-parser');
var session = require('express-session');

var app = express();

app.use(session({
  secret: 'keyboard cat',
  resave: false,
  saveUninitialized: true
}));
app.use(cookieParser());


var path = require('path');
var favicon = require('serve-favicon');
var logger = require('morgan');
var cookieParser = require('cookie-parser');
var bodyParser = require('body-parser');

var routes = require('./routes/index');
var users = require('./routes/users');
var io=require("socket.io");
var app = express();

// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'jade');

// uncomment after placing your favicon in /public
//app.use(favicon(__dirname + '/public/favicon.ico'));
app.use(logger('dev'));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));

app.use('/', routes);
app.use('/users', users);

// catch 404 and forward to error handler
app.use(function(req, res, next) {
    var err = new Error('Not Found');
    err.status = 404;
    next(err);
});

// error handlers

// development error handler
// will print stacktrace
if (app.get('env') === 'development') {
    app.use(function(err, req, res, next) {
        res.status(err.status || 500);
        res.render('error', {
            message: err.message,
            error: err
        });
    });
}

// production error handler
// no stacktraces leaked to user
app.use(function(err, req, res, next) {
    res.status(err.status || 500);
    res.render('error', {
        message: err.message,
        error: {}
    });
});

//aqui empiesa todo

var session=require("./session/django");
var s=session();

module.exports = app;


var cookie_reader = require('cookie');

var PORT=4000;
var server=app.listen(PORT,function(){
    console.log("Servidor y socket corriendo en "+PORT);
});
/*
io.use(function(socket, next){
    if (socket.request.headers.cookie)
        return next();
    next(new Error('Authentication error'));
});*/

var sockets =io(server);

sockets.on('connection',  function(socket) {
    socket.on('test', function(data) {
        //console.log(socket.handshake);
        socket.emit("test",{"conectado":"coneccion exitosa!!!"});
        return;
    });
    socket.on('sala_juego', function(data) {
        console.log(data.sala+"   sala socket  " +data.sessionid);
        s.getSession(data.sessionid,function(s){
            if(s===false)
              return;
            if(s.estado=="conectado")
            {
              //socket.disconnect();
              socket.salas=data.sala;
              socket.join(data.sala);

              console.log(data.sala);
            }
        });
        return;
    });
    socket.on('mensajes', function(data) {
        //console.log(data.sala+"   sala socket  " +data.sessionid);
        console.log(data.msn+"  mensaje");
        s.getSession(data.sessionid,function(s){
            if(s.estado=="conectado")
            {
              console.log(data.msn+"  mensaje  " +s.name);
              sockets.to(socket.salas).emit("mensajes",{"msn":data.msn,"nick":s.name});
            }
        });
        return;
    });
});


/*
var mysql      = require('mysql');
var connection = mysql.createConnection({
  host     : 'localhost',
  user     : 'root',
  password : '123456789',
  port     : '3305',
  database : 'information_schema'
});

connection.connect();
connection.query('select * from INNODB_SYS_FOREIGN', function(err, rows, fields) {
  if (err) throw err;

  console.log('The solution is: ', rows[0]);
});*/