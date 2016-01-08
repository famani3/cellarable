import { Component, OnInit } from 'angular2/core';
import { User } from './user';
import { UserService } from './user.service';
import 'static/node_modules/rxjs/add/operator/map'

@Component({
  selector: 'my-app',
  template: '<h1>{{title}}</h1><div>{{currentUser.username}}</div>',
  providers: [UserService]
})

export class AppComp implements OnInit {
  public title: string = 'Cellarable';
  public currentUser: User;

  constructor(private _userService: UserService) { }

  getUser() {
    this._userService.getUser().suscribe(user => this.currentUser = user.json());
  }

  ngOnInit() {
    this.getUser()
  }
}

