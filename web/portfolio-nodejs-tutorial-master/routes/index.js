// routes/index.js
var express = require('express');
var router = express.Router();
// MySQL
var {User} = require('../models');
var {Activity} = require('../models');
var {Award} = require('../models');

/* GET home page. */
router.get('/', function(req, res, next) {
	res.render('welcome', {'title': 'Welcome!!!'}); 
});

/* GET users listing. */
router.get('/users', function(req, res, next) {
	// get users data from DB
	User.findAll().then((data) => { 
		//console.log(data);
		res.render('list', { 'title': 'Portfolio', 'content': 'users', 'data': data});
	});
});

/* GET campus listing. */
router.get('/:userId/campus', function(req, res, next) {
	// get users data from DB
	Activity.findAll({ where : { userId: req.params.userId, iscampus: 0 }
	}).then((data) => { 
		res.render('list', { 'title': 'Campus', 'content': 'activities', 'userId': req.params.userId, 'data': data});
	});
});

/* GET extracurricular listing. */
router.get('/:userId/extracurricular', function(req, res, next) {
	// get users data from DB
	Activity.findAll({ where : { userId: req.params.userId, iscampus: 1 }
	}).then((data) => { 
		res.render('list', { 'title': 'Extra Curriculars', 'content': 'activities', 'userId': req.params.userId, 'data': data});
	});
});

/* GET awards listing. */
router.get('/:userId/awards', function(req, res, next) {
	// get users data from DB
	Award.findAll({ where : { userId: req.params.userId }
	}).then((data) => { 
		res.render('list', { 'title': 'Awards', 'content': 'awards', 'userId': req.params.userId, 'data': data});
	});
});


/* create & edit page load */
/* GET users editing. */
router.get('/:id/users/edit', function(req, res, next) {
	User.findOne({ where : {id : req.params.id }
	}).then((data) => { 
		//console.log(data);
		res.render('edit', { 'title': 'Portfolio', 'content': 'users', 'id': data.userId,'data': data});
	}).catch(err => {
		res.render('edit', { 'title': 'Portfolio', 'content': 'users', 'id': 0});
	});
});

/* GET campus editing. */
router.get('/:userId/campus/:id/edit', function(req, res, next) {
	Activity.findOne({ where : {id : req.params.id, iscampus: 0 }
	}).then((data) => { 
		res.render('edit', { 'title': 'Campus', 'content': 'activities', 'userId': data.userId,'data': data});
	}).catch(err => {
		res.render('edit', { 'title': 'Campus', 'content': 'activities', 'userId': req.params.userId});
	});
});

/* GET extracurricular editing. */
router.get('/:userId/extracurricular/:id/edit', function(req, res, next) {
	Activity.findOne({ where : {id : req.params.id, iscampus: 1 }
	}).then((data) => { 
		res.render('edit', { 'title': 'Extra Curriculars', 'content': 'activities', 'userId': data.userId,'data': data});
	}).catch(err => {
		res.render('edit', { 'title': 'Extra Curriculars', 'content': 'activities', 'userId': req.params.userId});
	});
});

/* GET awards editing. */
router.get('/:userId/awards/:id/edit', function(req, res, next) {
	Award.findOne({ where : {id : req.params.id }
	}).then((data) => { 
		res.render('edit', { 'title': 'Awards', 'content': 'awards', 'userId': data.userId,'data': data});
	}).catch(err => {
		res.render('edit', { 'title': 'Awards', 'content': 'awards', 'userId': req.params.userId});
	});
});

