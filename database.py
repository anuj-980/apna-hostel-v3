from flask_pymongo import pymongo
from dotenv import load_dotenv
import os

load_dotenv()

CONNECTION_STR = os.getenv("CONNECTION_STRING")
client = pymongo.MongoClient(CONNECTION_STR)

# Database Name
db = client["data"]
 
# Collection Name
tabdata = db["tabdata"]
signin = db["signin"]
admin = db["admin"]
bridge_slip = db["bridge_slip"]
pass_slip = db["pass_slip"]

def counter(doc_name):
  c = []
  result = doc_name.find()
  for i in result:
    c.append(i)
  return len(c)

def load_signin():
  
  users = signin.find()
  user = []
  for i in users:
    i["_id"] = str(i["_id"])
    user.append(i)
  return user


def load_user(id):
  result = signin.find_one({"id": int(id)})
  return result
  
 

def load_admin(id):
  result = admin.find_one({'id': int(id)})
  return result

def do_signup(details):
  c = counter(signin) + 1
  data = {"email": details['email'],"username": details['name'],"pass": details['pass'],"id": c}
  signin.insert_one(data)
    
  return

def load_admins():
  
  ad = admin.find()

  return ad

def check_admin(data):
  admins = load_admins()

  for j in admins:
    if data['email'] == j['ad_email'] and data['pass'] == j['ad_pass']:
      admin=j['id']
      return admin
      break
  else:
    return 0

def check_user(data):
  users = load_signin()
  
  for i in users:
    if data['email'] == i['email'] and data['pass'] == i['pass']:
      user=i['id']
      return user
      break
  else:
    return 0


def put_slip_request(details):
  c = counter(bridge_slip) + 1
  id = details[0]
  data = details[1]
  qry_data = {"id": id,"std_name": data['std_name'],"place": data['place'],"address": data['address'],"time_go": data['time_go'],"time_in": data['time_in'],"hostel_name": data['hostel_name'],"clg_name": data['clg_name'],"room_no": data['room_no'],"slip_id": c}
  bridge_slip.insert_one(qry_data)
  
  slip = bridge_slip.find_one({'id': int(id)})

  slip_id = slip['slip_id']
  return slip_id

def load_slip(s_id):
  
  result = bridge_slip.find({'slip_id':int(s_id)})
  return result

def load_bridge_slip():
  
  slips = bridge_slip.find()

  return slips

def passed_slip(passed_list,reject_list):
    
  for i in passed_list:
    qry = bridge_slip.find({'slip_id': int(i)})
    pass_slip.insert_many(qry)
    bridge_slip.delete_one({'slip_id': int(i)})

  for j in reject_list:
    bridge_slip.delete_one({'slip_id': int(j)})
    
    
  return

def load_pass_slip(id):
    
  slips = pass_slip.find({"id": int(id)})

  return slips

def load_data():

  user = tabdata.find()

  return user