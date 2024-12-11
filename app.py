import os
import uuid
from flask import Flask, jsonify
from flask_session import Session
from sqlalchemy import types, text, JSON, MetaData, Any, dialects
from sqlalchemy.orm import Mapped, mapped_column
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    metadata = MetaData(
        naming_convention={
            "ix": "ix_%(column_0_label)s",
            "uq": "uq_%(table_name)s_%(column_0_name)s",
            "ck": "ck_%(table_name)s_%(constraint_name)s",
            # "ck": "ck_%(table_name)s_%(column_0_name)s",  # https://github.com/sqlalchemy/sqlalchemy/issues/3345
            "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
            "pk": "pk_%(table_name)s",
        }
    )

app = Flask(__name__)

db = SQLAlchemy(model_class=Base)

app.config["SQLALCHEMY_DATABASE_URI"] = (
    "postgresql+psycopg2://{user}:{password}@{host}:{port}/{db_name}".format(
        user=os.environ.get("FLASK_DATABASE_USER", "lucasys"),
        password=os.environ.get("FLASK_DATABASE_PASSWORD", "lucasys"),
        host=os.environ.get("FLASK_DATABASE_HOST", "localhost"),
        port=os.environ.get("FLASK_DATABASE_PORT", 5432),
        db_name=os.environ.get("FLASK_DATABASE_NAME", "lucasys"),
    )
)

db.init_app(app)

class Company(db.Model):
    __tablename__ = "company"
    __table_args__ = { "schema": "core" }
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    dit_company_id = db.Column(db.UUID)

    def to_dict(self):
        return { 'id': self.id, 'name': self.name, 'company_id': self.dit_company_id }
DEVELOPMENT_ENV = True

@app.route("/")
def index():
    companies = Company.query.all()
    print(map(lambda comp: comp.to_dict(), companies))
    temp = list(map(lambda comp: comp.to_dict(), companies))
    return jsonify(temp)


if __name__ == "__main__":
    # app.config['SQLALCHEMY_DATABASE_URI']='postgresql://dev-ci-postgres.cluster-cg9uuxm8vq93.us-east-1.rds.amazonaws.com:5432/fixture_test'
    app.run(debug=DEVELOPMENT_ENV, port=5050)
