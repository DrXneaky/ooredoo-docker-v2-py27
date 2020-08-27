import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PermissionsComponent } from './permissions/permissions.component';
import { RouterModule } from '@angular/router';
import { PERMISSIONSROUTES } from './permissions.routing';

@NgModule({
  declarations: [PermissionsComponent],
  imports: [
    CommonModule,
    RouterModule.forChild(PERMISSIONSROUTES)
  ]
})
export class ManagePermissionsModule { }
