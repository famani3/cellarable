import { Component } from 'angular2/core'

let temp: string = 'Testing this crap'

@Component({
  selector: 'my-app',
  template: '<h1>{{title}}</h1>'
})
export class AppComp {
  public title = temp
}

