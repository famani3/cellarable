import {bootstrap} from 'angular2/platform/browser'
import { HTTP_PROVIDERS } from 'angular2/http'
import { AppComp } from './app.container'

bootstrap(AppComp, [HTTP_PROVIDERS])
