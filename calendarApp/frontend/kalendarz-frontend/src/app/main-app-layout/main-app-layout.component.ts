import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';

import { AuthenticationService } from '../services/authentication.service';

@Component({
  selector: 'app-main-app-layout',
  templateUrl: './main-app-layout.component.html',
  styleUrls: ['./main-app-layout.component.css']
})
export class MainAppLayoutComponent implements OnInit {

  constructor(
      private authenticationService: AuthenticationService,
      private router: Router
      )
{
    if (!this.authenticationService.currentUserValue) {
        this.router.navigate(['/']);
    }
}

  ngOnInit(): void {
  }

  public getUserLogin(): string {
    return this.authenticationService.currentUserValue.login;
  }

  public logout(): void {
    this.authenticationService.logout();
    this.router.navigate(['/']);
  }

}
