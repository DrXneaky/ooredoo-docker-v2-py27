import { NgModule } from "@angular/core";
import { Routes } from "@angular/router";
import { CollectDashboardComponent } from "./collect-dashboard/collect-dashboard.component";

export const COLLECTROUTES: Routes = [
  {
    path: "",
    children: [
      {
        path: "dashboard",
        component: CollectDashboardComponent,
        data: {
          title: "Collect Dashboard",
          urls: [
            { title: "Dashboard", url: "/dashboard" },
            { title: "Audit Dashboard" },
          ],
        },
      },
    ],
  },
];
