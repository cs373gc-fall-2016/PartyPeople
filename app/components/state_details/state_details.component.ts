import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { AllServicesService } from '../../services/allServices.service';

@Component({
    selector: 'state-details',
    templateUrl: 'app/components/state_details/state_details.html',
    providers: [
    	AllServicesService
    ]
})
export class StateDetailsComponent implements OnInit, OnDestroy {
	errorMessage: string;
	id: number;
	private sub: any;

	data = {};

	constructor(private route: ActivatedRoute, private allServicesService: AllServicesService) {}

	ngOnInit() {
	    this.sub = this.route.params.subscribe(params => {
	       this.id = +params['id'];

	       this.allServicesService.getStateDetails(this.id).subscribe(
			stateInfo => this.data = stateInfo,
			error => this.errorMessage = <any>error)
	    });
	  }

	ngOnDestroy() {
    	this.sub.unsubscribe();
  	}

}
