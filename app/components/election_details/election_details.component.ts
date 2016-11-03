import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { AllServicesService } from '../../services/allServices.service';

@Component({
    selector: 'election-details',
    templateUrl: 'app/components/election_details/election_details.html',
    providers: [
    	AllServicesService
    ]
})
export class ElectionDetailsComponent implements OnInit, OnDestroy {
	errorMessage: string;
	id: number;
	private sub: any;

	stateName = "Texas";
	columns = ["STATE NAME", "CAPITAL", "POPULATION", "GOVERNOR", "PARTY IN CONTROL"];
	data = {"STATE NAME": "Texas", "CAPITAL": "Austin", "POPULATION": "123123123", "GOVERNOR": "asdf", "PARTY IN CONTROL": "reps"};

	constructor(private route: ActivatedRoute, private allServicesService: AllServicesService) {}

	ngOnInit() {
	    this.sub = this.route.params.subscribe(params => {
	       this.id = +params['id'];

	       this.allServicesService.getElectionDetails(this.id).subscribe(
			electionInfo => this.data = electionInfo,
			error => this.errorMessage = <any>error)
	    });
	  }

	ngOnDestroy() {
    	this.sub.unsubscribe();
  	}

}