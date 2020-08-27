import { Component, OnInit } from "@angular/core";
import { WorkOrderRadio } from "../work-order-list/work-order-list-config";
import { WorkOrderRadioService } from "src/app/shared/services/work-order-radio.service";
import { ActivatedRoute } from "@angular/router";

@Component({
  selector: "ui-work-order-radio-detail",
  templateUrl: "./work-order-radio-detail.component.html",
  styleUrls: ["./work-order-radio-detail.component.scss"],
})
export class WorkOrderRadioDetailComponent implements OnInit {
  workorder: WorkOrderRadio;

  constructor(
    private route: ActivatedRoute,
    private workOrderRadioService: WorkOrderRadioService
  ) {}

  ngOnInit() {
    console.log(this.route.snapshot.params["id"]);
    //console.log(this.route.snapshot.params["type"]);
    this.fetchWorkOrderDetail(+this.route.snapshot.params["id"]);
    // this.workorderDetails = copyWorkOrder(WORKORDERDEATAILS);
  }

  fetchWorkOrderDetail(id: number) {
    this.workOrderRadioService
      .fetchWorkorderDetail(id)
      .subscribe((workorderDetail: WorkOrderRadio) => {
        this.workorder = workorderDetail[0];
        console.log("list", this.workorder);
      });
  }
}
