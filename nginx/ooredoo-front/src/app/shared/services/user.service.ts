import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { User } from '../user';
import { environment } from '../../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class UserService {

  $API_URL = environment.API_URL;

  constructor(private http: HttpClient) { }
  register(user: User) {
    return this.http.post(`${this.$API_URL}register`, user);
  }
  getUsers() {
    return this.http.get(`${this.$API_URL}users`)
  }

  deleteUsers() {
    return this.http.delete(`${this.$API_URL}delete-users`)
  }

  deleteUser(id: number) {
    return this.http.delete(this.$API_URL + 'delete-user/' + id)
  }

}
