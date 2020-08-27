import { NgModule } from "@angular/core";
import { CommonModule } from "@angular/common";
import { NavigationCardComponent } from "./components/navigation-card/navigation-card.component";
import { RouterModule } from "@angular/router";
import { HttpClientModule } from "@angular/common/http";
import { AuditCardComponent } from "./components/audit-card/audit-card.component";
import { CheckboxComponent } from "./components/checkbox/checkbox.component";
import { MatExpansionModule } from '@angular/material/expansion';
import { MatTreeModule } from '@angular/material/tree';
import { MatIconModule } from '@angular/material/icon';
import { MatButtonModule } from '@angular/material/button';
import { MultiSelectModule } from '@syncfusion/ej2-angular-dropdowns';
import { CheckBoxModule } from '@syncfusion/ej2-angular-buttons';
import { DialogBodyComponent } from './components/dialog-body/dialog-body.component';
import { MatDialogModule } from "@angular/material";
import { PdfViewerComponent } from './components/pdf-viewer/pdf-viewer.component';
import { PdfViewerModule } from 'ng2-pdf-viewer';




@NgModule({
  declarations: [NavigationCardComponent, AuditCardComponent, CheckboxComponent, DialogBodyComponent, PdfViewerComponent],

  imports: [CommonModule,
    RouterModule,
    HttpClientModule,
    MatExpansionModule,
    MatTreeModule,
    MatIconModule,
    MatButtonModule,
    MultiSelectModule,
    CheckBoxModule,
    MatDialogModule,
    PdfViewerModule,
  ],

  exports: [NavigationCardComponent,
    AuditCardComponent,
    MatExpansionModule,
    MatTreeModule,
    CheckboxComponent,
    DialogBodyComponent,
    PdfViewerComponent
  ],

  entryComponents: [DialogBodyComponent],
})
export class SharedModule { }
