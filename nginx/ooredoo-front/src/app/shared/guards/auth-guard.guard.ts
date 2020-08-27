import { Injectable } from '@angular/core';
import { ActivatedRouteSnapshot, RouterStateSnapshot, UrlTree, Router, CanActivate } from '@angular/router';
import { Observable } from 'rxjs';
import { AuthService } from '../services/auth.service';
import { tokenKey } from '@angular/core/src/view';

@Injectable({
  providedIn: 'root'
})
export class AuthGuardGuard implements CanActivate {
  constructor(private router: Router, private authService: AuthService) { }


  canActivate(route: ActivatedRouteSnapshot, state: RouterStateSnapshot) {
    const currentUser = this.authService.currentUserValue;
    //console.log("canActivate");
    if (currentUser && this.authService.isAuthenticated()) {
      // logged in so return true
      return true;
    }
    else {
      console.log('currentuser:', currentUser);
      console.log('is authenticated:', this.authService.isAuthenticated());
      // not logged in so redirect to login page with the return url and return false
      console.log('local storage cleared');
      localStorage.removeItem('currentUser');
      localStorage.removeItem('token');
      this.router.navigate(['/auth/signin'], { queryParams: { returnUrl: state.url } });
      return true;
    }
  }
}

