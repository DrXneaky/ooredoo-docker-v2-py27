import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Device } from 'src/app/work-order/work-order-list/work-order-list-config';
import { Observable } from 'rxjs';
import { $API_URL } from '../env';

const httpOptions = {
  headers: new HttpHeaders({
    'Content-Type': 'application/json',
    'Authorization': 'my-auth-token'
  })
};
@Injectable({
  providedIn: 'root'
})
export class DeviceService {

  constructor(private http: HttpClient) { }

  generateDevice(device: Device): Observable<Device> {
    return this.http.post<Device>($API_URL + 'generate-device', device, httpOptions);
  }
  getDevices(page: number, size: number): Observable<any> {
    return this.http.get<any>($API_URL + 'devices/' + page + '/' + size);
  }
  getDevicesFromType(type): Observable<any> {
    return this.http.get<any>($API_URL + 'get-devices-from-type/' + type);
  }
  getAllDevices(): Observable<any> {
    return this.http.get<any>($API_URL + 'devices/');
  }
  uploadDevices(devices: Device[]): Observable<Device> {
    return this.http.post<Device>($API_URL + 'upload-devices', devices, httpOptions);
  }
  editDevice(device: Device): Observable<any> {
    return this.http.post<Device>($API_URL + 'edit-device', device, httpOptions);
  }
  deleteDevice(device: Device): Observable<any> {
    return this.http.post<Device>($API_URL + 'delete-device', device, httpOptions);
  }
}
