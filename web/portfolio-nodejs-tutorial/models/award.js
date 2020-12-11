module.exports = (sequelize, DataTypes) => { 
	return sequelize.define('award', { 
		name: { 
			type: DataTypes.STRING(50), 	
			allowNull: false, 
		}, 
		institute: { 
			type: DataTypes.STRING(50), 
			allowNull: false,
		}, 
		date: { 
			type: DataTypes.DATEONLY, 
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
}
