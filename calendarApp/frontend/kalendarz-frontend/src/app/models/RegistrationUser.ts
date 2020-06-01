export class RegistrationUser {

  login:string;
  email: string;
  password: string;
  repeatedPassword: string;

  constructor(login: string, email: string, password: string, repeatedPassword: string) {
    this.login = login;
    this.email = email;
    this.password = password;
    this.repeatedPassword = repeatedPassword;
    }
}
