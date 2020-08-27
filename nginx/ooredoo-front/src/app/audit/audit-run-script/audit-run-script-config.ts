import { AbstractControl } from '@angular/forms';


export function ValidateRequiredSelect(control: AbstractControl) {
  return control && +control.value === 0 ? { validRequiredSelect: true } : null;
}