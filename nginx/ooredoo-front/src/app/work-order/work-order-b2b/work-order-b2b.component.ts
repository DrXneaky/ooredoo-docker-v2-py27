import { Component, OnInit, ViewContainerRef, ViewChild, ElementRef, } from "@angular/core";
import { WorkOrder, Client, TemplateType, Vendor, WorkOrderType, } from "../work-order-list/work-order-list-config";
import { ValidateRequiredSelect } from "./work-order-b2b-config";
import { FormGroup, FormBuilder, FormControl, Validators, } from "@angular/forms";
import { WorkOrderService } from "src/app/shared/services/work-order.service";
import { ToastrService } from "ngx-toastr";
import { NgbModal, ModalDismissReasons } from "@ng-bootstrap/ng-bootstrap";
import { saveAs } from "file-saver";
import { ReactiveFormsModule, FormsModule } from "@angular/forms";

@Component({
  selector: "ui-work-order-b2b",
  templateUrl: "./work-order-b2b.component.html",
  styleUrls: ["./work-order-b2b.component.scss"],
})
export class WorkOrderB2bComponent implements OnInit {
  @ViewChild("content") content: ElementRef;
  @ViewChild("content2") content2: ElementRef;

  workOrders: WorkOrder[] = [];
  workOrderFormGroup: FormGroup;
  workOrderFormEdit: FormGroup;
  workOrder: WorkOrder;
  pageNumber = 1;
  pages = 0;

  constructor(
    private formBuilder: FormBuilder,
    private workOrderService: WorkOrderService,
    private toastr: ToastrService,
    private modalService: NgbModal
  ) { }

  ngOnInit() {
    this.getWorkOrders(this.pageNumber);
    this.initFormGroup();
  }

  onSubmit(formGroup: FormGroup) {
    this.workOrderService
      .generateWorkOrders(this.createWorkOrder(formGroup))
      .subscribe(
        (data: WorkOrder) => {
          console.log(data);
          if (data[1]) {
            this.toastr.success(
              data[0]["name"] + ":\nYour Workorder is generated sucesfully"
            );
          } else {
            this.toastr.error("Your Workorder is failed because :" + data[2]);
          }
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
      (isDeleted: boolean) => { },
      (error: any) => {
        this.toastr.error("Editing workorder has been failed!");
      }
    );
    console.log("Creating workorder in progress..");
    this.workOrderService
      .generateWorkOrders(this.createWorkOrder(formGroup))
      .subscribe(
        (data: WorkOrder) => {
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

  createWorkOrder(formGroup: FormGroup): WorkOrder {
    const codeClient = formGroup.get("codeClient").value;
    const vendor = formGroup.get("vendor").value;
    const templateType = formGroup.get("templateType").value;
    const workOrder = new WorkOrder();
    workOrder.name = "WO_" + formGroup.get("codeClient").value + "@SUPPORT_IP";
    workOrder.client = new Client();
    workOrder.client.name = null;
    workOrder.client.code = codeClient;
    workOrder.creationDate = new Date();
    workOrder.type = WorkOrderType.B2B;
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
    return workOrder;
  }

  getWorkOrders(pageNumber: number) {
    this.workOrderService
      .getWorkOrders(pageNumber, 5)
      .subscribe((page: any) => {
        this.workOrders = page.items.data;
        this.pages = page.pages;
      });
  }
  // refactor this code to the b2b componenets
  deleteWorkOrder(id: number) {
    this.workOrderService.deleteWorkorder(id).subscribe(
      (isDeleted: boolean) => {
        this.toastr.success("Your Workorder is deleted sucesfully!");
        this.getWorkOrders(this.pageNumber);
      },
      (error: any) => {
        this.toastr.error("Deleting workorder has been failed!");
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

  // receive event{actionClick} from workorder-list on: put it on events handler eg onActionClick
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
                  console.log("Edit Cnaceled");
                  break;
              }
            },
            (reason) => {
              console.log(this.getDismissReason(reason));
            }
          );
    }
  }

  open(content, workOrder: WorkOrder) {
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
