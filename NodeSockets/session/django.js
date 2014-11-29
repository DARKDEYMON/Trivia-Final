var mysql=require("../db/mysql");
var django=function()
{
	var query=new mysql({
		host     : 'localhost',
		user     : 'root',
		password : '123456789',
		port     : '3305',
		database : 'trivia'
	});
	this.getSession=function(key,callback)
	{
		query.get("django_session").where({session_key:key}).execute(function(rows){
			
			if(rows.length>0){
				
				var data=new Buffer(rows[0].session_data, 'base64').toString('ascii');
				//console.log(data);
				var objson=data.split(":{");
				var jsonObj="{"+objson[1];
				var jsonreal=JSON.parse(jsonObj);
				//console.log(jsonreal.idkey);
				//res.render("saladechat",{title:"Sala"});
				
				query.get("django_session").where({session_key:jsonreal.idkey}).execute(function(rows){
					var data=new Buffer(rows[0].session_data, 'base64').toString('ascii');
					//console.log(data);
					var objson=data.split(":{");
					var jsonObj="{"+objson[1];
					var jsonreal=JSON.parse(jsonObj);
					//console.log(jsonreal);
					callback(jsonreal);
				});
			}else{
				callback(false);
			}

		});
	};
	return this;
};
module.exports=django;