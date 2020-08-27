import { Component, OnInit, Input, Output, EventEmitter } from "@angular/core";
import {
  WorkOrder,
  WorkOrderRadio,
} from "../work-order-list/work-order-list-config";
import { WorkOrderRadioService } from "src/app/shared/services/work-order-radio.service";

@Component({
  selector: "ui-work-order-radio-list",
  templateUrl: "./work-order-radio-list.component.html",
  styleUrls: ["./work-order-radio-list.component.scss"],
})
export class WorkOrderRadioListComponent implements OnInit {
  @Input() workOrders: WorkOrderRadio[];
  @Input() pages = 0;
  @Output() actionClick: EventEmitter<any> = new EventEmitter<any>();
  @Output() pageChange: EventEmitter<number> = new EventEmitter<number>();
  pageNumber = 1;
  workOrderRadio: WorkOrderRadio;
  page = 1;
  constructor() { }

  ngOnInit() {
    //+this.getWorkOrders(this.pageNumber);
    //this.initFormGroup();
  }

  onClick(action: string, workOrder: WorkOrder): void {
    this.actionClick.emit({ action, workOrder });
  }

  onPageChange(page: number) {
    /* this.pageChange.emit(page);
    console.log(page); */
    this.pageNumber = page;
    //this.getWorkOrders(this.pageNumber);
  }
}
