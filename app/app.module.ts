import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { RouterModule } from '@angular/router';

import { AppComponent } from './app.component';
import { HeaderComponent } from './components/header/header.component';
import { AboutComponent } from './components/about/about.component';
import { HomeComponent } from './components/home/home.component';
import { TableComponent } from './components/table/table.component';

@NgModule({
  imports: [
  	BrowserModule,
  	RouterModule.forRoot([
  		{ path: 'about', component: AboutComponent },
      { path: 'table', component: TableComponent },
  		{ path: '', component: HomeComponent }      

  	])
  ],
  declarations: [
  	AppComponent,
  	HeaderComponent,
  	AboutComponent,
    HomeComponent,
    TableComponent
  ],
  bootstrap: [ AppComponent ]
})
export class AppModule { }
