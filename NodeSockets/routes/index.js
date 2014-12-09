var express = require('express');
var router = express.Router();

var session=require("../session/django");
var s=session();

/* GET home page. */
var mysql=require("../db/mysql");
var query=new mysql({
		host     : 'localhost',
		user     : 'root',
		password : '123456789',
		port     : '3305',
		database : 'trivia'
});

var sesiones=Array();

router.get("/django/",function(req,res){
	res.header("Access-Control-Allow-Origin", "*");
    res.header("Access-Control-Allow-Headers", "X-Requested-With");
		if(sesiones[req.cookies.sessionid]==undefined)
		{
			res.writeHead("302",{"Location":"http://127.0.0.1:8000/user/login/"});
			res.end();
			return;
		}
		query.get("usuario_partida").where({acabada:0}).execute(function(rows){
				console.log(rows[0]);
				req.params.username=s.name;
				sesiones[req.cookies.sessionid]={id:req.params.id,name:s.name};
				console.log(sesiones[req.cookies.sessionid]);
				res.render('unirse', { title: 'Chat',sessionid:req.params.id,name:s.name,partidas:rows});
		});

});

router.get("/crear_partida/",function(req,res){
	res.header("Access-Control-Allow-Origin", "*");
    res.header("Access-Control-Allow-Headers", "X-Requested-With");
	if(sesiones[req.cookies.sessionid]==undefined)
	{
		res.writeHead("302",{"Location":"http://127.0.0.1:8000/user/login/"});
		res.end();
		return;
	}
	res.render('crear_partida',{title:"Chat",idsession:sesiones[req.cookies.sessionid].id,username:sesiones[req.cookies.sessionid].name});

});
router.get("/sala/:idr?",function(req,res){
	res.header("Access-Control-Allow-Origin", "*");
    res.header("Access-Control-Allow-Headers", "X-Requested-With");
	if(sesiones[req.cookies.sessionid]==undefined)
	{
		console.log(sesiones[req.cookies.sessionid]);
		res.writeHead("302",{"Location":"http://127.0.0.1:8000/user/login/"});
		res.end();
		return;
	}
	console.log(req.params.idr);
	sesiones[req.cookies.sessionidr]={id:req.params.idr};
	res.render('saladechatespera', { title: 'Sala de Espera',salaid:req.params.idr});
});
router.get('/conectar/:id?', function(req, res) {
	res.header("Access-Control-Allow-Origin", "*");
    res.header("Access-Control-Allow-Headers", "X-Requested-With");
    //req.session.q='1';
    //req.session.id='1';
    console.log(req.params.id);
	console.log(req.cookies);//.sessionid);

	s.getSession(req.params.id,function(s){
		console.log(s);
		if(s.estado=="conectado")
		{
			req.params.username=s.name;
			sesiones[req.cookies.sessionid]={id:req.params.id,name:s.name};
			console.log(sesiones[req.cookies.sessionid]);
		}
	});
});
router.get('/', function(req, res) {
  res.render('index', { title: 'Express' });
  console.log(req.cookies);
});
module.exports = router;
