import {
  Component,
  OnInit,
  ViewContainerRef,
  ViewChild,
  ElementRef,
} from "@angular/core";
import {
  WorkOrderRadio,
  Client,
  TemplateType,
  Vendor,
} from "../work-order-list/work-order-list-config";
import { ValidateRequiredSelect } from "./work-order-radio-config";
import {
  FormGroup,
  FormBuilder,
  FormControl,
  Validators,
} from "@angular/forms";
import { WorkOrderRadioService } from "src/app/shared/services/work-order-radio.service";
import { ToastrService } from "ngx-toastr";
import { NgbModal, ModalDismissReasons } from "@ng-bootstrap/ng-bootstrap";
import { saveAs } from "file-saver";

@Component({
  selector: "ui-work-order-radio",
  templateUrl: "./work-order-radio.component.html",
  styleUrls: ["./work-order-radio.component.scss"],
})
export class WorkOrderRadioComponent implements OnInit {
  @ViewChild("content") content: ElementRef;
  @ViewChild("content2") content2: ElementRef;

  workOrders: WorkOrderRadio[] = [];
  workOrderFormGroup: FormGroup;
  workOrderFormEdit: FormGroup;
  workOrder: WorkOrderRadio;
  pageNumber = 1;
  pages = 0;
  constructor(
    private formBuilder: FormBuilder,
    private workOrderService: WorkOrderRadioService,
    private toastr: ToastrService,
    private modalService: NgbModal
  ) {}

  ngOnInit() {
    this.getWorkOrders(this.pageNumber);
    this.initFormGroup();
  }
  onSubmit(formGroup: FormGroup) {
    this.workOrderService
      .generateWorkOrders(this.createWorkOrder(formGroup))
      .subscribe(
        (data: WorkOrderRadio) => {
          this.toastr.success(
            data[0]["name"] + ":\nYour Workorder is generated sucesfully"
          );
          this.getWorkOrders(this.pageNumber);
          formGroup.reset({
            codeClient: "",
            vendor: 0,
            templateType: 0,
          });
        },
        (error: any) => {
          this.toastr.error(":Your Workorder is failed");
        }
      );
  }

  onSubmitEdit(formGroup: FormGroup) {
    console.log("Deleting workorder in progress..");
    this.workOrderService.deleteWorkorder(this.workOrder.id).subscribe(
      (isDeleted: boolean) => {},
      (error: any) => {
        this.toastr.error("Editing workorder has been failed!");
      }
    );
    console.log("Creating workorder in progress..");
    this.workOrderService
      .generateWorkOrders(this.createWorkOrder(formGroup))
      .subscribe(
        (data: WorkOrderRadio) => {
          console.log("this is data");
          console.log(data);
          this.toastr.success(
            data[0]["name"] + ":\nYour Workorder is Edited sucesfully"
          );
          this.getWorkOrders(this.pageNumber);
          formGroup.reset({
            codeClient: "",
            vendor: 0,
            templateType: 0,
          });
        },
        (error: any) => {
          this.toastr.error(":Your Workorder is failed");
        }
      );
    this.modalService.dismissAll("CONFIRM");
  }

  initFormGroup() {
    this.workOrderFormGroup = this.formBuilder.group({
      codeClient: new FormControl("", [
        Validators.required,
        Validators.pattern("^[A-Z]{3}_[A-Z0-9-]{0,}"),
      ]),
      vendor: new FormControl(0, Validators.compose([ValidateRequiredSelect])),
      templateType: new FormControl(
        0,
        Validators.compose([ValidateRequiredSelect])
      ),
    });

    this.workOrderFormEdit = this.formBuilder.group({
      codeClient: new FormControl("", [
        Validators.required,
        Validators.pattern("^[A-Z]{3}_[A-Z0-9-]{0,}"),
      ]),
      vendor: new FormControl(0, Validators.compose([ValidateRequiredSelect])),
      templateType: new FormControl(
        0,
        Validators.compose([ValidateRequiredSelect])
      ),
    });
  }

  changeFormGroup(formGroup: FormGroup, workorder: WorkOrderRadio) {
    formGroup.setValue({
      codeClient: workorder.client.code,
      vendor: 0,
      templateType: 0,
    });
  }

