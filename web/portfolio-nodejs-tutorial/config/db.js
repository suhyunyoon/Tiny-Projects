// config/db.js

module.exports = {
  host     : '127.0.0.1',
  user     : 'root',
  password : '',
  database : 'portfolio',
  port		: 3306,
  dialect	: "mysql",
  operatorAliases : false,
  define: {
    charset: 'utf8',
    collate: 'utf8_general_ci'
  }
};
