import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { ROUTES, RouteInfo } from './route-info';
import { AuthService } from 'src/app/shared/services/auth.service';
declare var $: any;
@Component({
  selector: 'ui-side-bar',
  templateUrl: './side-bar.component.html',
  styleUrls: ['./side-bar.component.scss']
})
export class SideBarComponent implements OnInit {


  showMenu = '';
  showSubMenu = '';
  public sidebarnavItems: RouteInfo[];

  constructor(
    private authService: AuthService,
    private modalService: NgbModal,
    private router: Router,
    private route: ActivatedRoute) {
  }
  // End open close
  ngOnInit() {
    this.sidebarnavItems = ROUTES.filter(sidebarnavItem => sidebarnavItem);
    if (this.authService.currentUserValue.role.name == 'Admin') {
      this.sidebarnavItems[4].disabled = false;
    } else {
      this.sidebarnavItems[4].disabled = true;
    }
    $(function () {
      $('.sidebartoggler').on('click', function () {
        if ($('#main-wrapper').hasClass('mini-sidebar')) {
          $('body').trigger('resize');
          $('#main-wrapper').removeClass('mini-sidebar');

        } else {
          $('body').trigger('resize');
          $('#main-wrapper').addClass('mini-sidebar');
        }
      });

    });

  }

  // this is for the open close
  addExpandClass(element: any) {
    if (element === this.showMenu) {
      this.showMenu = '0';

    } else {
      this.showMenu = element;
    }
  }
  addActiveClass(element: any) {
    if (element === this.showSubMenu) {
      this.showSubMenu = '0';

    } else {
      this.showSubMenu = element;
    }
  }

}
