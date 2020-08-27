
import { Routes } from '@angular/router';
import { SigninComponent } from './signin/signin.component';


export const AUTHENTICATIONROUTES: Routes = [
    {
        path: '',
        children: [
            {
                path: 'signin',
                component: SigninComponent,
                data: {
                    title: 'signin',
                    urls: [{ title: 'signin', url: '/signin' }, { title: 'signin' }]
                }
            }
        ]
    },
    {
        path: '',
        children: [
            {
                path: 'register',
                component: SigninComponent,
                data: {
                    title: 'register',
                    urls: [{ title: 'signin', url: '/register' }, { title: 'signin' }]
                }
            }
        ]
    }
];
