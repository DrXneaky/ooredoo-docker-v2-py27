
import { Routes } from '@angular/router';
import { UserComponent } from './user/user.component';
import { CheckAdminGuard } from "../shared/guards/check-admin.guard";

export const RBACROUTES: Routes = [
    {
        path: '',
        children: [
            {
                path: 'users',
                component: UserComponent,
                data: {
                    title: 'Manage users',
                    urls: [{ title: 'Dashboard', url: '/dashboard' }, { title: 'Manage users' }]
                }
            }
        ]
    }
];
