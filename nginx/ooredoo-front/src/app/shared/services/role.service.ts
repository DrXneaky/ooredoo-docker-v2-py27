import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { $API_URL } from '../env';
import { HttpClient } from '@angular/common/http';
import { Role } from 'src/app/authentication/role';

@Injectable({
  providedIn: 'root'
})
export class RoleService {

  constructor(private http: HttpClient) { }
  getRoles(): Observable<any> {
    return this.http.get<any>($API_URL + '/get_roles');
  }
  register(role: Role) {
    return this.http.post(`${$API_URL}register_role`, role);
  }
  deleteRole(id: number): Observable<any> {
    return this.http.delete<any>($API_URL + 'delete-role/' + id);
  }

}
