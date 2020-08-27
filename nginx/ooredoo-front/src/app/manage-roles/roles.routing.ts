
import { Routes } from '@angular/router';
import { RolesComponent } from './roles/roles.component';


export const ROLESROUTES: Routes = [
    {
        path: '',
        children: [
            {
                path: 'roles',
                component: RolesComponent,
                data: {
                    title: 'Manage roles',
                    urls: [{ title: 'Dashboard', url: '/dashboard' }, { title: 'Manage roles' }]
                }
            }
        ]
    }
];

