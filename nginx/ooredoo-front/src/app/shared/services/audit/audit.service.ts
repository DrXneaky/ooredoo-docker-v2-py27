import { Injectable } from "@angular/core";
import { HttpClient } from "@angular/common/http";
import { Observable } from "rxjs";
import { HttpHeaders } from "@angular/common/http";
import { CronJob } from "src/app/audit/audit-list-cronjobs/audit-list-cronjobs-config";
import { AuditNestedTreeElements } from "src/app/shared/components/audit-card/audit-card-config";
import { $API_URL } from '../../env';
import { $ } from 'protractor';

const httpOptions = {
  headers: new HttpHeaders({
    "Content-Type": "application/json",
    Authorization: "my-auth-token",
  }),
};

@Injectable({
  providedIn: "root",
})
export class AuditService {
  constructor(private http: HttpClient) { }

  generateCronJob(cronJob: CronJob): Observable<CronJob> {
    return this.http.post<CronJob>(
      $API_URL + "generate-cron-job",
      cronJob,
      httpOptions
    );
  }

  convertCronJob(cronJob: CronJob): Observable<CronJob> {
    return this.http.post<CronJob>(
      $API_URL + "convert-cron-job",
      cronJob,
      httpOptions
    );
  }

  getCronJobs(page: number, size: number): Observable<any> {
    return this.http.get<any>(
      $API_URL + "cron-jobs/" + page + "/" + size
    );
  }

  getScriptNames(path: any): Observable<any> {
    return this.http.post<any>(
      $API_URL + "get-script-names",
      { "path": path },
      httpOptions
    );
  }

  getScripts(page: number, size: number, type: String): Observable<any> {
    return this.http.get<any>(
      $API_URL + "get-scripts/" + type + "/" + page + "/" + size
    );
  }

  generateScript(script: any): Observable<any> {
    return this.http.post<any>(
      $API_URL + "generate-script",
      script,
      httpOptions
    );
  }

  runScript(script: any): Observable<any> {
    return this.http.post<any>(
      $API_URL + "run-script",
      script,
      httpOptions
    );
  }

  getTreeArch(): Observable<AuditNestedTreeElements[]> {
    return this.http.get<AuditNestedTreeElements[]>(
      $API_URL + 'get-script-tree-arch'
    );
  }

  editFolder(path: String, name: String, action: String): Observable<any> {
    return this.http.post<any>(
      $API_URL + 'edit-script-folder',
      {
        "path": path,
        "name": name,
        "action": action
      },
      httpOptions
    );
  }

  postFile(fileToUpload: File, path: String): Observable<boolean> {
    console.log(path.split("/").join('_'));
    const endpoint = $API_URL + 'upload-script/' + path;
    const formData: FormData = new FormData();
    formData.append('uploadFile', fileToUpload, fileToUpload.name);
    let headers = new HttpHeaders();
    headers.append('Content-Type', 'multipart/form-data');
    headers.append('Accept', 'application/json');
    let options = { headers: headers };
    return this.http.post<any>(endpoint, formData, options);
    /*       .map(() => { return true; })
          .catch((e) => this.handleError(e)); */
  }

}