  createWorkOrder(formGroup: FormGroup): WorkOrderRadio {
    const codeClient = formGroup.get("codeClient").value;
    const vendor = formGroup.get("vendor").value;
    const templateType = formGroup.get("templateType").value;
    const workOrder = new WorkOrderRadio();
    workOrder.name = "WO_" + formGroup.get("codeClient").value + "@SUPPORT_IP";
    workOrder.client = new Client();
    workOrder.client.name = null;
    workOrder.client.code = codeClient;
    workOrder.creationDate = new Date();
    if (templateType === "1") {
      workOrder.templateType = TemplateType.NORMAL;
    } else if (templateType === "2") {
      workOrder.templateType = TemplateType.DUAL_HOMING;
    } else if (templateType === "3") {
      workOrder.templateType = TemplateType.MCLAG;
    } else {
      workOrder.templateType = null;
    }
    if (vendor === "2") {
      workOrder.vendor = Vendor.CISCO;
    } else if (vendor === "3") {
      workOrder.vendor = Vendor.HUAWEI;
    } else if (vendor === "1") {
      workOrder.vendor = Vendor.NOKIA;
    } else if (vendor === "4") {
      workOrder.vendor = Vendor.SIAE;
    } else {
      workOrder.vendor = null;
    }
    console.log(workOrder);
    return workOrder;
  }

  getWorkOrders(pageNumber: number) {
    this.workOrderService
      .getWorkOrders(pageNumber, 5)
      .subscribe((page: any) => {
        console.log(page.items.data);
        this.workOrders = page.items.data;
        this.pages = page.pages;
      });
  }

  deleteWorkOrder(id: number) {
    this.workOrderService.deleteWorkorder(id).subscribe(
      (isDeleted: boolean) => {
        this.toastr.success("Your Workorder is deleted successfully!");
        this.getWorkOrders(this.pageNumber);
      },
      (error: any) => {
        this.toastr.error("Deleting workorder has failed!");
      }
    );
  }

  downloadWorkOrder(filename: string) {
    this.workOrderService.downloadWorkorder(filename).subscribe(
      (res) => {
        let blob = new Blob([res], { type: "application/txt" });
        saveAs(blob, filename + ".txt");
      },
      (error) => console.log("Error downloading the file")
    );
  }

  onActionClick(event: any) {
    switch (event.action) {
      case "DELETE":
        this.workOrder = event.workOrder;
        console.log(this.workOrder);
        console.log("delete content");
        console.log(this.content);
        this.open(this.content, event.workOrder);
        break;

      case "EXPORT":
        this.workOrder = event.workOrder;
        this.downloadWorkOrder(this.workOrder.name + ".txt");
        break;

      case "EDIT":
        console.log("EDIT", event.workOrder.id);
        this.workOrder = event.workOrder;
        this.changeFormGroup(this.workOrderFormEdit, this.workOrder);
        this.modalService
          .open(this.content2, {
            ariaLabelledBy: "modal-basic-title",
            size: "lg",
            centered: true,
          })
          .result.then(
            (result) => {
              switch (result) {
                case "CANCEL":
                  console.log("Edit has been Canceled");
                  break;
              }
            },
            (reason) => {
              console.log(this.getDismissReason(reason));
            }
          );
    }
  }

  open(content, workOrder: WorkOrderRadio) {
    this.modalService
      .open(content, { ariaLabelledBy: "modal-basic-title", size: "lg" })
      .result.then(
        (result) => {
          switch (result) {
            case "CONFIRM":
              console.log("delete");
              this.deleteWorkOrder(workOrder.id);
              break;
            default:
              break;
          }
        },
        (reason) => {
          console.log(this.getDismissReason(reason));
        }
      );
  }

  private getDismissReason(reason: any): string {
    if (reason === ModalDismissReasons.ESC) {
      return "by pressing ESC";
    } else if (reason === ModalDismissReasons.BACKDROP_CLICK) {
      return "by clicking on a backdrop";
    } else {
      return `with: ${reason}`;
    }
  }

  onPageChange(page: number) {
    this.pageNumber = page;
    this.getWorkOrders(this.pageNumber);
  }
}
