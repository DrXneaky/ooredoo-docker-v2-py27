import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { UserComponent } from './user/user.component';
import { RouterModule } from '@angular/router';
import { RBACROUTES } from './rbac.routing';
import { ReactiveFormsModule, FormsModule } from '@angular/forms';
import { UserListComponent } from './user-list/user-list.component';
import { NgbPaginationModule } from '@ng-bootstrap/ng-bootstrap';

@NgModule({
  declarations: [UserComponent, UserListComponent],
  imports: [
    CommonModule,
    ReactiveFormsModule,
    FormsModule,
    RouterModule.forChild(RBACROUTES),
    NgbPaginationModule,
  ]
})
export class RbacModule { }
