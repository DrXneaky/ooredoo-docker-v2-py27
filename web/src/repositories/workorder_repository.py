from ..entities.work_order import WorkOrder
from ..entities.client import Client
from ..entities.service import Service
import datetime
from sqlalchemy_pagination import paginate

def get_work_orders(session, page, size):
    # workorder_worders = session.query(WorkOrder).all()
    # workorder_worders = session.query(WorkOrder).order_by(WorkOrder.creationDate.desc()).limit(5).all()
    pagination = paginate(session.query(WorkOrder).order_by(WorkOrder.creationDate.desc()), int(page), int(size))
    return pagination

def generate_work_order(session, workorder_to_save, services):
    services_to_save = []
    if workorder_to_save["client"]["name"] is None:
        workorder_to_save["client"]["name"] = ""
    for service in services:
        service_to_save  = Service(service['vrf_id'], service['vrf_name'], service['description'], service['qos'])
        services_to_save.append(service_to_save)
    print(services_to_save)
    client = Client(workorder_to_save["client"]["name"], workorder_to_save["client"]["code"], services_to_save)
    if workorder_to_save["creationDate"] is None:
        workorder_to_save["creationDate"] = datetime.datetime.now().strftime("%Y-%m-%d")
    work_order = WorkOrder(workorder_to_save["name"], workorder_to_save["creationDate"], workorder_to_save["vendor"], workorder_to_save["templateType"], client)
    session.add(work_order)
    session.commit()

def fetch_work_order(session, workorder_to_fetch):
    print(workorder_to_fetch)
    query_fetch_workorder= session.query(WorkOrder).filter(WorkOrder.id == workorder_to_fetch)
    fetched_work_order = query_fetch_workorder.all()
    print(fetched_work_order)
    return fetched_work_order

def delete_work_order(session, id):
    print(id)
    delete_work_order= session.query(WorkOrder).filter(WorkOrder.id == id).first()
    session.delete(delete_work_order)
    session.commit()
    print(delete_work_order)

