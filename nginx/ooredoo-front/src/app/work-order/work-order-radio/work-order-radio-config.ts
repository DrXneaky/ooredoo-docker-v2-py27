import { WorkOrder } from "../work-order-list/work-order-list-config";
import { AbstractControl } from "@angular/forms";

export const WORKORDERS: WorkOrder[] = [];

export function ValidateRequiredSelect(control: AbstractControl) {
  return control && +control.value === 0 ? { validRequiredSelect: true } : null;
}
