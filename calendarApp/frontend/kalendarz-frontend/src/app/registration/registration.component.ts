import{Component, OnInit}from '@angular/core';
import {Router, ActivatedRoute}from '@angular/router';
import {FormBuilder, FormGroup, Validators}from '@angular/forms';
import {first}from 'rxjs/operators';
import {AuthenticationService}from '../services/authentication.service';

@Component({
selector: 'app-registration',
templateUrl: './registration.component.html',
styleUrls: ['./registration.component.css']
})
export class RegistrationComponent implements OnInit {

registrationForm: FormGroup;
loading = false;
submitted = false;
success = false
error = '';

constructor(
        private formBuilder: FormBuilder,
        private route: ActivatedRoute,
        private router: Router,
        private authenticationService: AuthenticationService)
  {

  }

  ngOnInit(): void {
      this.registrationForm = this.formBuilder.group({
            username: ['', Validators.required],
            email: ['', Validators.required],
            password: ['', Validators.required],
            repeatPassword: ['', Validators.required],
        }, {validator: this.matchingPasswords('password', 'repeatPassword')});
  }

  matchingPasswords(passwordKey: string, confirmPasswordKey: string) {
  return (group: FormGroup) => {
    let password = group.controls[passwordKey];
    let confirmPassword = group.controls[confirmPasswordKey];

    if (password.value !== confirmPassword.value) {
      return confirmPassword.setErrors({mismatchedPasswords: true})
    }
  }
}

  // convenience getter for easy access to form fields
    get f() { return this.registrationForm.controls; }

  onSubmit() {
    this.submitted = true;
    this.error = '';

        // stop here if form is invalid
        if (this.registrationForm.invalid) {
            return;
        }

        this.loading = true;

        this.authenticationService.register(this.f.username.value, this.f.email.value, this.f.password.value, this.f.repeatPassword.value)
        .pipe(first())
            .subscribe(
                data => {
                    this.success = true;
                    //this.router.navigate(['/']);
                },
                error => {
                    this.success = false;
                    this.error = error.error;
                    this.loading = false;
                });

        this.loading = false;
  }

  onSignInClick() {
    this.router.navigate(['/']);
  }

}
