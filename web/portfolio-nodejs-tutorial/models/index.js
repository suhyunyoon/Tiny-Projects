var path = require('path');
var Sequelize = require('sequelize');

var config = require(path.join(__dirname, '..', 'config', 'db.js')); 
var db = {}; 
//console.log(config);
var sequelize = new Sequelize(config.database, config.user, config.password, config); 
db.sequelize = sequelize; 
db.Sequelize = Sequelize; 

db.User = require('./user')(sequelize, Sequelize);
db.Activity = require('./activity')(sequelize, Sequelize);
db.Award = require('./award')(sequelize, Sequelize); 

db.User.hasMany(db.Activity, {as: 'Activities', onDelete: 'cascade'});
db.User.hasMany(db.Award, {as : 'Awards', onDelete: 'cascade'});

module.exports = db;

