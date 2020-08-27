interface Log {
  sendMail: Boolean;
  logFile: Boolean;
}

export class CronJob {
  id: number;
  creationDate: Date;
  command: String;
  //minute: String;
  //hour: String;
  //day: String;
  //month: String;
  //weekDay: String;
  type: String;
  expression: String;
  cronSchedule: String;
  lastRun: Date;
  status: String;
  nextRun: Date;
  log: Log;
  description: String;
  /* lastRun: Date;
  nextRun: Date;
  status: String; */
}

export enum Type {
  PROTOCOLS = "Protocols",
  PEERING_RULES = "Peering Rules",
  QOS = "QoS",
  OTHER_FEATURES = "Other features",
}
