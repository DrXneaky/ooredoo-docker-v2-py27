import { Component, OnInit, ViewChild, ElementRef } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { UserService } from 'src/app/shared/services/user.service';
import { User } from 'src/app/shared/user';
import { Role } from 'src/app/authentication/role';
import { RoleService } from 'src/app/shared/services/role.service';
import { NgbModal, ModalDismissReasons } from '@ng-bootstrap/ng-bootstrap';
import { Observable } from 'rxjs';
import { AuthService } from 'src/app/shared/services/auth.service';

@Component({
  selector: 'nao-user',
  templateUrl: './user.component.html',
  styleUrls: ['./user.component.scss']
})
export class UserComponent implements OnInit {
  @ViewChild('content') content: ElementRef;
  registerForm: FormGroup;
  loading = false;
  submitted = false;
  error: string;
  //roles: Role[] = [];
  public roles = [];
  success: string;
  failed: string;
  message: string;
  users: User[];
  user: User;


  constructor(private formBuilder: FormBuilder,
    private modalService: NgbModal, private router: Router, private userService: UserService, private role: RoleService, private authService: AuthService) { }

  ngOnInit() {
    this.registerForm = this.formBuilder.group({
      fullName: ['', Validators.required],
      email: ['', Validators.required],
      password: ['', [Validators.required, Validators.minLength(6)]],
      role: [0]
    });

    this.getRole();
    this.getUsers();
  }

  createUser(formGroup: FormGroup): User {
    const fullName = formGroup.get('fullName').value;
    const email = formGroup.get('email').value;
    const password = formGroup.get('password').value;
    const ro = formGroup.get('role').value;
    const user = new User();
    user.name = fullName;
    user.email = email;
    user.password = password;
    user.creationDate = new Date();
    user.role = ro;
    /* user.role = new Role();
    var fetchedRole = this.roles.filter(
      roe => roe["name"] === ro);

    user.role.id = fetchedRole["id"];
    user.role.name = fetchedRole["name"];
    user.role.description = fetchedRole["description"]; */
    return user;
  }

  // convenience getter for easy access to form fields
  get f() { return this.registerForm.controls; }
  onSubmit(formGroup: FormGroup) {
    this.submitted = true;
    // stop here if form is invalid
    if (this.registerForm.invalid) {
      return;
    }
    this.loading = true;
    console.log(this.createUser(formGroup));
    this.userService.register(this.createUser(formGroup))
      .subscribe(
        (data) => {
          if (data["status"] === "success") {
            this.success = "su";
            formGroup.reset({
              fullName: '',
              email: '',
              role: 0,
              password: ''
            });
            this.getUsers();
          }
          else {
            this.failed = "failed"
          }
          this.message = data["message"]
          this.loading = false;

          // this.router.navigate(['/login'], { queryParams: { registered: true } });
        },
        error => {
          this.error = error;
          this.loading = false;
        });
  }


  getUsers() {
    this.userService.getUsers().subscribe((user: User[]) => {
      this.users = user;
      console.log(this.users);
    });
  }

  getRole() {
    this.role.getRoles().subscribe(
      data => {
        console.log("data roles", data);
        this.roles = data;
        return data;
      },
      error => {
        this.error = error;
        console.log(2);
        return [];
      }
    );
  }

  deleteUser(id: number) {
    this.userService.deleteUser(id).subscribe((isDeleted: boolean) => {
      if (this.authService.currentUserValue.id == id) {
        this.authService.doLogout();
      } else {
        this.getUsers();
      }
    },
      (error: any) => {
        console.log('Deleting User has failed!');
      });
  }
  onActionClick(event: any) {
    switch (event.action) {

      case 'DELETE':
        this.user = event.user;

        this.open(this.content, event.user);
        break;
    }
  }
  open(content, user: User) {
    this.modalService.open(content, { ariaLabelledBy: 'modal-basic-title', size: 'lg' }).result.then((result) => {
      switch (result) {
        case 'CONFIRM':
          this.deleteUser(user.id);
          break;
        default:
          break;
      }
    }, (reason) => {
      console.log(this.getDismissReason(reason));
    });
  }
  private getDismissReason(reason: any): string {
    if (reason === ModalDismissReasons.ESC) {
      return 'by pressing ESC';
    } else if (reason === ModalDismissReasons.BACKDROP_CLICK) {
      return 'by clicking on a backdrop';
    } else {
      return `with: ${reason}`;
    }
  }
}
