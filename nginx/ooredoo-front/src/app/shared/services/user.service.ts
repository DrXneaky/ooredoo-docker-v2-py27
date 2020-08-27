import { Injectable } from '@angular/core';
import { $API_URL } from '../env';
import { HttpClient } from '@angular/common/http';
import { User } from '../user';

@Injectable({
  providedIn: 'root'
})
export class UserService {

  constructor(private http: HttpClient) { }
  register(user: User) {
    return this.http.post(`${$API_URL}register`, user);
  }
  getUsers() {
    return this.http.get(`${$API_URL}users`)
  }

  deleteUsers() {
    return this.http.delete(`${$API_URL}delete-users`)
  }

  deleteUser(id: number) {
    return this.http.delete($API_URL + 'delete-user/' + id)
  }

}
