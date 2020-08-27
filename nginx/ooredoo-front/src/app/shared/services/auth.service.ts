import { Injectable } from "@angular/core";
import { User } from "../user";
import { $API_URL } from '../env';
import { BehaviorSubject, Observable } from 'rxjs';
import { map } from 'rxjs/operators';
import { HttpClient, HttpHeaders, HttpErrorResponse } from '@angular/common/http';
import { Router } from '@angular/router';
//import { JwtHelper } from 'angular2-jwt';
import { JwtHelperService } from '@auth0/angular-jwt'

const httpOptions = {
  headers: new HttpHeaders({
    "Content-Type": "application/json",
    Authorization: "my-auth-token",
  }),
};
@Injectable({
  providedIn: "root",
})
export class AuthService {
  private currentUserSubject: BehaviorSubject<User>;
  public currentUser: Observable<User>;

  constructor(private http: HttpClient, public router: Router) {
    this.currentUserSubject = new BehaviorSubject<User>(JSON.parse(localStorage.getItem('currentUser')));
    this.currentUser = this.currentUserSubject.asObservable();
  }

  public get currentUserValue() {
    return this.currentUserSubject.value;
  }

  register(user: User) {
    return this.http.post<any>($API_URL + "register", user).subscribe(
      (res: any) => {
        if (res["response"]) {
          console.log("User added successfully");
        }
      },
      (error: any) => {
        console.log(error);
      }
    );
  }

  public isAuthenticated(): boolean {
    let token = this.getToken();
    //console.log('token: ', token);
    let jwtHelper = new JwtHelperService();
    let expirationDate = jwtHelper.getTokenExpirationDate(token);
    //console.log('expiration date', expirationDate);
    //console.log('expired?', jwtHelper.isTokenExpired(token));
    if (token == null || jwtHelper.isTokenExpired(token)) {
      return false;
    }
    return true;
  }

  get isLoggedIn(): boolean {
    let authToken = localStorage.getItem('token');
    return authToken !== null ? true : false;
  }

  doLogout() {
    console.log('logout');
    let removeToken = localStorage.removeItem('token');
    let removeUser = localStorage.removeItem('currentUser');
    this.router.navigate(["/auth/signin"]);
  }

  login(user: User) {
    return this.http.post<any>($API_URL + 'login', user, httpOptions)
      .pipe(map(user => {
        // login successful if there's a jwt token in the response
        if (user && user.token) {
          // store user details and jwt token in local storage to keep user logged in between page refreshes
          localStorage.setItem('token', user.token);
          localStorage.setItem('currentUser', JSON.stringify(user));
          this.currentUserSubject.next(user);
        }
        return user;
      }));
  }

  getToken() {
    return localStorage.getItem('token');
  }

  getUserRoleFromToken() {
    return this.currentUserValue.role.name;
  }

}
