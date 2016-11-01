import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

@Component({
    selector: 'state-details',
    templateUrl: 'app/components/state_details/state_details.html',
})
export class StateDetailsComponent implements OnInit, OnDestroy {
	id: number;
	private sub: any;

	stateName = "Texas";
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
