import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { SigninComponent } from './signin/signin.component';
import { RouterModule } from '@angular/router';
import { AUTHENTICATIONROUTES } from './authentication.routing';
import { ReactiveFormsModule, FormsModule } from '@angular/forms';
import { HTTP_INTERCEPTORS } from '@angular/common/http';
import { TokenInterceptor } from '../shared/token-interceptor';


@NgModule({
  declarations: [SigninComponent],
  imports: [
    ReactiveFormsModule,
    FormsModule,
    CommonModule,
    RouterModule.forChild(AUTHENTICATIONROUTES),
  ],
  providers:[ { provide: HTTP_INTERCEPTORS, useClass: TokenInterceptor, multi: true },]
})
export class AuthenticationModule { }
