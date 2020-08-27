import { Injectable } from '@angular/core';
import { CanActivate, ActivatedRouteSnapshot, RouterStateSnapshot, UrlTree } from '@angular/router';
import { Observable } from 'rxjs';
import { AuthService } from '../services/auth.service';

@Injectable({
  providedIn: 'root'
})
export class CheckAdminGuard implements CanActivate {
  constructor(private authService: AuthService) { }
  canActivate(next: ActivatedRouteSnapshot, state: RouterStateSnapshot) {
    const currentUser = this.authService.currentUserValue;
    if (currentUser.role.name == "Admin") {
      console.log("role", currentUser.role.name);
      return true;
    } else {
      return false;
    }
  }
}
