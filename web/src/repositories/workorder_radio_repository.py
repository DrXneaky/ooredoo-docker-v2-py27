from ..entities.work_order_radio import WorkOrderRadio
from ..entities.client import Client
from ..entities.service import Service
import datetime
from sqlalchemy_pagination import paginate

def get_work_orders(session, page, size):
    # workorder_worders = session.query(WorkOrder).all()
    # workorder_worders = session.query(WorkOrder).order_by(WorkOrder.creationDate.desc()).limit(5).all()

    pagination = paginate(session.query(WorkOrderRadio).order_by(WorkOrderRadio.creationDate.desc()), int(page), int(size))
    return pagination


def generate_work_order(session, workorder_to_save, services):

  #add code here

  return True

def fetch_work_order(session, workorder_to_fetch):
    print(workorder_to_fetch)
    query_fetch_workorder= session.query(WorkOrderRadio).filter(WorkOrderRadio.id == workorder_to_fetch)
    fetched_work_order = query_fetch_workorder.all()
    print(fetched_work_order)
    return fetched_work_order


def delete_work_order(session, id):
    print(id)
    delete_work_order= session.query(WorkOrderRadio).filter(WorkOrderRadio.id == id).first()
    session.delete(delete_work_order)
    session.commit()
    print(delete_work_order)