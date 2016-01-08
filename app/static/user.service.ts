import { Injectable } from 'angular2/core'
import { httpInjectables, Http, Response } from 'angular2/http'

import { User } from './user'

@Injectable()
export class UserService {
  constructor(public http: Http) {
  }

  getUser() {
    return this.http.get('/user').map(user => user.json())
  }
}
