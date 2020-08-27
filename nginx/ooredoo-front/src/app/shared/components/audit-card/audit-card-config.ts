export interface AuditNavConfig {
  title: String;
  description: String;
  children: AuditChildNavConfig[];
}

export interface AuditChildNavConfig {
  title: String;
  description: String;
  path: String;
  disabled: Boolean;
}

export class AuditNestedTreeElements {
  title: String;
  path: String;
  level: Number;
  children: AuditNestedTreeElements[];
}