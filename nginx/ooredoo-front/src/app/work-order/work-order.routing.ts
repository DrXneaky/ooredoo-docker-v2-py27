import { WorkOrderDashboardComponent } from "./work-order-dashboard/work-order-dashboard.component";
import { WorkOrderB2bComponent } from "./work-order-b2b/work-order-b2b.component";
import { WorkOrderRadioComponent } from "./work-order-radio/work-order-radio.component";
import { Routes } from "@angular/router";
import { WorkOrderDetailComponent } from "./work-order-detail/work-order-detail.component";
import { WorkOrderAdvancedComponent } from "./work-order-advanced/work-order-advanced.component";

export const WORKORDERROUTES: Routes = [
  {
    path: "",
    children: [
      {
        path: "work-order-dashboard",
        component: WorkOrderDashboardComponent,
        data: {
          title: "Workorder Dashboard",
          urls: [
            { title: "Dashboard", url: "/dashboard" },
            {
              title: "Workorder Dashboard",
              url: "/work-order/work-order-dashboard",
            },
          ],
        },
      },
      {
        path: "work-order-b2b",
        component: WorkOrderB2bComponent,
        data: {
          title: "Generate Workorder B2B",
          urls: [
            { title: "Dashboard", url: "/dashboard" },
            {
              title: "Workorder Dashboard",
              url: "/work-order/work-order-dashboard",
            },
            { title: "Generate Workorder B2B" },
          ],
        },
      },
      {
        path: "work-order-radio",
        component: WorkOrderRadioComponent,
        data: {
          title: "Generate Workorder Radio",
          urls: [
            { title: "Dashboard", url: "/dashboard" },
            {
              title: "Workorder Dashboard",
              url: "/work-order/work-order-dashboard",
            },
            { title: "Generate Workorder Radio" },
          ],
        },
      },
      {
        path: "work-order-advanced",
        component: WorkOrderAdvancedComponent,
        data: {
          title: "Generate Workorder Advanced",
          urls: [
            { title: "Dashboard", url: "/dashboard" },
            {
              title: "Workorder Dashboard",
              url: "/work-order/work-order-dashboard",
            },
            { title: "Generate Workorder Advanced" },
          ],
        },
      },
      {
        path: "work-order-detail/:id",
        component: WorkOrderDetailComponent,
        data: {
          title: "Workorder Detail",
          urls: [
            { title: "Dashboard", url: "/dashboard" },
            {
              title: "Workorder Dashboard",
              url: "/work-order/work-order-dashboard",
            },
            { title: "Workorder Detail" },
          ],
        },
      },
    ],
  },
];
