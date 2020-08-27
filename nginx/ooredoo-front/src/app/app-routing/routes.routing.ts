import { Routes } from "@angular/router";
import { MainLayoutComponent } from "../core/main-layout/main-layout.component";
import { DashboardComponent } from "../core/dashboard/dashboard.component";
import { BlankLayoutComponent } from "../core/blank-layout/blank-layout.component";
import { CheckAdminGuard } from "../shared/guards/check-admin.guard";
import { AuthChildGuard } from "../shared/guards/auth-child.guard";

export const routes: Routes = [
  {
    path: '',
    component: BlankLayoutComponent,
    children: [
      { path: '', redirectTo: '/auth/signin', pathMatch: 'full' },
      {
        path: 'auth', loadChildren: '../authentication/authentication.module#AuthenticationModule'
      }
    ]
  },
  {
    path: "",
    component: MainLayoutComponent,
    canActivateChild: [AuthChildGuard],
    children: [
      { path: "dashboard", component: DashboardComponent },
      {
        path: "work-order",
        loadChildren: "../work-order/work-order.module#WorkOrderModule",
      },
      {
        path: "devices",
        loadChildren: "../devices/devices.module#DevicesModule",
      },
      {
        path: "users",
        canActivate: [CheckAdminGuard],
        loadChildren: "../rbac/rbac.module#RbacModule"
      },
      {
        path: "perm",
        canActivate: [CheckAdminGuard],
        loadChildren:
          "../manage-permissions/manage-permissions.module#ManagePermissionsModule",
      },
      {
        path: "roles",
        canActivate: [CheckAdminGuard],
        loadChildren: "../manage-roles/manage-roles.module#ManageRolesModule",
      },
      {
        path: "audit",
        loadChildren: "../audit/audit.module#AuditModule"
      },
      {
        path: "collect",
        loadChildren: "../collect/collect.module#CollectModule"
      },
    ],
  },
  {
    path: "**",
    redirectTo: "404",
  },
];