// POST(EDIT)
router.post('/users', function(req, res, next) {
	User.count({ where: {id: req.body.id}
	}).then(count => {
		var fields = {
			name: req.body.name, 
			gender: req.body.gender, 
			birth: req.body.birth, 
			school: req.body.school,
			grade: parseInt(req.body.grade) + parseInt(req.body.gradenum)
		};
		if(count != 0){
			User.update( fields, {where: { id: req.body.id}
			}).then(result => {
		   	 	res.send('<script type="text/javascript">'
					+ 'alert("수정이 완료되었습니다.");'
					+ 'window.location.href = "/users";</script>');
			}).catch(err => {
		   	 	res.send('<script type="text/javascript">'
					+ 'alert("수정하지 못했습니다.");'
					+ 'window.location.href = "/users";</script>');
			});	
		}else{
			User.create( fields ).then(result => {
		   	 	res.send('<script type="text/javascript">'
					+ 'alert("생성이 완료되었습니다.");'
					+ 'window.location.href = "/users";</script>');
			}).catch(err => {
		   	 	res.send('<script type="text/javascript">'
					+ 'alert("생성하지 못했습니다.");'
					+ 'window.location.href = "/users";</script>');
			});
		}
	});
});
router.post('/activities/:userId', function(req, res, next) {
	Activity.count({ where: {id: req.body.id}
	}).then(count => {
		var fields = {
			iscampus: req.body.iscampus,
			name: req.body.name, 
			type: req.body.type, 
			startdate: req.body.startdate, 
			enddate: req.body.enddate,
			text: req.body.text,
			userId: req.params.userId
		};
		var iscampus = (req.body.iscampus == 0 ? 'campus' : 'extracurricular');
		if(count != 0){	
			Activity.update( fields, {where: { id: req.body.id}
			}).then(result => {
		   	 	res.send('<script type="text/javascript">'
					+ 'alert("수정이 완료되었습니다.");'
					+ 'window.location.href = "/' + req.params.userId + '/' + iscampus + '";</script>');
			}).catch(err => {
		   	 	res.send('<script type="text/javascript">'
					+ 'alert("수정하지 못했습니다.");'
					+ 'window.location.href = "/' + req.params.userId + '/' + iscampus + '";</script>');
			});	
		}else{
			Activity.create( fields ).then(result => {
		   	 	res.send('<script type="text/javascript">'
					+ 'alert("생성이 완료되었습니다.");'
					+ 'window.location.href = "/' + req.params.userId + '/' + iscampus + '";</script>');
			}).catch(err => {
		   	 	res.send('<script type="text/javascript">'
					+ 'alert("생성하지 못했습니다.");'
					+ 'window.location.href = "/' + req.params.userId + '/' + iscampus + '";</script>');
			});
		}
	});
});
router.post('/awards/:userId', function(req, res, next) {
	Award.count({ where: {id: req.body.id}
	}).then(count => {
		var fields = {
			name: req.body.name, 
			institute: req.body.institute, 
			date: req.body.date, 
			enddate: req.body.enddate,
			text: req.body.text,
			userId: req.params.userId
		};
		if(count != 0){
			Award.update( fields, {where: { id: req.body.id}
			}).then(result => {
		   	 	res.send('<script type="text/javascript">'
					+ 'alert("수정이 완료되었습니다.");'
					+ 'window.location.href = "/' + req.params.userId + '/awards";</script>');
			}).catch(err => {
		   	 	res.send('<script type="text/javascript">'
					+ 'alert("수정하지 못했습니다.");'
					+ 'window.location.href = "/' + req.params.userId + '/awards";</script>');
			});	
		}else{
			Award.create( fields ).then(result => {
		   	 	res.send('<script type="text/javascript">'
					+ 'alert("생성이 완료되었습니다.");'
					+ 'window.location.href = "/' + req.params.userId + '/awards";</script>');
			}).catch(err => {
		   	 	res.send('<script type="text/javascript">'
					+ 'alert("생성하지 못했습니다.");'
					+ 'window.location.href = "/' + req.params.userId + '/awards";</script>');			});
		}
	});

});

// DELETE

router.post('/users/delete', function(req, res, next) {
	User.destroy({where: { id: req.body.id }
	}).then(result => {
   	 	res.send('<script type="text/javascript">'
			+ 'alert("삭제가 완료되었습니다.");'
			+ 'window.location.href = "/users";</script>');
	}).catch(err => {
   	 	res.send('<script type="text/javascript">'
			+ 'alert("삭제하지 못했습니다.");'
			+ 'window.location.href = "/users";</script>');
	});	
});
router.post('/activities/delete/:userId', function(req, res, next) {
	var iscampus = (req.body.iscampus == 0 ? 'campus' : 'extracurricular');
	Activity.destroy({where: { id: req.body.id }
	}).then(result => {
   	 	res.send('<script type="text/javascript">'
			+ 'alert("삭제가 완료되었습니다.");'
			+ 'window.location.href = "/' + req.params.userId + '/' + iscampus + '";</script>');
	}).catch(err => {
   	 	res.send('<script type="text/javascript">'
			+ 'alert("삭제하지 못했습니다.");'
			+ 'window.location.href = "/' + req.params.userId + '/' + iscampus + '";</script>');
	});
});
router.post('/awards/delete/:userId', function(req, res, next) {	
	Award.destroy({where: { id: req.body.id }
	}).then(result => {
   	 	res.send('<script type="text/javascript">'
			+ 'alert("삭제가 완료되었습니다.");'
			+ 'window.location.href = "/' + req.params.userId + '/awards";</script>');
	}).catch(err => {
   	 	res.send('<script type="text/javascript">'
			+ 'alert("삭제하지 못했습니다.");'
			+ 'window.location.href = "/' + req.params.userId + '/awards";</script>');
	});
});

module.exports = router;
