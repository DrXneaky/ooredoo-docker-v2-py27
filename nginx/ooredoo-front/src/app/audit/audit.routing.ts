import { NgModule } from "@angular/core";
import { Routes } from "@angular/router";
import { AuditListCronjobsComponent } from "./audit-list-cronjobs/audit-list-cronjobs.component";
import { AuditDashboardComponent } from "./audit-dashboard/audit-dashboard.component";
import { AuditAddCronjobComponent } from "./audit-add-cronjob/audit-add-cronjob.component";
import { AuditRunScriptComponent } from "./audit-run-script/audit-run-script.component";
import { AuthChildGuard } from "../shared/guards/auth-child.guard";

export const AUDITROUTES: Routes = [
  {
    path: "",
    children: [
      {
        path: "dashboard",
        component: AuditDashboardComponent,
        data: {
          title: "Audit Dashboard",
          urls: [
            { title: "Dashboard", url: "/dashboard" },
            { title: "Audit Dashboard" },
          ],
        },
      },
      {
        path: "cron-job",
        component: AuditAddCronjobComponent,
        data: {
          title: "Task Scheduler",
          urls: [
            { title: "Dashboard", url: "/dashboard" },
            { title: "Task Scheduler" },
          ],
        },
      },
      {
        path: "script/:folder/:subFolder/:rule",
        component: AuditRunScriptComponent,
        data: {
          title: "Script Manager",
          urls: [
            { title: "Dashboard", url: "/dashboard" },
            { title: "Audit Dashboard", url: "/audit/dashboard" },
            { title: "Script Manager" },
          ],
        },
      },
      {
        path: "script/:folder/:subFolder",
        component: AuditRunScriptComponent,
        data: {
          title: "Script Manager",
          urls: [
            { title: "Dashboard", url: "/dashboard" },
            { title: "Audit Dashboard", url: "/audit/dashboard" },
            { title: "Script Manager" },
          ],
        },
      },
      {
        path: "script/:folder",
        component: AuditRunScriptComponent,
        data: {
          title: "Script Manager",
          urls: [
            { title: "Dashboard", url: "/dashboard" },
            { title: "Audit Dashboard", url: "/audit/dashboard" },
            { title: "Script Manager" },
          ],
        },
      },
    ],
  },
];
