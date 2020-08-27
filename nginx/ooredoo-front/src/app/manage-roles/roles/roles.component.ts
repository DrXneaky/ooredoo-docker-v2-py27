import { Component, OnInit, ViewChild, ElementRef } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { Role } from 'src/app/authentication/role';
import { RoleService } from 'src/app/shared/services/role.service';
import { NgbModal, ModalDismissReasons } from '@ng-bootstrap/ng-bootstrap';

@Component({
  selector: 'nao-roles',
  templateUrl: './roles.component.html',
  styleUrls: ['./roles.component.scss']
})
export class RolesComponent implements OnInit {
  @ViewChild('content') content: ElementRef;

  registerForm: FormGroup;
  loading = false;
  error: string; success: string; failed: string;
  message: string;
  roles: Role[];
  role: Role;
  constructor(private formBuilder: FormBuilder,
    private roleService: RoleService,
    private modalService: NgbModal) { }

  ngOnInit() {
    this.registerForm = this.formBuilder.group({
      name: ['', Validators.required],
      description: ['', Validators.required]
    });

    this.getRole();
  }
  // convenience getter for easy access to form fields
  get f() { return this.registerForm.controls; }

  createRole(formGroup: FormGroup): Role {
    const name = formGroup.get('name').value;
    const description = formGroup.get('description').value;
    const role = new Role();
    role.name = name;
    role.description = description;
    return role;
  }

  onSubmit(formGroup: FormGroup) {
    // stop here if form is invalid
    if (this.registerForm.invalid) {
      return;
    }

    this.roleService.register(this.createRole(formGroup))
      .subscribe(
        (data) => {
          if (data["status"] === "success") {
            this.success = "su";
            formGroup.reset({
              name: '',
              description: ''
            });
            this.getRole();
          }
          else {
            this.failed = "failed"
          }
          this.message = data["message"]
          this.loading = false;
        },
        error => {
          this.error = error;
          this.loading = false;
        });
  }


  getRole() {
    this.roleService.getRoles().subscribe(
      data => {
        this.roles = data;
      },
      error => { this.error = error; }
    )
  }
  deleteRole(id: number) {
    this.roleService.deleteRole(id).subscribe((isDeleted: boolean) => {
      console.log('Your role is deleted sucesfully!');
      console.log(isDeleted)
      this.getRole();
    },
      (error: any) => {
        console.log('Deleting role has been failed!');
      });
  }
  // receive event{actionClick} from workorder-list on: put it on events handler eg onActionClick
  onActionClick(event: any) {
    switch (event.action) {

      case 'DELETE':
        this.role = event.role;
        console.log(event);

        this.open(this.content, event.role);
        break;
    }
  }
  open(content, role: Role) {
    this.modalService.open(content, { ariaLabelledBy: 'modal-basic-title', size: 'lg' }).result.then((result) => {
      switch (result) {
        case 'CONFIRM':
          console.log(role);
          this.deleteRole(role.id);
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
