import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';
import { UserService } from 'src/app/shared/services/user.service';
import { User } from 'src/app/shared/user';

@Component({
  selector: 'nao-user-list',
  templateUrl: './user-list.component.html',
  styleUrls: ['./user-list.component.scss']
})
export class UserListComponent implements OnInit {
  @Input() users: User[];
  @Output() actionClick: EventEmitter<any> = new EventEmitter<any>();

  constructor(private userService: UserService) { }

  ngOnInit() {
  }
  // onClick(action: string, role: Role): void {

  //   this.actionClick.emit({ action, role });
  // }
  getUsers() {
    this.userService.getUsers().subscribe((user: User[]) => {
      this.users = user;
      console.log(this.users);
    });
  }
  delete() {
    this.userService.deleteUsers().subscribe(data => console.log(data))
    this.getUsers()
  }
  onClick(action: string, user: User): void {

    this.actionClick.emit({ action, user });
  }
}
