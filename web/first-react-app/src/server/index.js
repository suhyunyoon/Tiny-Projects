const express = require('express');
//const bodyParser = require('body-parser');
//const os = require('os');
const mysql = require('mysql');
const dbconfig = require('../../config/db_config.js');
const connection = mysql.createConnection(dbconfig);

const app = express();
//app.use(bodyParser.json());

app.use(express.static('dist'));

// Username을 불러옴
app.get('/api/getUsername', 
	(req, res) => {
		//connection.connect();
		connection.query('SELECT * from user', function(err, rows, fields){
			if(!err){
				// console.log(rows);
				// send random name
				const min = 0;
				const max = 4;
				const rand = Math.floor(min + Math.random() * (max - min+1));
				res.send({aaa: 'abcd', username: rows[rand].name });
				//res.status(200).json({url: '123', username: rows});
			}
			else{
				console.log(err);
				res.send({username: '이름'});
			}
		});
		//connection.end();
		//res.send({username: os.userInfo().username })
	}
);
 
app.listen(8080, () => console.log('Listening on port 8080!'));
