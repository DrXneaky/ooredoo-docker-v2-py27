import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RolesComponent } from './roles/roles.component';
import { RouterModule } from '@angular/router';
import { ROLESROUTES } from './roles.routing';
import { ReactiveFormsModule } from '@angular/forms';
import { RoleListsComponent } from './role-lists/role-lists.component';

@NgModule({
  declarations: [RolesComponent, RoleListsComponent],
  imports: [
    CommonModule,
    RouterModule.forChild(ROLESROUTES),
    ReactiveFormsModule,
  ]
})
export class ManageRolesModule { }
