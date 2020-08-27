import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';
import { Device } from 'src/app/work-order/work-order-list/work-order-list-config';

@Component({
  selector: 'nao-devices-list',
  templateUrl: './devices-list.component.html',
  styleUrls: ['./devices-list.component.scss']
})
export class DevicesListComponent implements OnInit {
  @Input() devices: Device[];
  @Input() pages = 0;
  @Output() actionClick: EventEmitter<any> = new EventEmitter<any>();
  @Output() pageChange: EventEmitter<number> = new EventEmitter<number>();
  page = 1;
  constructor() { }

  ngOnInit() {
  }

  onClick(action: string, device: Device): void {
    this.actionClick.emit({ action, device });
  }

  onPageChange(page: number) {
    this.pageChange.emit(page);
    console.log(page);
  }

}
