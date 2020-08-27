import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { CollectDashboardComponent } from './collect-dashboard/collect-dashboard.component';
import { RouterModule } from "@angular/router";
import { COLLECTROUTES } from "./collect.routing";

@NgModule({
  declarations: [CollectDashboardComponent],
  imports: [
    CommonModule,
    RouterModule.forChild(COLLECTROUTES),
  ]
})
export class CollectModule { }
