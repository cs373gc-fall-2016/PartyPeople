import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { RouterModule } from '@angular/router';

import { AppComponent } from './app.component';
import { HeaderComponent } from './components/header/header.component';
import { AboutComponent } from './components/about/about.component';
import { HomeComponent } from './components/home/home.component';
import { StatesTableComponent } from './components/states_table/states_table.component';
import { StateDetailsComponent } from './components/state_details/state_details.component';
import { PageNotFoundComponent } from './components/page_not_found/not_found.component';

@NgModule({
  imports: [
  	BrowserModule,
  	RouterModule.forRoot([
  		{ 
        path: 'about',
        component: AboutComponent
      },
      {
        path: 'state/:id',
        component: StateDetailsComponent
      },
      {
        path: 'states',
        component: StatesTableComponent
      },
  		{
        path: '',
        component: HomeComponent
      },
      {
        path: '**',
        component: PageNotFoundComponent
      }


  	])
  ],
  declarations: [
  	AppComponent,
  	HeaderComponent,
  	AboutComponent,
    HomeComponent,
    StatesTableComponent,
    StateDetailsComponent,
    PageNotFoundComponent
  ],
  bootstrap: [ AppComponent ]
})
export class AppModule { }
