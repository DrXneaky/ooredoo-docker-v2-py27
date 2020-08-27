export class WorkOrder {
  id: number;
  name: string;
  client: Client;
  creationDate: Date;
  vendor: Vendor;
  templateType: TemplateType;
  services?: Service[]; // reafactor in client;
  type: WorkOrderType;
}
export class Device {
  id: number;
  hostname: string;
  ipSystem: string;
  rd: string;
  vendor: Vendor;
}
export class Client {
  id: number;
  name: string;
  code: string;
  // services here!
}

export enum Vendor {
  NOKIA = "NOKIA",
  CISCO = "CISCO",
  HUAWEI = "HUAWEI",
  SIAE = "SIAE",
}

export enum TemplateType {
  NORMAL = "Normal",
  DUAL_HOMING = "Dual Homing",
  MCLAG = "MCLag",
}

export class Service {
  id: number;
  name: string;
  vprnId: number;
  qos: number;
}

export enum WorkOrderType {
  B2B = "B2B",
  RADIO = "Radio",
}

//WORKORDER RADIO : This part will be deleted if the radio workorders have the same structure as B2B.

export class WorkOrderRadio {
  id: number;
  name: string;
  client: Client;
  creationDate: Date;
  vendor: Vendor;
  templateType: TemplateType;
  services?: Service[];
  type: WorkOrderType;
}
