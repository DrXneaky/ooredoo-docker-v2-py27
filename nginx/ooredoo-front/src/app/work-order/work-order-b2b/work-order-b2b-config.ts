import { WorkOrder } from '../work-order-list/work-order-list-config';
import { AbstractControl } from '@angular/forms';

export const WORKORDERS: WorkOrder[] = [
    // {
    //     id: 1,
    //     name: 'work order one',
    //     client: {
    //         id: 1,
    //         name: 'ATTIJARI',
    //         code: 'TUN_B377'
    //     },
    //     creationDate: new Date(),
    //     vendor: Vendor.NOKIA,
    //     templateType: TemplateType.NORMAL

    // }
];

export function ValidateRequiredSelect(control: AbstractControl) {
    return control && +control.value === 0  ? { validRequiredSelect: true } : null;
}
