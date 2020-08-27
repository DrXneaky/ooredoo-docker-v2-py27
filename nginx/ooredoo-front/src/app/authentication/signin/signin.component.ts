import { Component, OnInit } from "@angular/core";
import {
  FormBuilder,
  FormGroup,
  FormControl,
  Validators,
} from "@angular/forms";
import { User } from "src/app/shared/user";
import { Router, ActivatedRoute } from "@angular/router";
import { first } from 'rxjs/operators';
import { AuthService } from "src/app/shared/services/auth.service";

@Component({
  selector: "nao-signin",
  templateUrl: "./signin.component.html",
  styleUrls: ["./signin.component.scss"],
})
export class SigninComponent implements OnInit {
  returnUrl: string;
  signinFormGroup: FormGroup;
  loading = false;
  error: string;
  loginFailed: String = "";

  constructor(
    private formBuilder: FormBuilder,
    private authService: AuthService,
    private router: Router,
    private route: ActivatedRoute,
  ) {
    if (this.authService.currentUserValue) {
      this.router.navigate(['dashboard']);
    }
  }

  ngOnInit() {
    this.signinFormGroup = this.formBuilder.group({
      userName: new FormControl("", [Validators.required]),
      password: new FormControl("", [Validators.required]),
    });
    this.returnUrl = this.route.snapshot.queryParams['returnUrl'] || '/dashboard';
  }

  onSubmit(formGroup: FormGroup) {
    const userName = formGroup.get("userName").value;
    const password = formGroup.get("password").value;
    var user = new User();
    user.email = userName;
    user.password = password;
    this.loading = true;
    this.authService.login(user)
      .pipe(first())
      .subscribe(
        data => {
          this.loginFailed = "";
          if (data.code == 401) {
            console.log(data.message);
            this.loginFailed = data.message;
            this.resetForm(this.signinFormGroup);
          }
          this.router.navigate([this.returnUrl]);
        },
        error => {
          this.error = error;
          this.loading = false;
        });
  }

  resetForm(formGroup: FormGroup) {
    formGroup.reset();
  }

}
