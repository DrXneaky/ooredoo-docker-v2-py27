import { Component, OnInit, ViewChild, ViewEncapsulation, ElementRef } from '@angular/core';
import { FormGroup, FormBuilder, FormControl, Validators, Form, } from "@angular/forms";
import { ValidateRequiredSelect } from "./audit-run-script-config";
import { ActivatedRoute } from '@angular/router';
import { AuditService } from "src/app/shared/services/audit/audit.service";
import { Script } from "../audit-list-scripts/audit-list-scripts-config";
import { NgbModal, ModalDismissReasons } from "@ng-bootstrap/ng-bootstrap";
import { MatDialog, MatDialogConfig } from "@angular/material";
import { ToastrService } from "ngx-toastr";
import { DeviceService } from 'src/app/shared/services/device.service';
import { AuthService } from 'src/app/shared/services/auth.service';
import { DialogBodyComponent } from 'src/app/shared/components/dialog-body/dialog-body.component';
//import { MultiSelectComponent } from '@syncfusion/ej2-angular-dropdowns';
//import { CheckBoxComponent } from '@syncfusion/ej2-angular-buttons';
//import { CheckboxComponent } from '../../core/checkbox/checkbox.component';


@Component({
  selector: 'nao-audit-run-script',
  templateUrl: './audit-run-script.component.html',
  styleUrls: ['./audit-run-script.component.scss']
})
export class AuditRunScriptComponent implements OnInit {
  @ViewChild("contentDevices") contentDevices: ElementRef;
  @ViewChild("contentReport") contentReport: ElementRef;
  @ViewChild("contentPdf") contentPdf: ElementRef;


  ScriptFormGroup: FormGroup;
  scriptType: String;
  scriptList: Array<any> = [];
  scripts: Array<any> = [];
  public reportBody = "";
  modalBody: Array<any> = [];
  modalHeader: String;
  //script: any;
  devices: String[] = [];
  selectedDevices: String[] = [];
  pageNumber = 1;
  pages = 0;
  displayedPath: String = "";
  path: String = "";
  fileToUpload: File = null;
  // Checkbox variables
  popHeight: String = "300px";
  checkWaterMark: string = "Select Devices";
  checkFields: Object = { text: 'hostname', value: 'hostname', groupBy: 'vendor' }; //add groupBy:'vendor'
  enableGroupCheckBox: boolean = true;
  label: String = "Devices*";
  filterPlaceholder: String = "Search Devices..";
  // pdf-viewer variables
  pdf_filename: String = "";
  constructor(
    private formBuilder: FormBuilder,
    private route: ActivatedRoute,
    private auditService: AuditService,
    private modalService: NgbModal,
    private deviceService: DeviceService,
    private authService: AuthService,
    private toastr: ToastrService,
    private dialog: MatDialog,
  ) { }

  ngOnInit() {
    this.initFormGroup();
    this.displayedPath = this.route.snapshot.params['folder'];
    if (this.route.snapshot.params['subFolder']) {
      this.displayedPath = [this.displayedPath, this.route.snapshot.params['subFolder']].join(' > ');
    }
    if (this.route.snapshot.params['rule']) {
      this.displayedPath = [this.displayedPath, this.route.snapshot.params['rule']].join(' > ');
    }
    this.path = this.displayedPath.split(' > ').join('/');
    this.getScriptNames(this.path);
    this.getAllDevices();
    this.getScripts(this.pageNumber, this.path.split("/").join('_'));
  }

  initFormGroup() {
    this.ScriptFormGroup = this.formBuilder.group({
      scriptName: new FormControl(0, Validators.compose([ValidateRequiredSelect])),
      deviceType: new FormControl("All", Validators.compose([ValidateRequiredSelect])),
      device: new FormControl(0),
    });
  }

  getScriptNames(path: String) {
    this.auditService.getScriptNames(path).subscribe(
      (data: any) => {
        this.scriptList = data;
      }
    );
  }

  getAllDevices() {
    this.deviceService.getAllDevices().subscribe((data: any) => {
      this.devices = data;
    });
  }

  getDevicesFromType(type: any) {
    this.deviceService.getDevicesFromType(type).subscribe((data: any) => {
      this.devices = data;
    });
  }

  onSelectChange(value: String) {
    if (value == 'All') {
      this.getAllDevices();
    } else {
      this.getDevicesFromType(value);
    }
  }

