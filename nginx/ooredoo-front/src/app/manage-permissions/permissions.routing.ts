
import { Routes } from '@angular/router';
import { PermissionsComponent } from './permissions/permissions.component';


export const PERMISSIONSROUTES: Routes = [
    {
        path: '',
        children: [
            {
                path: 'perm',
                component: PermissionsComponent,
                data: {
                    title: 'Manage Permissions',
                    urls: [{ title: 'permissions', url: '/perm' }, { title: 'manage pemissions' }]
                }
            }
        ]
    }
];
