import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';
import { Role } from 'src/app/authentication/role';

@Component({
  selector: 'nao-role-lists',
  templateUrl: './role-lists.component.html',
  styleUrls: ['./role-lists.component.scss']
})
export class RoleListsComponent implements OnInit {
@Input() roles : Role []
@Output() actionClick: EventEmitter<any> = new EventEmitter<any>();

  constructor() { }

  ngOnInit() {
  }

  onClick(action: string, role: Role): void {
    
    this.actionClick.emit({ action, role });
  }

}
