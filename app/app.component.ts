import { Component } from '@angular/core';
import { HeaderComponent } from './components/header/header.component';

@Component({
  selector: 'my-app',
  template: `<header></header>
  			<h1>My First Angular App</h1>
  			
  			<!-- Routed views go here -->
			<router-outlet></router-outlet>`
})
export class AppComponent { }