  getScripts(pageNumber: number, type: String) {
    this.auditService.getScripts(pageNumber, 5, type).subscribe((page: any) => {
      this.scripts = page.items.data;
      console.log(this.scripts);
      this.pages = page.pages;
    });
  }

  onSubmit(formGroup: FormGroup) {
    this.auditService.generateScript(this.createScript(formGroup)).subscribe(
      (data: any) => {
        if (data.status == "Success") {
          this.toastr.success("Your script was executed successfully!");
        } else {
          this.toastr.error("An error has ocurred while executing your script.");
        }
      },
      (error: any) => {
        if (error.status == 422) {
          this.authService.doLogout();
        }
      }
    );
    this.getScripts(this.pageNumber, this.path.split("/").join('_'));
    formGroup.reset({ scriptName: 0, deviceType: "All", device: 0, });
  }

  createScript(formGroup: FormGroup) {
    const script = new Script();
    script.creationDate = new Date();
    script.scriptName = formGroup.get("scriptName").value;
    script.deviceType = formGroup.get("deviceType").value;
    //script.target = formGroup.get("target").value;
    //script.device = formGroup.get("device").value;
    script.devices = this.selectedDevices;
    script.scriptType = this.path.split("/").join('_');
    //console.log(script);
    return script;
  }
  //triggered when clicking on action buttons (run, report, device) in the script table 
  onActionClick(event: any) {
    console.log("event", event.action);
    this.modalBody = [];
    switch (event.action) {
      //open modal and show report: status and errors (if any)
      case "REPORT":
        this.modalHeader = "Report";
        this.reportBody = event.script.report;
        this.openDialog()
        break;
      //run the script (in case it was unsuccessful the first time) -> script table is refreshed after
      case "RUN":
        this.runScript(event.script);
        this.getScripts(this.pageNumber, this.path.split("/").join('_'));
        break;
      //open modal and show the devices where the script was executed
      case "DEVICE":
        this.modalBody = event.script.devices;
        this.modalHeader = "Device details";
        this.modalService.open(this.contentDevices, {
          ariaLabelledBy: "modal-basic-title",
          size: "lg",
          centered: true,
        });
        break;
      //Open PDF viewer
      case "PDF":
        console.log('open pdf viewer');
        this.modalHeader = "PDF Viewer";
        this.pdf_filename = this.path.split("/").join('+') + '+' + event.script.scriptName;
        //console.log(this.pdf_filename);
        //pdf viewer
        /* this.modalService.open(this.contentPdf, {
          ariaLabelledBy: "modal-basic-title",
          size: "lg",
          centered: true,
        }); */
        //idsplay log
        this.reportBody = event.script.log;
        this.openDialog()

        break;
    }
  }

  openDialog() {
    const dialogConfig = new MatDialogConfig();
    dialogConfig.disableClose = true;
    dialogConfig.autoFocus = true;

    dialogConfig.data = {
      report: this.reportBody
    };
    this.dialog.open(DialogBodyComponent, dialogConfig);
  }


  runScript(script: any) {
    console.log(script);
    this.auditService.runScript(script).subscribe(
      (data: any) => {
        console.log(data);
        if (data.status == "Success") {
          this.toastr.success("Your script was executed successfully!");
        } else {
          this.toastr.error("An error has ocurred while executing your script.");
        }
      }, (error: any) => {
        if (error.status == 422) {
          this.authService.doLogout();
        }
      }
    );
  }

  onPageChange(page: number) {
    this.pageNumber = page;
    this.getScripts(this.pageNumber, this.path.split("/").join('_'));
  }





  // Upload scripts 
  handleFileInput(files: FileList) {
    this.fileToUpload = files.item(0);
  }
  UploadFileToActivity(url: String) {
    try {
      this.auditService.postFile(this.fileToUpload, this.path.split("/").join('_'), url).subscribe(data => {
        this.toastr.success(data['response']);
      }, error => {
        this.toastr.error(error);
        console.log(error);
      });
      this.getScriptNames(this.path);
    } catch (error) {
      if (error instanceof TypeError) {
        this.toastr.error("Please choose a file before uploading");
      }
    }
  }
  OnMultiSelectChange(eventValues: []) {
    console.log(eventValues);
    this.selectedDevices = eventValues;
  }


}


