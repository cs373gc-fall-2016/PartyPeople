import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

@Component({
    selector: 'party-details',
    templateUrl: 'app/components/party_details/party_details.html',
})
export class PartyDetailsComponent implements OnInit, OnDestroy {
	id: number;
	private sub: any;

	stateName = "Party Name";
	columns = ["STATE NAME", "CAPITAL", "POPULATION", "GOVERNOR", "PARTY IN CONTROL"];
	data = {"STATE NAME": "Texas", "CAPITAL": "Austin", "POPULATION": "123123123", "GOVERNOR": "asdf", "PARTY IN CONTROL": "reps"};

	constructor(private route: ActivatedRoute) {}

	ngOnInit() {
	    this.sub = this.route.params.subscribe(params => {
	       this.id = +params['id'];

	       // In a real app: dispatch action to load the details here.
	    });
	  }

	ngOnDestroy() {
    	this.sub.unsubscribe();
  	}

}