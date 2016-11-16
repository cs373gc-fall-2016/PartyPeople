import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { AllServicesService } from '../../services/allServices.service';

@Component({
    selector: 'candidate-details',
    templateUrl: 'app/components/candidate_details/candidate_details.html',
    providers: [
    	AllServicesService
    ]
})
export class CandidateDetailsComponent implements OnInit, OnDestroy {
	errorMessage: string;
	id: number;
	private sub: any;

	data = {};
	image = {};

	constructor(private route: ActivatedRoute, private allServicesService: AllServicesService) {}

	ngOnInit() {
	    this.sub = this.route.params.subscribe(params => {
	       this.id = +params['id'];

	       this.allServicesService.getCandidateDetails(this.id).subscribe(
			candidateInfo => {
				this.data = candidateInfo;
				this.allServicesService.getImageData(candidateInfo.name).subscribe(
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