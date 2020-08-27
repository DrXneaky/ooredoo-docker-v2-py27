import { NgModule } from "@angular/core";
import { CommonModule } from "@angular/common";
import { WorkOrderB2bComponent } from "./work-order-b2b/work-order-b2b.component";
import { WorkOrderRadioComponent } from "./work-order-radio/work-order-radio.component";
import { WorkOrderDashboardComponent } from "./work-order-dashboard/work-order-dashboard.component";
import { WorkOrderListComponent } from "./work-order-list/work-order-list.component";
import { RouterModule } from "@angular/router";
import { WORKORDERROUTES } from "./work-order.routing";
import { SharedModule } from "../shared/shared.module";
import { ReactiveFormsModule, FormsModule } from "@angular/forms";
import { WorkOrderDetailComponent } from "./work-order-detail/work-order-detail.component";
import { ModalDialogModule } from "ngx-modal-dialog";
import { NgbPaginationModule } from "@ng-bootstrap/ng-bootstrap";
import { WorkOrderAdvancedComponent } from "./work-order-advanced/work-order-advanced.component";
import { WorkOrderRadioDetailComponent } from "./work-order-radio-detail/work-order-radio-detail.component";
import { WorkOrderRadioListComponent } from "./work-order-radio-list/work-order-radio-list.component";

@NgModule({
  declarations: [
    WorkOrderB2bComponent,
    WorkOrderRadioComponent,
    WorkOrderDashboardComponent,
    WorkOrderListComponent,
    WorkOrderDetailComponent,
    WorkOrderAdvancedComponent,
    WorkOrderRadioDetailComponent,
    WorkOrderRadioListComponent,
  ],
  imports: [
    CommonModule,
    SharedModule,
    ReactiveFormsModule,
    FormsModule,
    RouterModule.forChild(WORKORDERROUTES),
    ModalDialogModule.forRoot(),
    NgbPaginationModule,
  ],
})
export class WorkOrderModule {}
