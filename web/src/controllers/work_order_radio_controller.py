from src.entities.work_order_radio import WorkOrderRadioSchema
from src.repositories.workorder_radio_repository import get_work_orders, fetch_work_order, delete_work_order
#from src.repositories.workorder_repository import edit_work_order
import json


def get_work_orders_schema(session, page, size):
    schema = WorkOrderRadioSchema(many=True)
    # page = schema.dumps(get_work_orders(session, page, size))
    page = get_work_orders(session, page, size)
    page.items = schema.dump(page.items)
    return page.__dict__


def fetch_work_orders_schema(session, workorder_to_fetch):
    schema = WorkOrderRadioSchema(many=True)
    workorder_worders = schema.dump(fetch_work_order(session, workorder_to_fetch))
    print(workorder_worders)
    return workorder_worders.data


def delete_work_orders_schema(session,id):
    schema = WorkOrderRadioSchema(many=True)
    schema.dump(delete_work_order(session, id))