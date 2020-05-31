import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { HeaderComponent } from './header/header.component'
import { LoginFormComponent } from './login-form/login-form.component'
import {MainAppLayoutComponent } from './main-app-layout/main-app-layout.component'


const routes: Routes = [
      { path: 'app', component: MainAppLayoutComponent },
      { path: '', component: LoginFormComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
