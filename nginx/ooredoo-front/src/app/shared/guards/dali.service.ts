/* import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';
import { headers, UrlConfig } from '../shared/config/urlConfig';
import { JwtHelper } from 'angular2-jwt';
import { GlobalAttribute } from "../shared/config/globalAttribute";
import { LoginRequest } from "../shared/model/LoginRequest.model";
@Injectable({
  providedIn: 'root',
})
export class AuthentificationService {
  userIdFromJwtToken: string;
  jwtToken: string;
  private url = UrlConfig;
  constructor(private http: HttpClient,
    private router: Router,) {
  }
  login(loginRequest: LoginRequest) {
    return this.http.post(this.url.loginUrl, loginRequest, {
      observe: 'response',
      headers:
      {
        'Content-Type': 'application/json'
      }
      , responseType: 'json'
    });
  }
  logout() {
    //localStorage.clear();
    localStorage.removeItem(GlobalAttribute.LocalStorageAttribute.TOKEN);
    this.router.navigateByUrl('/');
  }
  saveToken(jwt: string) {
    localStorage.setItem(GlobalAttribute.LocalStorageAttribute.TOKEN, jwt);
    this.router.navigate(['/um'])
  }
  loadToken() {
    this.jwtToken = localStorage.getItem(GlobalAttribute.LocalStorageAttribute.TOKEN);
    return this.jwtToken;
  }
  getUserIdFromJwtToken() {
    this.jwtToken = this.loadToken();
    let jwtHelper = new JwtHelper();
    this.userIdFromJwtToken = jwtHelper.decodeToken(this.jwtToken).sub;
    return this.userIdFromJwtToken;
  }
  isAuthenticated() {
    let token = localStorage.getItem(GlobalAttribute.LocalStorageAttribute.TOKEN);
    let jwtHelper = new JwtHelper();
    if (token == null || jwtHelper.isTokenExpired(token)) {
      return false;
    }
    return true;
  }
}


 */