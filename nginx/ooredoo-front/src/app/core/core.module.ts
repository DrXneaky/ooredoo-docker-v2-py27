import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { NavBarComponent } from './nav-bar/nav-bar.component';
import { SideBarComponent } from './side-bar/side-bar.component';
import { FooterComponent } from './footer/footer.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { MainLayoutComponent } from './main-layout/main-layout.component';
import { BlankLayoutComponent } from './blank-layout/blank-layout.component';
import { BreadCrumbComponent } from './bread-crumb/bread-crumb.component';
import { RouterModule } from '@angular/router';
import { PerfectScrollbarConfigInterface, PERFECT_SCROLLBAR_CONFIG, PerfectScrollbarModule } from 'ngx-perfect-scrollbar';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';


const DEFAULT_PERFECT_SCROLLBAR_CONFIG: PerfectScrollbarConfigInterface = {
  suppressScrollX: true,
  wheelSpeed: 2,
  wheelPropagation: true,
};

@NgModule({
  imports: [
    CommonModule,
    RouterModule,
    PerfectScrollbarModule,
    NgbModule,
  ],
  declarations: [
    NavBarComponent,
    SideBarComponent,
    FooterComponent,
    DashboardComponent,
    MainLayoutComponent,
    BlankLayoutComponent,
    BreadCrumbComponent],
  exports: [
    NavBarComponent,
    SideBarComponent,
    FooterComponent,
    DashboardComponent,
    MainLayoutComponent,
    BlankLayoutComponent,
    BreadCrumbComponent],
  providers: [
    {
      provide: PERFECT_SCROLLBAR_CONFIG,
      useValue: DEFAULT_PERFECT_SCROLLBAR_CONFIG
    }]
})
export class CoreModule { }
