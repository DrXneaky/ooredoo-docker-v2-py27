import { Component, OnInit, ViewChild, ElementRef } from "@angular/core";
import { AuditNavConfig, AuditNestedTreeElements } from "src/app/shared/components/audit-card/audit-card-config";
import { AuditChildNavConfig } from "src/app/shared/components/audit-card/audit-card-config";
import { MatExpansionModule } from '@angular/material/expansion';
import { NestedTreeControl } from '@angular/cdk/tree';
import { MatTreeModule } from '@angular/material/tree';
import { MatTreeNestedDataSource } from '@angular/material/tree';
import { nodeChildrenAsMap } from '@angular/router/src/utils/tree';
import { AuditService } from "src/app/shared/services/audit/audit.service";
import { NgbModal, ModalDismissReasons } from "@ng-bootstrap/ng-bootstrap";
import { ToastrService } from "ngx-toastr";
import { FormGroup, FormBuilder, FormControl, Validators, Form, } from "@angular/forms";
import { ValidateFolder } from "./audit-dashboard-config";



@Component({
  selector: "ui-audit-dashboard",
  templateUrl: "./audit-dashboard.component.html",
  styleUrls: ["./audit-dashboard.component.scss"],
})
export class AuditDashboardComponent implements OnInit {
  @ViewChild("content") content: ElementRef;

  navigationCardItems: AuditNavConfig[];
  navigationCardItems2: AuditNestedTreeElements[];
  navigationCardItems3: AuditNestedTreeElements[];
  childItems: AuditChildNavConfig[];
  treeControl = new NestedTreeControl<AuditNestedTreeElements>(node => node.children);
  dataSource = new MatTreeNestedDataSource<AuditNestedTreeElements>();
  addFormGroup: FormGroup;
  action: String;
  editPath: String;

  constructor(
    private auditService: AuditService,
    private toastr: ToastrService,
    private modalService: NgbModal,
    private formBuilder: FormBuilder
  ) {
    //this.dataSource.data = AUDITMENU2.filter((item) => item);
  }

  ngOnInit() {
    this.getTreeArch();
    this.initFormGroup();
  }

  initFormGroup() {
    this.addFormGroup = this.formBuilder.group({
      itemName: new FormControl("", [Validators.required])
    })
  }

  hasChild = (_: number, node: AuditNestedTreeElements) => !!node.children && node.children.length > 0;

  getDataSource(item: any) {
    let newDataSource = new MatTreeNestedDataSource<AuditNestedTreeElements>();
    let node = [];
    node[0] = item;
    newDataSource.data = node.filter((item) => item);
    return newDataSource;
  }

  getTreeArch() {
    this.auditService.getTreeArch().subscribe(
      (data: AuditNestedTreeElements[]) => {
        this.navigationCardItems2 = this.formatTree(data);
      },
      (error: any) => { })
  }

  formatTree(data: any) {
    let list0 = [];
    let list1 = [];
    let list2 = [];
    let newList2: AuditNestedTreeElements[] = [];
    let newList1: AuditNestedTreeElements[] = [];
    let newList0: AuditNestedTreeElements[] = [];
    for (let item of data) {
      if (item.level == 0) {
        list0.push(item);
      } else if (item.level == 1) {
        list1.push(item);
      } else if (item.level == 2) {
        list2.push(item);
      }
    }
    for (let item of list2) { newList2.push(this.createTreeElements(item, [])); }
    for (let item of list1) { newList1.push(this.createTreeElements(item, newList2)); }
    for (let item of list0) { newList0.push(this.createTreeElements(item, newList1)); }
    return newList0;
  }

  createTreeElements(item: any, newList: any) {
    const treeItem = new AuditNestedTreeElements();
    treeItem.title = item.title;
    //treeItem.path = item.path;
    treeItem.path = item.path;
    treeItem.level = item.level;
    treeItem.children = [];
    for (let child of item.children) {
      for (let kid of newList) {
        if (child == kid.title) {
          treeItem.children.push(kid);
        }
      }
    }
    return treeItem;
  }

  addItem(path: String) {
    this.editPath = path;
    this.action = "add";
    this.openModal(this.content);
  }

  deleteItem(path: String) {
    this.editPath = path;
    this.action = "delete";
    this.openModal(this.content);
  }

  openModal(content: any) {
    this.modalService.open(content, {
      ariaLabelledBy: "modal-basic-title",
      size: "lg",
      centered: true,
    });
  }

  onSubmit(form: FormGroup) {
    const submitted_name = form.get("itemName").value;
    this.editFolder(this.editPath, submitted_name);
    this.modalService.dismissAll();
    form.reset({ itemName: "" });
    this.getTreeArch();
  }

  editFolder(path: String, submitted_name: String) {
    if ((submitted_name == this.get_folder_name(path) && (this.action == 'delete')) || (this.action == 'add')) {
      this.auditService.editFolder(path, submitted_name, this.action).subscribe(
        (data: any) => {
          if (data['response'] == "OK") {
            switch (data['action']) {
              case 'add':
                this.toastr.success(['A Folder was added in the path :', data['path']].join(' '));
                break;
              case 'delete':
                this.toastr.success(["'", data['name'], "'", ' was deleted successfully!'].join(''));
                break;
            }
          } else {
            this.toastr.error(data['response'])
          }
        },
        (error: any) => { }
      );
    } else {
      this.toastr.error("The folder name doesn't match");
    }
  }

  get_folder_name(path: String) {
    const folders = path.split('/');
    const level = folders.length;
    return folders[level - 1];
  }


}
