
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { WorkOrder } from 'src/app/work-order/work-order-list/work-order-list-config';
import { HttpHeaders } from '@angular/common/http';
import { environment } from '../../../environments/environment';
//import { ResponseContentType, RequestOptions} from '@angular/http';


const httpOptions = {
  headers: new HttpHeaders({
    'Content-Type': 'application/json',
    'Authorization': 'my-auth-token'
  })
};
@Injectable({
  providedIn: 'root'
})
export class WorkOrderService {

  $API_URL = environment.API_URL;

  constructor(private http: HttpClient) { }

  getWorkOrders(page: number, size: number): Observable<any> {
    return this.http.get<any>(this.$API_URL + 'work-orders/' + page + '/' + size);
  }

  generateWorkOrders(workWorder: WorkOrder): Observable<WorkOrder> {
    return this.http.post<WorkOrder>(this.$API_URL + 'generate-work-order', workWorder, httpOptions);
  }

  fetchWorkorderDetail(id: number) {
    //return this.http.post<WorkOrder>($API_URL +'work-order-detail', id, httpOptions);
    return this.http.get<any>(this.$API_URL + 'work-order-detail/' + id);
  }

  deleteWorkorder(id: number): Observable<any> {
    return this.http.delete<any>(this.$API_URL + 'delete-work-order/' + id);
  }

  downloadWorkorder(filename: string) {
    const headers = new HttpHeaders({ 'Content-Type': 'application/txt' });
    //console.log(this.http.get('http://localhost:5000/download/'+filename, { headers, responseType:'blob' }).subscribe(res => {
    //let blob = new Blob([res],{type:'application/txt'});
    //}));
    return this.http.get(this.$API_URL + 'download/' + filename, { headers, responseType: 'blob' });
  }

}

