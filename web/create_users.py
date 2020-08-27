from src.repositories.entity import Session
from src.entities.user import User
from src.entities.role import Role
from src.repositories.role_repository import fetch_role
from datetime import datetime

session = Session()
try:
    user = session.query(User).filter(User.email == 'ip@ooredoo.tn').first()
    if not user:
        role = fetch_role(session, 'admin')
        cDate = datetime.now()
        user = User('test', 'ip@ooredoo.tn', '123456', cDate, role)
        session.add(user)
        session.commit()
        session.close()
except Exception as e:
    print(str(e))
