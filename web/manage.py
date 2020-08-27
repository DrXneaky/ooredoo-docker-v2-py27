
from src.entities.device import Device
from src.repositories.entity import Base, Session, engine
#sys.path.append("C:/Users/Ahmed/Desktop/ooredoo on docker-nginx flask gunicorn postgres/web")
from run import app
import click


@app.cli.command("create_db")
def create_db():
    Base.metadata.create_all(bind=engine)
    click.echo('db created')


@app.cli.command("init_db")
def init_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    click.echo('db intialized')

def create_db_fn():
    Base.metadata.create_all(bind=engine)
    click.echo('db created')

#@app.cli.command("add_device")
def add_device():
    session = Session()
    new_device = Device("9422", "172.65.112.13", "3")
    session.add(new_device)
    session.commit()
    session.close()
    click.echo('device added')


