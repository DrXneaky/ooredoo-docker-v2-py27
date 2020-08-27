import { Injectable } from '@angular/core';
import { HttpClient, HttpEvent, HttpErrorResponse, HttpEventType } from '@angular/common/http';
import { map } from 'rxjs/operators';
import { $API_URL } from "../env"

@Injectable({
  providedIn: 'root'
})
export class UploadService {
  SERVER_URL: string = $API_URL;
  constructor(private httpClient: HttpClient) { }

  public upload(formData) {

    return this.httpClient.post<any>(this.SERVER_URL, formData, {
      reportProgress: true,
      observe: 'events'
    });
  }
}
