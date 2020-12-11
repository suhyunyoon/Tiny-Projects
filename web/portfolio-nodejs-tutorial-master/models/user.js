var models = require('../models');
module.exports = (sequelize, DataTypes) => { 
	const user = sequelize.define('user', { 
		name: { 
		/* column 속성들 */ 
			type: DataTypes.STRING(10), 	
			allowNull: false, 
		}, 
		gender: { 
			type: DataTypes.BOOLEAN, 
			allowNull: false,
		}, 
		birth: { 
			type: DataTypes.DATEONLY, 
			allowNull: false, 
		},
 		school: { 
			type: DataTypes.STRING(20), 	
			allowNull: false, 
		}, 
		grade: { 
			type: DataTypes.INTEGER, 	
			allowNull: false, 
		},
        createdAt: {
    	    type: 'TIMESTAMP',
	        defaultValue: sequelize.literal('CURRENT_TIMESTAMP'),
        	allowNull: false
	    },
	    updatedAt: {
    	    type: 'TIMESTAMP',
	        defaultValue: sequelize.literal('CURRENT_TIMESTAMP'),
        	allowNull: false
      	} 
	});
    
	return user; 
}
