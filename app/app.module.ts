import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { RouterModule } from '@angular/router';
import { DataTableModule } from 'primeng/primeng';
import { HttpModule } from '@angular/http';

import { AppComponent } from './app.component';
import { HeaderComponent } from './components/header/header.component';
import { AboutComponent } from './components/about/about.component';
import { HomeComponent } from './components/home/home.component';
import { PageNotFoundComponent } from './components/page_not_found/not_found.component';

import { StatesTableComponent } from './components/states_table/states_table.component';
import { StateDetailsComponent } from './components/state_details/state_details.component';

import { CandidatesTableComponent } from './components/candidates_table/candidates_table.component';
import { CandidateDetailsComponent } from './components/candidate_details/candidate_details.component';

import { ElectionsTableComponent } from './components/elections_table/elections_table.component';
import { ElectionDetailsComponent } from './components/election_details/election_details.component';

import { PartiesTableComponent } from './components/parties_table/parties_table.component';
import { PartyDetailsComponent } from './components/party_details/party_details.component';


@NgModule({
  imports: [
    DataTableModule,
  	BrowserModule,
    HttpModule,
  	RouterModule.forRoot([
  		{ 
        path: 'about',
        component: AboutComponent
      },
      {
        path: 'states/:id',
        component: StateDetailsComponent
      },
      {
        path: 'states',
        component: StatesTableComponent
      },
      {
        path: 'candidates/:id',
        component: CandidateDetailsComponent
      },
      {
        path: 'candidates',
        component: CandidatesTableComponent
      },
      {
        path: 'elections/:id',
        component: ElectionDetailsComponent
      },
      {
        path: 'elections',
        component: ElectionsTableComponent
      },
      {
        path: 'parties/:id',
        component: PartyDetailsComponent
      },
      {
        path: 'parties',
        component: PartiesTableComponent
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
    CandidatesTableComponent,
    ElectionsTableComponent,
    PartiesTableComponent,
    StatesTableComponent,
    CandidateDetailsComponent,
    ElectionDetailsComponent,
    PartyDetailsComponent,
    StateDetailsComponent,
    PageNotFoundComponent
  ],
  bootstrap: [ AppComponent ]
})
export class AppModule { }
