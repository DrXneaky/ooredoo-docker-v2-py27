import { Component, OnInit } from '@angular/core';
import { WorkOrder } from '../work-order-list/work-order-list-config';
import { copyWorkOrder, WORKORDERDEATAILS } from './work-order-detail-config';
import { WorkOrderService } from 'src/app/shared/services/work-order.service';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'ui-work-order-detail',
  templateUrl: './work-order-detail.component.html',
  styleUrls: ['./work-order-detail.component.scss']
})
export class WorkOrderDetailComponent implements OnInit {

  /**
   * 
   */
  workorder: WorkOrder;


  constructor(
    private route: ActivatedRoute, 
    private workOrderService: WorkOrderService) { }

  ngOnInit() {
    console.log(this.route.snapshot.params['id']);
    this.fetchWorkOrderDetaill(+this.route.snapshot.params['id']);
    // this.workorderDetails = copyWorkOrder(WORKORDERDEATAILS);
  }

  fetchWorkOrderDetaill(id: number) {
    this.workOrderService.fetchWorkorderDetail(id).subscribe((workorderDetail: WorkOrder) => {
      this.workorder = workorderDetail[0];
      console.log('list', this.workorder);
    });
  }

}
