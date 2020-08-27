import { Routes } from '@angular/router';
import { DevicesDashboardComponent } from './devices-dashboard/devices-dashboard.component';


export const DEVICESROUTES: Routes = [
    {
        path: '',
        children: [
            {
                path: 'devices-dashboard',
                component: DevicesDashboardComponent,
                data: {
                    title: 'Devices Dashboard',
                    urls: [{ title: 'Dashboard', url: '/dashboard' }, { title: 'Devices Dashboard' }]
                      }
            }
           
        ]
    }
];
