import { Injectable } from "@angular/core";
import { HttpClient } from "@angular/common/http";
import { Observable } from "rxjs";
import { WorkOrder } from "src/app/work-order/work-order-list/work-order-list-config";
import { HttpHeaders } from "@angular/common/http";

import { $API_URL } from "../env"

const httpOptions = {
  headers: new HttpHeaders({
    "Content-Type": "application/json",
    Authorization: "my-auth-token",
  }),
};

@Injectable({
  providedIn: "root",
})
export class WorkOrderRadioService {
  constructor(private http: HttpClient) { }

  getWorkOrders(page: number, size: number): Observable<any> {
    return this.http.get<any>(
      $API_URL + "work-orders-radio/" + page + "/" + size
    );
  }

  generateWorkOrders(workWorder: WorkOrder): Observable<WorkOrder> {
    return this.http.post<WorkOrder>(
      $API_URL + 'generate-work-order-radio',
      workWorder,
      httpOptions
    );
  }

  fetchWorkorderDetail(id: number) {
    //return this.http.post<WorkOrder>('http://172.0.0.1:5000/work-order-detail', id, httpOptions);
    return this.http.get<any>(
      $API_URL + "work-order-radio-detail/" + id
    );
  }

  deleteWorkorder(id: number): Observable<any> {
    return this.http.delete<any>(
      $API_URL + "delete-work-order-radio/" + id
    );
  }

  downloadWorkorder(filename: string) {
    const headers = new HttpHeaders({ "Content-Type": "application/txt" });
    //console.log(this.http.get('http://172.0.0.1:5000/download/'+filename, { headers, responseType:'blob' }).subscribe(res => {
    //let blob = new Blob([res],{type:'application/txt'});
    //}));
    return this.http.get($API_URL + "download-radio/" + filename, {
      headers,
      responseType: "blob",
    });
  }
}
