import { Injectable } from '@angular/core';
import { HttpRequest, HttpHandler, HttpEvent, HttpInterceptor, HttpResponse, HttpErrorResponse } from '@angular/common/http';
import { Observable } from 'rxjs';
import 'rxjs/add/operator/do';
import { AuthService } from './services/auth.service';
import { $API_URL } from './env';

@Injectable()

export class TokenInterceptor implements HttpInterceptor {
    constructor(private authService: AuthService) { }
    intercept(request: HttpRequest<any>, next: HttpHandler) {
        // add auth header with jwt if user is logged in and request is to api url
        const currentUser = this.authService.currentUserValue;
        const isLoggedIn = currentUser && currentUser.token;
        const isApiUrl = request.url.startsWith($API_URL);

        if (isLoggedIn && isApiUrl && this.authService.isAuthenticated()) {
            request = request.clone({
                setHeaders: {
                    Authorization: `Bearer ${currentUser.token}`
                }
            });
        }
        return next.handle(request);
    }

}
