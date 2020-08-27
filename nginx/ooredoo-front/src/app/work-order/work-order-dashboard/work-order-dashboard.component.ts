import { Component, OnInit } from '@angular/core';
import { NavigationConfig } from 'src/app/shared/components/navigation-card/navigation-card-config';
import { WORKORDERMENU } from './work-order-dashboard-cofig';

@Component({
  selector: 'ui-work-order-dashboard',
  templateUrl: './work-order-dashboard.component.html',
  styleUrls: ['./work-order-dashboard.component.scss']
})
export class WorkOrderDashboardComponent implements OnInit {

  navigationCardItems: NavigationConfig[];

  constructor() { }

  ngOnInit() {
    this.navigationCardItems = WORKORDERMENU.filter(item => item);
  }

}  
