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
	image = {};

	constructor(private route: ActivatedRoute, private allServicesService: AllServicesService) {}

	ngOnInit() {
	    this.sub = this.route.params.subscribe(params => {
	       this.id = +params['id'];

	       this.allServicesService.getStateDetails(this.id).subscribe(
			stateInfo => {
				this.data = stateInfo,
				this.allServicesService.getImageData(stateInfo.name).subscribe(
				imageData => this.image = imageData,
				error => this.errorMessage = <any>error)
	    	});
	    },
		error => this.errorMessage = <any>error)
	  }

	ngOnDestroy() {
    	this.sub.unsubscribe();
  	}

}
