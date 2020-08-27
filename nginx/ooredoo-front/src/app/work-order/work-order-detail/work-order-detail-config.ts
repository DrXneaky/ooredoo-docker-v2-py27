import {
  WorkOrder,
  Vendor,
  TemplateType,
  Client,
  WorkOrderType,
} from "../work-order-list/work-order-list-config";

export const WORKORDERDEATAILS: WorkOrder = {
  id: 5,
  name: "workorder_attijari",
  creationDate: new Date(),
  vendor: Vendor.NOKIA,
  templateType: TemplateType.NORMAL,
  client: {
    id: 5,
    code: "TUN_B377",
    name: "Attijari Lac",
  },
  services: [
    {
      id: 1,
      name: "hsi",
      qos: 4,
      vprnId: 9500,
    },
    {
      id: 2,
      name: "vpn_attijari",
      qos: 20,
      vprnId: 5240,
    },
  ],
  type: WorkOrderType.B2B,
};

export function copyWorkOrder(origine: WorkOrder): WorkOrder {
  const copy = new WorkOrder();

  copy.id = origine.id;
  copy.name = origine.name;
  copy.templateType = origine.templateType;
  copy.vendor = origine.vendor;
  copy.creationDate = origine.creationDate;
  copy.type = origine.type;
  if (origine.client) {
    copy.client = new Client();
    copy.client.id = origine.client.id;
    copy.client.name = origine.client.name;
    copy.client.code = origine.client.name;
  }
  if (origine.services) {
    copy.services = origine.services.filter((service) => service);
  }
  return copy;
}
