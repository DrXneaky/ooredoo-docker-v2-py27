import { Component, OnInit, Input, EventEmitter, Output } from '@angular/core';
import { Script } from './audit-list-scripts-config';

@Component({
  selector: 'nao-audit-list-scripts',
  templateUrl: './audit-list-scripts.component.html',
  styleUrls: ['./audit-list-scripts.component.scss']
})
export class AuditListScriptsComponent implements OnInit {
  @Input() scripts: Script[];
  @Input() pages = 0;
  @Output() actionClick: EventEmitter<any> = new EventEmitter<any>();
  @Output() pageChange: EventEmitter<any> = new EventEmitter<any>();
  page = 1;

  constructor() { }

  ngOnInit() {
  }

  onClick(action: string, script: Script): void {
    this.actionClick.emit({ action, script });
  }

  onPageChange(page: Number) {
    this.pageChange.emit(page);
  }

}
