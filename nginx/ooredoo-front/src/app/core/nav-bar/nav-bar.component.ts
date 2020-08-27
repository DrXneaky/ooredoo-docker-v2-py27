import { Component, OnInit, AfterViewInit } from '@angular/core';
import { PerfectScrollbarConfigInterface } from 'ngx-perfect-scrollbar';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { NOTIFICATIONS, MESSAGES } from './nav-bar-info';
import { AuthService } from 'src/app/shared/services/auth.service';
declare var $: any;

@Component({
  selector: 'ui-nav-bar',
  templateUrl: './nav-bar.component.html',
  styleUrls: ['./nav-bar.component.scss']
})
export class NavBarComponent implements OnInit, AfterViewInit {


  name: string;
  config: PerfectScrollbarConfigInterface = {};
  notifications: any[];
  mymessages: any[];


  constructor(private modalService: NgbModal, private authservice: AuthService) {

  }

  ngOnInit(): void {
    this.notifications = NOTIFICATIONS.filter(notification => notification);
    this.mymessages = MESSAGES.filter(message => message);
  }

  ngAfterViewInit() {

    const set = function() {
      const width = (window.innerWidth > 0) ? window.innerWidth : this.screen.width;
      const topOffset = 0;
      if (width < 1170) {
        $('#main-wrapper').addClass('mini-sidebar');
      } else {
        $('#main-wrapper').removeClass('mini-sidebar');
      }
    };
    $(window).ready(set);
    $(window).on('resize', set);


    $('.search-box a, .search-box .app-search .srh-btn').on('click', function () {
      $('.app-search').toggle(200);
    });


    $('body').trigger('resize');
  }

  logout(){  this.authservice.doLogout();}
}
