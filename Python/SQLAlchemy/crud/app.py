from sqlalchemy import create_engine  

connect_args = {
	'user': 'root',
	'password': '1234',
	'database': 'store',
	'host': '127.0.0.1',
	'port': 3306
	}


e = create_engine('mysql+pymysql://', connect_args=connect_args)