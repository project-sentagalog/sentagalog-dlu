from app import db
import datetime 

class User(db.Model): 
    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(64), index=True) 
    first_name = db.Column(db.String(120), index=True)
    last_name = db.Column(db.String(120), index=True)
    role = db.Column(db.Integer)
    avatar = db.Column(db.String(256))
    bio = db.Column(db.String(1000))
    last_labelled_id = db.Column(db.Integer)

    def __repr__(self): 
        return '<User {}>'.format(self.username)

class Tweet(db.Model): 
    __tablename__ = "tweets"
    instance_id = db.Column(db.Integer, primary_key=True, index=True)
    tweet_id = db.Column(db.String(128))
    author = db.Column(db.String(64)) 
    text = db.Column(db.String(460)) 
    created_at = db.Column(db.String(256)) 
    language = db.Column(db.String(15)) 
    search_term = db.Column(db.String(64)) 
    dataset_domain = db.Column(db.String(64))
    

class Labels(db.Model):
    __tablename__ = "labels"
    label_id = db.Column(db.Integer, primary_key=True, index=True) 
    user_id = db.Column(db.Integer)
    tweet_id = db.Column(db.Integer)
    sentiment = db.Column(db.Integer)
    reason_for_sentiment = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

class Reason(db.Model): 
    __tablename__ = "reasons"
    reason_id = db.Column(db.Integer, primary_key=True, index=True) 
    reason = db.Column(db.String(128))
    description = db.Column(db.String(1000))
    