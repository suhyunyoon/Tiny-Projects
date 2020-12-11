module.exports = (sequelize, DataTypes) => { 
	return sequelize.define('activity', { 
		iscampus: { 
			type: DataTypes.BOOLEAN, 
			allowNull: false,
		}, 
		name: {  
			type: DataTypes.STRING(50), 	
			allowNull: false, 
		}, 	
		type: {  
			type: DataTypes.STRING(20), 	
			allowNull: false, 
		}, 
		startdate: { 
			type: DataTypes.DATEONLY, 
			allowNull: false, 
		},
		enddate: { 
			type: DataTypes.DATEONLY, 
			allowNull: false, 
		},
 		text: { 
			type: DataTypes.STRING(1024) 	 
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
}
