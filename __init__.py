from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)

# engine = create_engine('mssql+pymssql://argaamv2user:argaam123$@172.16.3.75/ArgaamV2')
engine = create_engine('mssql+pymssql://sa:abc123@./ArgaamPlus_09Mar')

Session = sessionmaker(bind=engine)
session = Session()

# Import Versions blueprints
from api.V1 import api_v1_blueprint
from api.V2 import api_v2_blueprint

# Register Blueprint
app.register_blueprint(api_v1_blueprint,url_prefix='/v1')
app.register_blueprint(api_v2_blueprint,url_prefix='/v2')


if __name__ == '__main__':
    app.run(debug=True)