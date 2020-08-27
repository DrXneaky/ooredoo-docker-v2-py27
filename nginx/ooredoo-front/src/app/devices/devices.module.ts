import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { DevicesDashboardComponent } from './devices-dashboard/devices-dashboard.component';
import { RouterModule } from '@angular/router';
import { DEVICESROUTES } from './devices.routing';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { DevicesListComponent } from './devices-list/devices-list.component';
import { NgbPaginationModule } from '@ng-bootstrap/ng-bootstrap';

@NgModule({
  declarations: [DevicesDashboardComponent, DevicesListComponent],
  imports: [
    CommonModule,
    FormsModule,
    ReactiveFormsModule,
    RouterModule.forChild(DEVICESROUTES),
    NgbPaginationModule
  ]
})
export class DevicesModule { 
 

}
