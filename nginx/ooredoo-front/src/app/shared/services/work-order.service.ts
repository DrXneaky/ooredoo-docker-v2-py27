
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { WorkOrder } from 'src/app/work-order/work-order-list/work-order-list-config';
import { HttpHeaders } from '@angular/common/http';
import { $API_URL } from '../env';
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

  constructor(private http: HttpClient) { }

  getWorkOrders(page: number, size: number): Observable<any> {
    return this.http.get<any>($API_URL + 'work-orders/' + page + '/' + size);
  }

  generateWorkOrders(workWorder: WorkOrder): Observable<WorkOrder> {
    return this.http.post<WorkOrder>($API_URL + 'generate-work-order', workWorder, httpOptions);
  }

  fetchWorkorderDetail(id: number) {
    //return this.http.post<WorkOrder>($API_URL +'work-order-detail', id, httpOptions);
    return this.http.get<any>($API_URL + 'work-order-detail/' + id);
  }

  deleteWorkorder(id: number): Observable<any> {
    return this.http.delete<any>($API_URL + 'delete-work-order/' + id);
  }

  downloadWorkorder(filename: string) {
    const headers = new HttpHeaders({ 'Content-Type': 'application/txt' });
    //console.log(this.http.get('http://localhost:5000/download/'+filename, { headers, responseType:'blob' }).subscribe(res => {
    //let blob = new Blob([res],{type:'application/txt'});
    //}));
    return this.http.get($API_URL + 'download/' + filename, { headers, responseType: 'blob' });
  }

}

