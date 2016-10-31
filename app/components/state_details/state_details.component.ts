import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

@Component({
    selector: 'state-details',
    templateUrl: 'app/components/state_details/state_details.html',
})
export class StateDetailsComponent implements OnInit, OnDestroy {
	id: number;
	private sub: any;

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
