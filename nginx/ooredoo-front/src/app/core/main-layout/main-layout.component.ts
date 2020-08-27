import { Component, OnInit } from '@angular/core';
import { PerfectScrollbarConfigInterface } from 'ngx-perfect-scrollbar';
import { Router } from '@angular/router';

@Component({
  selector: 'ui-main-layout',
  templateUrl: './main-layout.component.html',
  styleUrls: ['./main-layout.component.scss']
})
export class MainLayoutComponent implements OnInit {

  color = 'red';
  showSettings = false;
  showMinisidebar = false;
  showDarktheme = false;

  public config: PerfectScrollbarConfigInterface = {};

  constructor(public router: Router) { }

  ngOnInit() {
    if (this.router.url === '/') {
      this.router.navigate(['/dashboard/dashboard1']);
    }
  }

}
