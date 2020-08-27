import { Component, OnInit, Input, Output, EventEmitter } from "@angular/core";
import { CronJob } from "./audit-list-cronjobs-config";
import {
  FormGroup,
  FormBuilder,
  FormControl,
  Validators,
} from "@angular/forms";


@Component({
  selector: "ui-audit-list-cronjobs",
  templateUrl: "./audit-list-cronjobs.component.html",
  styleUrls: ["./audit-list-cronjobs.component.scss"],
})
export class AuditListCronjobsComponent implements OnInit {
  @Input() cronJobs: CronJob[];
  @Input() pages = 0;
  @Output() actionClick: EventEmitter<any> = new EventEmitter<any>();
  @Output() pageChange: EventEmitter<number> = new EventEmitter<number>();
  page = 1;
  filterFormGroup: FormGroup;
  constructor() { }

  ngOnInit() { }

  onClick(action: string, cronJob: CronJob): void {
    this.actionClick.emit({ action, cronJob });
  }

  onPageChange(page: number) {
    this.pageChange.emit(page);
  }
}
