var express = require('express');
var router = express.Router();

var session=require("../session/django");
var s=session();

/* GET home page. */
var sesiones=Array();
router.get("/django/:id?",function(req,res){
	console.log(req.params.id);

	s.getSession(req.params.id,function(s){
		
		console.log(s);
		
		if(s.estado=="conectado")
		{
			req.params.username=s.name;
			sesiones[req.cookies.sessionid]={id:req.params.id,name:s.name};
			res.render('saladechat', { title: 'Chat',sessionid:req.params.id,name:s.name});
		}else{
			res.writeHead("302",{"Location":"http://127.0.0.1:8000/user/login/"});
			res.end();
		}
		
	});
});


router.get('/', function(req, res) {
  res.render('index', { title: 'Express' });
});

module.exports = router;
