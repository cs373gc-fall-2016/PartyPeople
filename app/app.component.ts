import { Component } from '@angular/core';
import { HeaderComponent } from './components/header/header.component';

@Component({
  selector: 'my-app',
  template: `<pp-header></pp-header>
  			
  			<!-- Routed views go here -->
			<router-outlet></router-outlet>`,
})
export class AppComponent { }
