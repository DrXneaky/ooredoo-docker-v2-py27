import { AbstractControl } from '@angular/forms';

export function ValidateRequiredSelect(control: AbstractControl) {
  return control && +control.value === 0 ? { validRequiredSelect: true } : null;
}

export function ValidateFolder(control: AbstractControl) {
  if (/^[^`#\^*|\\:"<>?/]*/.test(control.value)) {
    return { symbols: true };
  }

  return null;
}

