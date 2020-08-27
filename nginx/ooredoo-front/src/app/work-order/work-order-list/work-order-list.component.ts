import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';
import { WorkOrder } from './work-order-list-config';

@Component({
  selector: 'ui-work-order-list',
  templateUrl: './work-order-list.component.html',
  styleUrls: ['./work-order-list.component.scss']
})
export class WorkOrderListComponent implements OnInit {
  @Input() workOrders: WorkOrder[];
  @Input() pages = 0;
  @Output() actionClick: EventEmitter<any> = new EventEmitter<any>();
  @Output() pageChange: EventEmitter<number> = new EventEmitter<number>();
  page = 1;
  constructor() { }

  ngOnInit() {
  }

  onClick(action: string, workOrder: WorkOrder): void {
    this.actionClick.emit({ action, workOrder });
  }

  onPageChange(page: number) {
    this.pageChange.emit(page);
    console.log(page);
  }
}
