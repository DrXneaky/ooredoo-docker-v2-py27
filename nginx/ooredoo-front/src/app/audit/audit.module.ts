import { NgModule } from "@angular/core";
import { CommonModule } from "@angular/common";
import { RouterModule } from "@angular/router";
import { AUDITROUTES } from "./audit.routing";
import { HTTP_INTERCEPTORS } from '@angular/common/http';
import { AuditListCronjobsComponent } from "./audit-list-cronjobs/audit-list-cronjobs.component";
import { AuditAddCronjobComponent } from "./audit-add-cronjob/audit-add-cronjob.component";
import { ModalDialogModule } from "ngx-modal-dialog";
import { NgbPaginationModule } from "@ng-bootstrap/ng-bootstrap";
import { MatTooltipModule } from '@angular/material';
import { MatExpansionModule } from '@angular/material/expansion';
import { NgbTooltipModule } from '@ng-bootstrap/ng-bootstrap';
import { SharedModule } from "../shared/shared.module";
import { ReactiveFormsModule, FormsModule } from "@angular/forms";
import { AuditDashboardComponent } from "./audit-dashboard/audit-dashboard.component";
import { AuditRunScriptComponent } from './audit-run-script/audit-run-script.component';
import { AuditListScriptsComponent } from './audit-list-scripts/audit-list-scripts.component';
//import { CheckboxComponent } from '../core/checkbox/checkbox.component';
//import { NestedTreeControl } from '@angular/cdk/tree';
import { MatTreeModule } from '@angular/material/tree';
import { MatIconModule } from '@angular/material/icon';
import { MatButtonModule } from '@angular/material/button';

import { MultiSelectModule } from '@syncfusion/ej2-angular-dropdowns';
import { MultiSelectAllModule } from '@syncfusion/ej2-angular-dropdowns';
import { CheckBoxModule } from '@syncfusion/ej2-angular-buttons';
import { MatCheckboxModule } from '@angular/material/checkbox';
//import { PdfViewerModule } from 'ng2-pdf-viewer';
//import { BrowserModule } from '@angular/platform-browser';

import { TokenInterceptor } from '../shared/token-interceptor';


@NgModule({
  declarations: [
    AuditListCronjobsComponent,
    AuditAddCronjobComponent,
    AuditDashboardComponent,
    AuditRunScriptComponent,
    AuditListScriptsComponent,
  ],
  imports: [
    SharedModule,
    CommonModule,
    RouterModule.forChild(AUDITROUTES),
    ReactiveFormsModule,
    FormsModule,
    ModalDialogModule.forRoot(),
    NgbPaginationModule,
    MatTooltipModule,
    NgbTooltipModule,
    MatExpansionModule,
    MatTreeModule,
    MatButtonModule,
    MatIconModule,
    MultiSelectModule,
    MultiSelectAllModule,
    CheckBoxModule,
    MatCheckboxModule,
    //PdfViewerModule,
    //BrowserModule
  ],
  providers: [
    { provide: HTTP_INTERCEPTORS, useClass: TokenInterceptor, multi: true }
  ],
  exports: [MatExpansionModule, MatTreeModule, MatCheckboxModule],
})
export class AuditModule { }

