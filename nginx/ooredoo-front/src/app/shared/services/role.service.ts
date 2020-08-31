import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';
import { Role } from 'src/app/authentication/role';

import { environment } from '../../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class RoleService {

  $API_URL = environment.API_URL;

  constructor(private http: HttpClient) { }
  getRoles(): Observable<any> {
    return this.http.get<any>(this.$API_URL + '/get_roles');
  }
  register(role: Role) {
    return this.http.post(`${this.$API_URL}register_role`, role);
  }
  deleteRole(id: number): Observable<any> {
    return this.http.delete<any>(this.$API_URL + 'delete-role/' + id);
  }

}
